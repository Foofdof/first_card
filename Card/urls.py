from django.urls import path
from . import views

urlpatterns = [
    path('', views.download, name='download'),
    path('post_list/', views.post_list, name='post_list'),
    path('feedback/new/', views.fb_new, name='feedback_edit'),
]