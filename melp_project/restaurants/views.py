from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.db.models import Avg, StdDev, Count
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from .models import Restaurant
from .serializers import RestaurantSerializer

# TASK 1

# Script to update csv file must be runned from console with "python manage.py runscript import_data"

# Resolves GET(ALL) and POST from Restaurants
class RestaurantListCreate(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# Resolves GET, PULL and DELETE from each Restaurants instance
class RestaurantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer   
        
# TASK 2

# Calculate statistics for restaurants within a specific radius
def restaurant_statistics(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    radius = request.GET.get('radius')

    # Check if parameters are valid
    if not (latitude and longitude and radius):
        return JsonResponse({'error': 'Missing parameters'}, status=400)

    # Convert parameters to numeric types
    try:
        latitude = float(latitude)
        longitude = float(longitude)
        radius = float(radius)
    except ValueError:
        return JsonResponse({'error': 'Invalid parameters'}, status=400)

    # Create a Point object to represent the center of the circle
    center_point = Point(longitude, latitude, srid=4326)

    # Calculate the maximum distance in meters for the search
    max_distance = D(m=radius)

    # Filter restaurants that are within the circle
    restaurants_within_radius = Restaurant.objects.filter(
        point__distance_lte=(center_point, max_distance)
    )

    # Calculate Count, Avg and StDev from filtered restaurantes
    statistics = restaurants_within_radius.aggregate(
        count=Count('id'),
        avg_rating=Avg('rating'),
        std_dev_rating=StdDev('rating')
    )

    # Return the results as JSON
    return JsonResponse({
        'count': statistics['count'],
        'avg': statistics['avg_rating'],
        'std': statistics['std_dev_rating']
    })
