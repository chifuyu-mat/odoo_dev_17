#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar la configuración de Odoo
"""

import os
import sys
import configparser

def check_config_file():
    """Verifica que el archivo de configuración esté correcto"""
    print("🔍 Verificando archivo de configuración...")
    
    config_file = 'odoo.conf'
    if not os.path.exists(config_file):
        print("❌ Archivo odoo.conf no encontrado")
        return False
    
    config = configparser.ConfigParser()
    config.read(config_file)
    
    if 'options' not in config:
        print("❌ Sección [options] no encontrada en odoo.conf")
        return False
    
    addons_path = config.get('options', 'addons_path', fallback='')
    print(f"📁 Path de addons: {addons_path}")
    
    # Verificar que los directorios existan
    paths = [p.strip() for p in addons_path.split(',') if p.strip()]
    missing_paths = []
    
    for path in paths:
        if not os.path.exists(path):
            missing_paths.append(path)
    
    if missing_paths:
        print(f"❌ Directorios faltantes: {missing_paths}")
        return False
    
    print("✅ Archivo de configuración correcto")
    return True

def check_required_modules():
    """Verifica que los módulos requeridos existan"""
    print("\n🔍 Verificando módulos requeridos...")
    
    # Verificar módulos en diferentes ubicaciones
    module_locations = [
        ('addons', ['web', 'hr_timesheet']),
        ('odoo/addons', ['base'])
    ]
    
    missing_modules = []
    
    for base_path, modules in module_locations:
        for module in modules:
            module_path = os.path.join(base_path, module)
            if not os.path.exists(module_path):
                missing_modules.append(f"{base_path}/{module}")
    
    if missing_modules:
        print(f"❌ Módulos faltantes: {missing_modules}")
        return False
    
    print("✅ Todos los módulos requeridos están presentes")
    return True

def check_custom_addons():
    """Verifica que el módulo de corrección esté presente"""
    print("\n🔍 Verificando módulo de corrección...")
    
    timesheet_fix_path = os.path.join('custom_addons', 'timesheet_fix')
    if not os.path.exists(timesheet_fix_path):
        print("❌ Módulo timesheet_fix no encontrado en custom_addons")
        return False
    
    required_files = ['__init__.py', '__manifest__.py', 'data/ir_module_category_data.xml']
    missing_files = []
    
    for file in required_files:
        file_path = os.path.join(timesheet_fix_path, file)
        if not os.path.exists(file_path):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Archivos faltantes en timesheet_fix: {missing_files}")
        return False
    
    print("✅ Módulo timesheet_fix está presente y completo")
    return True

def check_database():
    """Verifica el estado de la base de datos"""
    print("\n🔍 Verificando base de datos...")
    
    # Verificar que PostgreSQL esté configurado
    config = configparser.ConfigParser()
    config.read('odoo.conf')
    
    db_name = config.get('options', 'db_name', fallback='')
    db_user = config.get('options', 'db_user', fallback='')
    db_port = config.get('options', 'db_port', fallback='5432')
    
    print(f"📊 Base de datos: {db_name}")
    print(f"👤 Usuario: {db_user}")
    print(f"🔌 Puerto: {db_port}")
    
    # Intentar conectar a la base de datos
    try:
        import psycopg2
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=config.get('options', 'db_password', fallback=''),
            host='localhost',
            port=db_port
        )
        conn.close()
        print("✅ Conexión a la base de datos exitosa")
        return True
    except ImportError:
        print("⚠️  psycopg2 no está instalado, no se puede verificar la conexión")
        return True
    except Exception as e:
        print(f"❌ Error conectando a la base de datos: {e}")
        return False

def main():
    """Función principal de verificación"""
    print("=== Verificación de Configuración Odoo ===\n")
    
    checks = [
        check_config_file,
        check_required_modules,
        check_custom_addons,
        check_database
    ]
    
    all_passed = True
    
    for check in checks:
        if not check():
            all_passed = False
    
    print("\n" + "="*50)
    if all_passed:
        print("✅ Todas las verificaciones pasaron")
        print("🚀 Odoo está listo para usar")
    else:
        print("❌ Algunas verificaciones fallaron")
        print("🔧 Revisa los errores anteriores")
    
    return all_passed

if __name__ == "__main__":
    main()
