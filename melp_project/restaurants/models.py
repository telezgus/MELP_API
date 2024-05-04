from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Restaurant(models.Model):
    id = models.TextField(primary_key=True)
    rating = models.IntegerField()
    name = models.TextField()
    site = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    point = models.PointField(null=True, blank=True) # Field to store location as a point

    def save(self, *args, **kwargs):
        # Create a Point object based on latitude and longitude
        if self.lat is not None and self.lng is not None:
            self.point = Point(self.lng, self.lat)
        super().save(*args, **kwargs)
