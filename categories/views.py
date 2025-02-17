from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer
from django.http import Http404
from rest_framework.permissions import IsAdminUser

class CategoryListCreateView(APIView):
    
    permission_classes = [IsAdminUser]
    
    def get(self, request):

        categories = Category.objects.all()
        
        name_param = request.GET.get('name')
        if name_param:
            categories = categories.filter(name=name_param)

        search_param = request.GET.get('search')
        if search_param:
            categories = categories.filter(description__icontains=search_param)
            
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):

    permission_classes = [IsAdminUser]
    
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):

        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):

        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import generics
from rest_framework.response import Response
from .documents import CategoryDocument

class CategorySearchView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        Search the 'categories_index' using the user's query from ?q=<term>.
        """
        query = self.request.query_params.get('q', None)
        if query:
            search = CategoryDocument.search().query("match", name=query)
            results = search.execute()

            category_ids = [hit.meta.id for hit in results]

            return Category.objects.filter(pk__in=category_ids)

        return Category.objects.all()
