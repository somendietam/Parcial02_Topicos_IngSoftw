# Utiliza una imagen base de Python
FROM python:3.9

# Define /app como el directorio de trabajo
WORKDIR /app

# Añade el archivo de dependencias al contenedor
COPY requirements.txt .

# Realiza la instalación de las librerías necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Transfiere los archivos de la aplicación al contenedor
COPY . .

# Abre el puerto 5000 para permitir acceso externo a Flask
EXPOSE 5000

# Comando para iniciar el servidor de Flask
CMD ["python", "app.py"]
