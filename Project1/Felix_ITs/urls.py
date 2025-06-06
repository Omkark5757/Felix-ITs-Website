from django.urls import path 
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.all_felix, name='all_felix'), 
    
    path('all/', views.all_felix), # /Felix_ITs/all/
    path('create/', views.create_course, name='create_course'),  # /Felix_ITs/create/
    path('update/<int:pk>/', views.update_course, name='update_course'),
    path('delete/<int:pk>/', views.delete_course, name='delete_course'),
]
