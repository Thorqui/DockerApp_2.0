FROM nginx:latest

# Copiamos la configuración personalizada de Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copiamos los archivos del sitio
COPY index.html /usr/share/nginx/html/
COPY styles.css /usr/share/nginx/html/

EXPOSE 80
