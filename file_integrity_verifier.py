# file_integrity_verifier.py

import hashlib
import os

def calculate_sha256(filepath: str):
    """
    Calcula el hash SHA-256 de un archivo dado leyendo el contenido en bloques (chunks).

    Args:
        filepath: La ruta completa al archivo a hashear.

    Returns:
        El hash SHA-256 del archivo en formato hexadecimal, o None si ocurre un error.
    """
    # Eliminar comillas dobles o simples que el usuario pueda ingresar por arrastrar/soltar o copiar ruta
    filepath = filepath.strip("'\"")

    if not os.path.exists(filepath):
        print(f"\n❌ Error: El archivo '{filepath}' no fue encontrado.")
        return None
        
    try:
        # Inicializa el objeto hash para SHA-256
        hasher = hashlib.sha256()
        
        # Abre el archivo en modo lectura binaria ('rb')
        with open(filepath, 'rb') as file:
            # Lee el archivo en bloques de 64KB (chunk) para manejar archivos grandes eficientemente
            while True:
                chunk = file.read(65536) # 64KB
                if not chunk:
                    break
                hasher.update(chunk) # Actualiza el hash con el bloque leído
        
        # Devuelve la representación hexadecimal del hash
        return hasher.hexdigest()

    except Exception as e:
        print(f"\n❌ Ocurrió un error al calcular el hash del archivo: {e}")
        return None

def calculate_and_display_hash(filepath: str):
    """Calcula y muestra el hash de un archivo especificado."""
    print("\n" + "=" * 40)
    print("     CALCULANDO HASH DEL ARCHIVO...")
    print("=" * 40)
    hash_calculado = calculate_sha256(filepath)

    if hash_calculado:
        print(f"\n✅ Hash SHA-256 calculado para '{os.path.basename(filepath)}':")
        print("-" * 40)
        print(hash_calculado)
        print("-" * 40 + "\n")


def compare_hashes():
    """Permite al usuario comparar un hash calculado con uno esperado."""
    print("\n" + "=" * 40)
    print("      VERIFICACIÓN DE INTEGRIDAD")
    print("=" * 40)

    # 1. Obtener ruta del archivo a verificar
    filepath = input("Por favor, introduce la ruta del archivo que deseas verificar: ").strip()
    if not filepath:
        print("\n🛑 Cancelando verificación. Debe ingresar una ruta.")
        return

    # 2. Obtener hash esperado
    hash_esperado = input("Introduce el hash SHA-256 *original* (o deja vacío para calcular sin comparación): ").strip().lower()

    # 3. Calcular el hash actual
    hash_calculado = calculate_sha256(filepath)
    
    if hash_calculado is None:
        print("🚨 No se pudo calcular el hash. Verificación detenida.")
        return

    # 4. Comparación
    print("\n" + "=" * 40)
    print("       RESULTADO DE LA VERIFICACIÓN")
    print("=" * 40)
    print(f"Archivo verificado: {os.path.basename(filepath)}")
    print(f"Hash Calculado:     {hash_calculado}")

    if hash_esperado and hash_calculado == hash_esperado:
        # La comparación más importante
        print("\n🎉 ¡VERIFICACIÓN EXITOSA! El archivo no ha sido modificado.")
    elif not hash_esperado:
         # Si solo se calcula y no se compara, simplemente informar.
         pass
    else:
        print("\n❌ ¡ADVERTENCIA! EL CONTENIDO DEL ARCHIVO HA CAMBIADO.")
        print("=======================================")

    return


def main_menu():
    """Menú principal para la herramienta Verificador de Integridad."""
    while True:
        print("\n" + "*" * 40)
        print("     VERIFICADOR DE INTEGRIDAD (HASH)")
        print("*" * 40)
        print("1. Calcular y mostrar el Hash SHA-256 de un archivo")
        print("2. Comparar con Hash proporcionado (Verificar Integridad)")
        print("3. Salir")

        opcion = input("Selecciona una opción (1/2/3): ").strip()

        if opcion == '1':
            filepath = input("Introduce la ruta del archivo para calcular su hash: ").strip()
            if filepath:
                calculate_and_display_hash(filepath)
            else:
                print("🛑 Debe introducir una ruta de archivo válida.")
        
        elif opcion == '2':
            compare_hashes()

        elif opcion == '3':
            print("\n👋 ¡Saliendo del Verificador de Integridad! Adiós.")
            break
        
        else:
            print("⚠️ Opción no válida. Por favor, selecciona 1, 2 o 3.")


if __name__ == "__main__":
    # Nota: Para probar esta herramienta, asegúrate de tener un archivo real en el sistema (ej: test.txt)
    # y pasar su ruta cuando se te solicite.
    main_menu()