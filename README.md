# 🐳 DockerApp - Sitio Web Estático con Backend Flask

Un proyecto de ejemplo para tu portafolio: una **aplicación web estática** servida con **Nginx** en el frontend y un **backend Flask** que expone una API, todo orquestado con **Docker Compose**.  
Ideal para aprender a desplegar aplicaciones completas con contenedores.


## 📋 Descripción

DockerApp combina un frontend estático (HTML5 y CSS3) servido por Nginx con un backend Flask que expone una API. Ambos componentes están contenerizados con Docker y orquestados mediante Docker Compose, facilitando el despliegue y la escalabilidad.


## 🛠️ Tecnologías Utilizadas

| Componente       | Tecnologías                              |
|------------------|------------------------------------------|
| **Frontend**     | HTML5, CSS3, Nginx                       |
| **Backend**      | Python 3.10, Flask, Flask-CORS           |
| **Contenerización** | Docker, Docker Compose                 |


## 📂 Estructura del Proyecto

```plaintext
DockerApp/
├── backend/
│   ├── app.py             # Servidor Flask
│   ├── requirements.txt   # Dependencias de Python
│   └── Dockerfile         # Configuración del backend
├── frontend/
│   ├── index.html         # Página principal
│   ├── styles.css         # Estilos CSS
│   └── Dockerfile         # Configuración del frontend (Nginx)
└── docker-compose.yml     # Orquestación de frontend y backend
```

## 🚀 Cómo Ejecutar el Proyecto
  Sigue estos pasos para correr el proyecto localmente:

1. **Clona el repositorio**
  ```bash
  git clone https://github.com/Thorqui/DockerApp.git
  cd DockerApp
  ```

3. **Construye y ejecuta los contenedores con Docker Compose**
  ```bash
  bashdocker-compose up --build
 ```

4. **Accede al sitio**
  Abre tu navegador y visita:
  🌐 http://localhost:8080
  La API estará disponible en:
  🌐 http://localhost:5000 (o el puerto configurado en docker-compose.yml).


## 🧱 Dockerfiles
**Frontend (Nginx)**
  dockerfile
  ```bash
  FROM nginx:latest
  COPY . /usr/share/nginx/html
 ```

**Backend (Flask)**
  dockerfile
  ```bash
  FROM python:3.10-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  COPY . .
  EXPOSE 5000
  CMD ["python", "app.py"]
 ```

## 🧠 Objetivo del Proyecto
Creación y contenerización de aplicaciones web con Docker.
Orquestación de múltiples servicios con Docker Compose.
Integración de un frontend estático con un backend dinámico.


👨‍💻 Autor
Aitor (Thorqui)
🔗 GitHub - Thorqui

💡 Notas Adicionales

- Asegúrate de tener Docker y Docker Compose instalados en tu sistema.
- Puedes personalizar los puertos en el archivo docker-compose.yml si es necesario.
- Verifica que el puerto 8080 (frontend) y 5000 (backend) estén libres antes de ejecutar.
