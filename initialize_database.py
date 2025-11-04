#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para inicializar la base de datos lab05 con el módulo base
"""

import os
import sys
import subprocess

def initialize_database():
    """Inicializa la base de datos lab05 con el módulo base"""
    
    # Obtener el directorio actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Comando para inicializar la base de datos
    cmd = [
        sys.executable,
        os.path.join(current_dir, 'odoo-bin'),
        '-d', 'lab05',
        '-i', 'base',
        '--stop-after-init'
    ]
    
    print("Inicializando base de datos lab05...")
    print(f"Comando: {' '.join(cmd)}")
    
    try:
        # Ejecutar el comando
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=current_dir)
        
        if result.returncode == 0:
            print("✅ Base de datos inicializada correctamente")
            print("Salida:", result.stdout)
        else:
            print("❌ Error al inicializar la base de datos")
            print("Error:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error ejecutando el comando: {e}")
        return False
    
    return True

def install_timesheet_fix():
    """Instala el módulo timesheet_fix después de inicializar la base de datos"""
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    cmd = [
        sys.executable,
        os.path.join(current_dir, 'odoo-bin'),
        '-d', 'lab05',
        '-i', 'timesheet_fix',
        '--stop-after-init'
    ]
    
    print("\nInstalando módulo timesheet_fix...")
    print(f"Comando: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=current_dir)
        
        if result.returncode == 0:
            print("✅ Módulo timesheet_fix instalado correctamente")
            print("Salida:", result.stdout)
        else:
            print("❌ Error al instalar timesheet_fix")
            print("Error:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error ejecutando el comando: {e}")
        return False
    
    return True

def main():
    """Función principal"""
    print("=== Inicialización de Base de Datos Odoo ===")
    
    # Paso 1: Inicializar base de datos
    if not initialize_database():
        print("❌ Falló la inicialización de la base de datos")
        return
    
    # Paso 2: Instalar módulo de corrección
    if not install_timesheet_fix():
        print("⚠️  No se pudo instalar timesheet_fix, pero la base de datos está inicializada")
    
    print("\n✅ Proceso completado. Puedes iniciar Odoo normalmente.")

if __name__ == "__main__":
    main()
