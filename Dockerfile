# 1. Empezamos desde la imagen oficial de Odoo 17
FROM odoo:17.0

# 2. Cambiamos al usuario root para instalar dependencias
USER root

# 3. (NUEVO) Instalamos dependencias de Linux
#    Necesarias para 'python-ldap' y otras librerías.
RUN apt-get update && apt-get install -y \
    libldap2-dev \
    libsasl2-dev \
    && apt-get clean

# 4. Instalamos librerías de Python desde requirements.txt
COPY requirements.txt /etc/odoo/
RUN pip install -r /etc/odoo/requirements.txt

# 5. Copiamos los módulos personalizados
COPY ./Hotel /mnt/extra-addons/Hotel
COPY ./ConsultingERP /mnt/extra-addons/ConsultingERP

# 6. Creamos directorios y configuramos permisos
RUN mkdir -p /var/log/odoo /var/lib/odoo && \
    chown -R odoo:odoo /mnt/extra-addons /var/log/odoo /var/lib/odoo

# 7. Volvemos al usuario 'odoo' por seguridad
USER odoo