from django.urls import path
from places import views

urlpatterns = [
    path('places/', views.work_list),
    path('places/<int:pk>/', views.work_detail),
]