from django.urls import path 
from .import views 

urlpatterns = [

    path('', views.app_home, name='app'),
    path('blog/', views.blog, name='blog')

]
