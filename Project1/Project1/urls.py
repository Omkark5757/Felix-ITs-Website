from django.contrib import admin
from django.urls import path, include
from Project1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('Felix_ITs.urls')),# /Felix_ITs/
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('placement/', views.placement, name='placement'),
    path('faqs/', views.faqs, name='faqs'),
    
    path('Felix_ITs/', include('Felix_ITs.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

