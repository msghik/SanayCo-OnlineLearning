from django.urls import path
from .views import (
    course_list,
    course_detail,
    course_create,
    course_update,
    course_delete,
    CourseUploadVideoView
)


urlpatterns = [
    path('', course_list, name='course-list'),
    path('create/', course_create, name='course-create'),
    path('<int:pk>/', course_detail, name='course-detail'),
    path('<int:pk>/update/', course_update, name='course-update'),
    path('<int:pk>/delete/', course_delete, name='course-delete'),
    
    path('<int:pk>/upload-video/', CourseUploadVideoView.as_view(), name='course-upload-video'),
]


