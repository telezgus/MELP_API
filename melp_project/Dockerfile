# Usa una imagen base de Python (o cualquier otra imagen base que necesites)
FROM python:3.11

# Instala los paquetes necesarios
RUN apt-get update && \
    apt-get install -y binutils libproj-dev gdal-bin && \
    rm -rf /var/lib/apt/lists/*

# Copia tu aplicación y archivos necesarios
COPY . /app

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Ejecuta tu aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]