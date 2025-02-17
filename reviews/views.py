from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsOwner


class ReviewListCreateView(APIView):
    
    permission_classes = [AllowAny]
    
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailView(APIView):
    
    def get_permissions(self):
        
        if self.request.method == 'GET':
            return [AllowAny]
        return [IsAdminUser | IsOwner]
    
        
    def get_object(self, pk):
        return get_object_or_404(Review, pk=pk)

    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
from .documents import ReviewDocument
from .models import Review
from .serializers import ReviewSerializer 

class ReviewSearchView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        """
        We'll search 'reviews_index' for the user's query from ?q=<term>
        and return the corresponding Django queryset.
        """
        query = self.request.query_params.get('q')
        if query:

            search = ReviewDocument.search().query(
                    "multi_match",
                    query=query,
                    fields=["content", "rating"]
            )
            
            results = search.execute()

            review_ids = [hit.meta.id for hit in results]

            return Review.objects.filter(pk__in=review_ids)
        
        return Review.objects.all()
