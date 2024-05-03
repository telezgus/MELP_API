# API Documentation

## Overview
This API provides endpoints to interact with restaurant data. It allows users to perform CRUD operations on restaurant objects and retrieve statistics about restaurants within a specified radius.

## Endpoints

### 1. Retrieve a list of restaurants
- **URL:** `/api/restaurants/`
- **Method:** `GET`
- **Description:** This endpoint retrieves a list of all restaurants.

### 2. Create a new restaurant
- **URL:** `/api/restaurants/`
- **Method:** `POST`
- **Description:** This endpoint creates a new restaurant object.

### 3. Retrieve details of a restaurant
- **URL:** `/api/restaurants/<id>/`
- **Method:** `GET`
- **Description:** This endpoint retrieves details of a specific restaurant identified by its unique ID.

### 4. Update a restaurant
- **URL:** `/api/restaurants/<id>/`
- **Method:** `PUT`
- **Description:** This endpoint updates an existing restaurant object.

### 5. Delete a restaurant
- **URL:** `/api/restaurants/<id>/`
- **Method:** `DELETE`
- **Description:** This endpoint deletes a specific restaurant identified by its unique ID.

### 6. Calculate statistics for restaurants within a specific radius
- **URL:** `/api/restaurants/statistics/`
- **Method:** `GET`
- **Parameters:**
  - `latitude`: Latitude coordinate of the center of the circle
  - `longitude`: Longitude coordinate of the center of the circle
  - `radius`: Radius of the circle in meters
- **Description:** This endpoint calculates statistics for restaurants within a specified radius from a given latitude and longitude coordinate.
