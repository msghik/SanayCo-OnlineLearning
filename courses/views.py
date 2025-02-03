from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny

@api_view(['GET'])
def course_list(request):
    
    courses = Course.objects.filter(is_published=True)

    category_name = request.GET.get('category')
    if category_name:
        courses = courses.filter(category__name=category_name)

    search_param = request.GET.get('search')
    if search_param:
        courses = courses.filter(category__description__icontains=search_param)

    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def course_detail(request, pk):
    
    course = get_object_or_404(Course, pk=pk, is_published = True)
    serializer = CourseSerializer(course)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def course_create(request):

    if request.user.role not in ['instructor', 'admin']:
        return Response(
            {"detail": "Only instructors or admins can create courses."},
            status=status.HTTP_403_FORBIDDEN
        )

    data = request.data.copy()
    
    if request.user.role == 'instructor':
        data['instructor'] = request.user.id
        
    users_data = data.pop('users', None)
    
    serializer = CourseSerializer(data=data)
    if serializer.is_valid():
        course = serializer.save()

        if users_data is not None:          
            course.users.set(users_data)
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    if request.user.role == 'instructor' and course.instructor != request.user:
        return Response(
            {"detail": "You do not have permission to update this course."},
            status=status.HTTP_403_FORBIDDEN
        )
    if request.user.role not in ['instructor', 'admin']:
        return Response(
            {"detail": "Only instructors or admins can update courses."},
            status=status.HTTP_403_FORBIDDEN
        )

    data = request.data.copy()
    
    if request.user.role == 'instructor':
        data['instructor'] = request.user.id


    users_data = data.pop('users', None)
    
    
    serializer = CourseSerializer(course, data=data, partial=True)
    if serializer.is_valid():
        course = serializer.save()
        
        if users_data is not None:
            course.users.set(users_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    if request.user.role == 'instructor' and course.instructor != request.user:
        return Response(
            {"detail": "You do not have permission to delete this course."},
            status=status.HTTP_403_FORBIDDEN
        )

    if request.user.role not in ['instructor', 'admin']:
        return Response(
            {"detail": "Only instructors or admins can delete courses."},
            status=status.HTTP_403_FORBIDDEN
        )
    
    course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

