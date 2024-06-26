# MELP API

The MELP API is a RESTful API designed to provide information about restaurants and their statistics based on geographical locations.

## Requirements

- Python
- PostgreSQL
- PostGIS

## Installation

To install the MELP API, follow these steps:

### Using Docker

To run this project locally, you'll need to have Docker installed on your machine. Follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Build the Docker image by running the following command:

```
docker build -t api_melp .
```

4. Once the image is built successfully, you can run the container with the following command:

```
docker run -p 8000:8000 image_name
```

This will start the server, and you can access the application from your web browser at http://localhost:8000.

### Without Docker

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Configure your database settings in `settings.py`.
4. Run migrations using `python manage.py migrate`.
5. Start the development server using `python manage.py runserver`.

## Usage

### Endpoints

- `/restaurants/`: List all restaurants and create new ones.
- `/restaurants/<id>/`: Retrieve, update, or delete a specific restaurant.
- `/restaurants/statistics/`: Get statistics for restaurants within a specified radius.

### Example Requests

#### Get restaurant statistics

```
GET /restaurants/statistics/?latitude=19.4341320322948&longitude=-99.1326235608364&radius=5000
```

#### Create a new restaurant

POST /restaurants/

```
{
"id": "1",
"rating": 4,
"name": "La Cantina",
"site": "www.lacantina.com",
"email": "info@lacantina.com",
"phone": "123-456-7890",
"street": "123 Main St",
"city": "New York",
"state": "NY",
"lat": 40.7128,
"lng": -74.0060
}
```


For more examples and details, please refer to the [API documentation](api_documentation.md).

## Configuration

Refer to `settings_pord.py` for available configuration options.

## Importing Data

To import data from the CSV file containing restaurant information, run the following command:

```
python manage.py runscript import_data
```

## Documentation

For detailed information about the API endpoints and usage, please refer to the [API documentation](api_documentation.md).
