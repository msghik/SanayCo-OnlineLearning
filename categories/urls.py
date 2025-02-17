from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView
from .views import CategorySearchView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='category-list-create'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    
    path('search/', CategorySearchView.as_view(), name='category-search'),
]
