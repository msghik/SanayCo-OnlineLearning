from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser
from .permissions import IsOwner, IsInstructor
from rest_framework.views import APIView
import os
from django.conf import settings

 
@api_view(['GET'])
@permission_classes([AllowAny])
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
@permission_classes([IsAdminUser | IsInstructor])
def course_create(request):

    data = request.data
    users_data = data.pop('users', None)
    
    serializer = CourseSerializer(data=data)
    if serializer.is_valid():
        course = serializer.save()

        if users_data is not None:          
            course.users.set(users_data)
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAdminUser | IsOwner])
def course_update(request, pk):
    
    course = get_object_or_404(Course, pk=pk)
    data = request.data
    
    users_data = data.pop('users', None)
    
    serializer = CourseSerializer(course, data=data, partial=True)
    if serializer.is_valid():
        course = serializer.save()
        
        if users_data is not None:
            course.users.set(users_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@permission_classes([IsAdminUser | IsOwner])
def course_delete(request, pk):
    
    course = get_object_or_404(Course, pk=pk)
    
    course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class CourseUploadVideoView(APIView):
    
    def post(self, request, pk):

        course = get_object_or_404(Course, pk=pk)
        uploaded_file = request.FILES.get('video')  

        if not uploaded_file:
            return Response({"detail": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)


        file_extension = os.path.splitext(uploaded_file.name)[1]
        new_filename = f"course_{pk}_video{file_extension}"
        file_path = os.path.join("course_videos", new_filename) 


        full_path = os.path.join(settings.MEDIA_ROOT, file_path)
        with open(full_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)


        course.video = file_path
        course.save()

 
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
# courses/views.py

from rest_framework import generics
from rest_framework.response import Response
from .documents import CourseDocument

class CourseSearchView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        """
        We'll search the 'courses_index' for the user's query and
        then return the corresponding Django queryset so we can reuse our DRF serializer.
        """
        query = self.request.query_params.get('q', None)
        if query:

            search = CourseDocument.search().query("match", title=query)
            
            results = search.execute()
            
            course_ids = [hit.meta.id for hit in results]
            
            return Course.objects.filter(pk__in=course_ids)
        
        # If no query
        return Course.objects.all()

    

