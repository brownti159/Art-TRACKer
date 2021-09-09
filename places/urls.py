from django.urls import path
from places import views

urlpatterns = [
    path('places/artists', views.artist_list),
    path('places/artists/<int:pk>/', views.artist_detail),
    path('places/works', views.work_list),
    path('places/works/<int:pk>/', views.work_detail),
]