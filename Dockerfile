# 1. Empezamos desde la imagen oficial de Odoo 17
FROM odoo:17.0

# 2. Cambiamos al usuario root para instalar dependencias
USER root

# 3. Instalamos librerías de Python desde requirements.txt
COPY requirements.txt /etc/odoo/
RUN pip install -r /etc/odoo/requirements.txt

# 4. (OPCIONAL) Paquetes de Linux
# RUN apt-get update && apt-get install -y wkhtmltopdf && apt-get clean

# 5. Copiamos los módulos personalizados
COPY ./Hotel /mnt/extra-addons/Hotel
COPY ./ConsultingERP /mnt/extra-addons/ConsultingERP

# 6. Creamos directorios y configuramos permisos
# NO copiamos odoo.conf, usaremos variables de entorno
RUN mkdir -p /var/log/odoo /var/lib/odoo && \
    chown -R odoo:odoo /mnt/extra-addons /var/log/odoo /var/lib/odoo

# 7. Volvemos al usuario 'odoo' por seguridad
USER odoo