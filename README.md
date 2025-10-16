# 🐳 DockerApp – Sitio Web Estático con Backend Flask

Proyecto de ejemplo para mi portafolio: una aplicación web estática servida con **Nginx** en frontend y un **backend Flask** que expone una API, todo dentro de contenedores **Docker**.  
Ideal para aprender a desplegar un proyecto completo con Docker Compose.

---

## 🚀 Tecnologías utilizadas

- **Frontend:** HTML5, CSS3, Nginx  
- **Backend:** Python 3.10, Flask, Flask-CORS  
- **Contenerización:** Docker, Docker Compose

---

## 🧩 Estructura del proyecto

DockerApp/
│
├── backend/
│ ├── app.py # Servidor Flask
│ ├── requirements.txt # Dependencias de Python
│ └── Dockerfile # Dockerfile backend
│
├── frontend/
│ ├── index.html # Página principal
│ ├── styles.css # Estilos
│ └── Dockerfile # Dockerfile frontend (Nginx)
│
└── docker-compose.yml # Orquesta frontend y backend

---

## ⚙️ Cómo ejecutar el proyecto localmente

1️⃣ **Clona este repositorio:**
```bash
git clone https://github.com/Thorqui/DockerApp.git
cd DockerApp
2️⃣ Construye la imagen Docker:

bash
Copiar código
docker build -t dockerapp .
3️⃣ Ejecuta el contenedor:

bash
Copiar código
docker run -d -p 8080:80 --name web dockerapp
4️⃣ Abre el sitio en el navegador:
👉 http://localhost:8080

🧱 Dockerfile utilizado
dockerfile
Copiar código
FROM nginx:latest
COPY . /usr/share/nginx/html
Simple y eficiente: copia tus archivos HTML/CSS al contenedor Nginx y los sirve directamente.

🧠 Objetivo del proyecto
Este proyecto forma parte de mi portafolio como desarrollador, demostrando:

Capacidad para crear y dockerizar aplicaciones web

Comprensión del flujo build → run en Docker


👨‍💻 Autor
Aitor (Thorqui)
🔗 GitHub – Thorqui
