import pandas as pd
from restaurants.models import Restaurant
import os
import django


# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'melp_project.settings')
django.setup()


def import_data_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    for _, row in df.iterrows():
        Restaurant.objects.create(
            id=row['id'],
            rating=row['rating'],
            name=row['name'],
            site=row['site'],
            email=row['email'],
            phone=row['phone'],
            street=row['street'],
            city=row['city'],
            state=row['state'],
            lat=row['lat'],
            lng=row['lng']
        )


import_data_from_csv('data/restaurantes.csv')