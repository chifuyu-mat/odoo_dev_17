#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar la configuración del addons_path
"""

import os
import configparser

def check_addons_path():
    """Verifica que todos los módulos estén correctamente configurados"""
    print("🔍 Verificando configuración del addons_path...\n")
    
    # Leer configuración
    config = configparser.ConfigParser()
    config.read('odoo.conf')
    
    addons_path = config.get('options', 'addons_path', fallback='')
    paths = [path.strip() for path in addons_path.split(',')]
    
    print("📁 Paths configurados:")
    for i, path in enumerate(paths, 1):
        print(f"  {i}. {path}")
    
    print("\n🔍 Verificando existencia de directorios...")
    
    missing_paths = []
    existing_paths = []
    
    for path in paths:
        if os.path.exists(path):
            existing_paths.append(path)
            print(f"✅ {path}")
        else:
            missing_paths.append(path)
            print(f"❌ {path} - NO EXISTE")
    
    print(f"\n📊 Resumen:")
    print(f"  ✅ Directorios existentes: {len(existing_paths)}")
    print(f"  ❌ Directorios faltantes: {len(missing_paths)}")
    
    if missing_paths:
        print(f"\n⚠️  Directorios que no existen:")
        for path in missing_paths:
            print(f"    - {path}")
    
    # Verificar módulos en cada directorio
    print(f"\n🔍 Verificando módulos en cada directorio...")
    
    total_modules = 0
    for path in existing_paths:
        if os.path.exists(path):
            modules = []
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    manifest_path = os.path.join(item_path, '__manifest__.py')
                    if os.path.exists(manifest_path):
                        modules.append(item)
            
            if modules:
                print(f"✅ {path} - {len(modules)} módulos encontrados")
                total_modules += len(modules)
            else:
                print(f"⚠️  {path} - Sin módulos (solo directorio contenedor)")
    
    print(f"\n📊 Total de módulos encontrados: {total_modules}")
    
    return len(missing_paths) == 0

def main():
    """Función principal"""
    print("=== Verificación de Addons Path ===\n")
    
    success = check_addons_path()
    
    if success:
        print("\n🎉 ¡Configuración correcta!")
        print("Todos los directorios existen y están configurados correctamente.")
    else:
        print("\n⚠️  Problemas detectados:")
        print("Algunos directorios no existen. Revisa la configuración.")

if __name__ == "__main__":
    main()
