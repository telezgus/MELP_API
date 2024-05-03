from django.urls import path
from .views import RestaurantListCreate, RestaurantRetrieveUpdateDestroy, restaurant_statistics

urlpatterns = [
    path('restaurants/', RestaurantListCreate.as_view(), name='restaurant-list-create'),
    path('restaurants/statistics/', restaurant_statistics, name='restaurant-statistics'),
    path('restaurants/<str:pk>/', RestaurantRetrieveUpdateDestroy.as_view(), name='restaurant-retrieve-update-destroy'),

]