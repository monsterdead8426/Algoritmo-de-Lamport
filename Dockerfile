# Usa una imagen de Python
FROM python:3.9

# Copia el programa al contenedor
COPY app.py /app/app.py

# Configura el directorio de trabajo
WORKDIR /app

# Instala Flask (para la comunicación HTTP)
RUN pip install flask requests

# Ejecuta el programa
CMD ["python", "app.py"]
