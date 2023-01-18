from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPostData, name='getPostData'),
    path('<slug:slug>/', views.postFullDetail, name="postFullDetail"),
   
]