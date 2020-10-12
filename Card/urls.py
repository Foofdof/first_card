from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('feedback/new/', views.fb_new, name='feedback_edit'),
]