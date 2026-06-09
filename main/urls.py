from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('info/', views.important_info, name='info'),
    path('documents/', views.documents, name='documents'),
    path('reports/', views.reports, name='reports'),
]
