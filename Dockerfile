# Imagen base
FROM python:3.12

# Establece el directorio de trabajo
WORKDIR /code

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Instala dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código
COPY . .
