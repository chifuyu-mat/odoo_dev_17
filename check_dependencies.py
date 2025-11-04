#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar las dependencias de Python requeridas por Odoo
"""

import importlib
import sys

def check_dependency(module_name, package_name=None):
    """Verifica si un módulo está disponible"""
    try:
        importlib.import_module(module_name)
        print(f"✅ {module_name} - Disponible")
        return True
    except ImportError:
        package = package_name or module_name
        print(f"❌ {module_name} - NO DISPONIBLE (instalar: pip install {package})")
        return False

def main():
    """Verifica todas las dependencias requeridas"""
    print("=== Verificación de Dependencias de Python ===\n")
    
    # Lista de dependencias críticas para Odoo
    dependencies = [
        ('odoo', 'odoo'),
        ('psycopg2', 'psycopg2-binary'),
        ('werkzeug', 'werkzeug'),
        ('jinja2', 'jinja2'),
        ('markupsafe', 'markupsafe'),
        ('polib', 'polib'),
        ('dateutil', 'python-dateutil'),
        ('num2words', 'num2words'),
        ('pandas', 'pandas'),
        ('pdfminer', 'pdfminer.six'),
        ('numpy', 'numpy'),
        ('pytz', 'pytz'),
        ('tzdata', 'tzdata'),
        ('cryptography', 'cryptography'),
        ('cffi', 'cffi'),
        ('pycparser', 'pycparser'),
        ('charset_normalizer', 'charset-normalizer'),
    ]
    
    all_available = True
    missing_deps = []
    
    for module, package in dependencies:
        if not check_dependency(module, package):
            all_available = False
            missing_deps.append(package)
    
    print("\n" + "="*50)
    
    if all_available:
        print("✅ Todas las dependencias están instaladas correctamente")
        print("🚀 Odoo debería funcionar sin problemas de dependencias")
    else:
        print("❌ Faltan algunas dependencias")
        print("📦 Instala las dependencias faltantes con:")
        print(f"pip install {' '.join(missing_deps)}")
    
    return all_available

if __name__ == "__main__":
    main()
