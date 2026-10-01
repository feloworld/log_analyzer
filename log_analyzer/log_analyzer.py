# log_analyzer.py

import re
from collections import defaultdict

def analyze_logs(log_file_path: str):
    """
    Lee un archivo de logs y detecta patrones específicos, como múltiples 
    intentos fallidos de inicio de sesión.

    Args:
        log_file_path (str): La ruta al archivo de log a analizar.

    Returns:
        dict: Un diccionario con los resultados del análisis.
    """
    print(f"--- Iniciando análisis del archivo: {log_file_path} ---")
    
    # Diccionario para almacenar el conteo de intentos fallidos por usuario (o ID)
    failed_login_attempts = defaultdict(int)
    
    # Patrón de expresión regular para capturar la información relevante.
    # Asumimos un formato como: "[TIMESTAMP] INFO: LOGIN FAILED for user: [USERNAME]"
    # Este patrón captura el nombre de usuario después de "user: ".
    login_failed_pattern = re.compile(r"LOGIN FAILED.*for user: (\w+)")

    try:
        with open(log_file_path, 'r') as f:
            line_number = 0
            for line in f:
                line_number += 1
                # Buscar el patrón de fallo de inicio de sesión en la línea
                match = login_failed_pattern.search(line)
                
                if match:
                    username = match.group(1)  # El nombre capturado por el grupo (el usuario)
                    failed_login_attempts[username] += 1
                    print(f"[Línea {line_number}] DETECTADO: Fallo de login para '{username}'.")

    except FileNotFoundError:
        print(f"\n[ERROR] Archivo no encontrado en la ruta especificada: {log_file_path}")
        return {"status": "Error", "message": f"Archivo no encontrado: {log_file_path}"}
    except Exception as e:
        print(f"\n[ERROR] Ocurrió un error al leer el archivo: {e}")
        return {"status": "Error", "message": str(e)}

    # --- Generar Resumen de Resultados ---
    results = {
        "status": "Success",
        "total_lines_processed": line_number,
        "failed_login_summary": dict(failed_login_attempts)
    }
    
    print("\n=========================================")
    print("         RESUMEN DEL ANÁLISIS")
    print("=========================================")
    print(f"Total de líneas procesadas: {results['total_lines_processed']}")
    print("--- Intentos Fallidos por Usuario ---")
    
    # Ordenar los resultados para mostrar primero a quienes más fallaron
    sorted_attempts = sorted(failed_login_attempts.items(), key=lambda item: item[1], reverse=True)

    if not sorted_attempts:
        print("No se detectaron intentos de inicio de sesión fallidos.")
    else:
        for username, count in sorted_attempts:
            # Aquí podemos añadir lógica adicional, por ejemplo, alertar si > 3 intentos
            alert = "🚨 ¡ALERTA!" if count >= 3 else ""
            print(f"  {username:<15}: {count} veces ({alert})")

    return results

if __name__ == "__main__":
    # --- EJEMPLO DE USO ---
    LOG_FILE = "application.log" 
    
    print("=========================================")
    print(f"Ejecutando Analizador de Logs sobre '{LOG_FILE}'...")
    print("=========================================\n")

    analysis_results = analyze_logs(LOG_FILE)
    
    # Opcional: Imprimir el diccionario completo de resultados
    import pprint
    print("\n--- Resultados completos (Diccionario) ---")
    pprint.pprint(analysis_results)