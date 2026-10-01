# Importa los módulos necesarios para el análisis de URLs.
import re
from urllib.parse import urlparse

def analizar_url(url):
    """
    Analiza una URL y busca características que puedan indicar que es sospechosa.

    Args:
        url (str): La cadena de texto que representa la URL a analizar.

    Returns:
        dict: Un diccionario con los hallazgos del análisis, donde cada clave es un requisito/característica 
              y el valor es True si se cumple o False si no.
    """
    print(f"\n--- Analizando URL: {url} ---")
    
    # Inicializa el diccionario de resultados con valores por defecto (False)
    resultados = {}

    # 1. Validación básica y longitud
    if not isinstance(url, str) or not url.strip():
        return {"URL válida": False, "Longitud adecuada": False}
    
    resultados["URL válida"] = True
    
    # Limpia la URL de espacios en blanco al inicio/final
    url_limpia = url.strip()

    # 2. Longitud (Ejemplo: entre 15 y 100 caracteres)
    longitud = len(url_limpia)
    resultados["Longitud adecuada"] = 15 <= longitud <= 100

    # 3. Descomposición de la URL usando urlparse
    try:
        parsed_url = urlparse(url_limpia)
        resultados["Es una URL bien formada"] = bool(parsed_url.scheme and parsed_url.netloc)
        
        # Si no tiene esquema (http/https), se considera menos fiable o incompleta
        if not parsed_url.scheme:
            resultados["Tiene un esquema (http/https)"] = False
        else:
            resultados["Tiene un esquema (http/https)"] = True

    except Exception as e:
        print(f"Advertencia: Error al parsear la URL: {e}")
        resultados["Es una URL bien formada"] = False


    # 4. Búsqueda de patrones sospechosos con Expresiones Regulares (Regex)
    
    # Patrón para IPs (IPv4 simple): cuatro grupos de números separados por puntos (ej: 192.168.1.1)
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    resultados["Contiene una dirección IP"] = bool(re.search(ip_pattern, url_limpia))

    # Patrón para subdominios excesivos (ej: a.b.c.d.com) - más de 2 puntos en el dominio principal
    dot_count = url_limpia.count('.')
    resultados["Exceso de subdominios"] = dot_count > 3

    # Patrón para caracteres codificados inusuales (ej: %20, %2F, etc.) - busca dos letras seguidas de un número
    encoding_pattern = r'%\d{2}'
    resultados["Contiene codificación URL (%XX)"] = bool(re.search(encoding_pattern, url_limpia))

    # 5. Búsqueda de palabras clave peligrosas (Strings)
    keywords = [
        "login", "admin", "secure", "update", "bitcache", "download", 
        "crack", "freefile", "suspicious", "malware", "phishing"
    ]
    resultados["Contiene keywords sospechosas"] = False
    for keyword in keywords:
        # Busca la palabra clave, ignorando mayúsculas/minúsculas (re.IGNORECASE)
        if re.search(r'\b' + re.escape(keyword) + r'\b', url_limpia, re.IGNORECASE):
            resultados["Contiene keywords sospechosas"] = True
            break

    # 6. Análisis del dominio/netloc (si está disponible)
    if parsed_url.netloc:
        domain = parsed_url.netloc
        
        # Comprobar si el dominio es muy corto o genérico
        resultados["Dominio demasiado corto"] = len(domain) < 5
        
        # Comprobar si contiene guiones excesivos (ej: -very-long-name-site-)
        hyphen_count = domain.count('-')
        if hyphen_count > 3 and len(domain) > 15:
            resultados["Exceso de guiones en dominio"] = True
        else:
            resultados["Exceso de guiones en dominio"] = False

    return resultados


def mostrar_resultado(url, resultados):
    """Imprime los hallazgos del análisis de forma legible."""
    print("\n=========================================")
    print("           RESUMEN DEL ANÁLISIS")
    print("=========================================")
    
    cumplidos = 0
    total_checks = len(resultados)
    
    for requisito, cumple in resultados.items():
        estado = "✅ CUMPLE" if cumple else "❌ NO CUMPLE"
        print(f"{requisito:<35}: {estado}")
        if cumple:
            cumplidos += 1

    # Conclusión general
    porcentaje = (cumplidos / total_checks) * 100
    print("-----------------------------------------")
    print(f"Porcentaje de características positivas: {porcentaje:.2f}%")
    
    if porcentaje >= 85 and resultados.get("Contiene keywords sospechosas", False):
        print("🚨 Veredicto General: MUY SOSPECHOSO (Alto riesgo)")
    elif porcentaje >= 70:
        print("⚠️ Veredicto General: POSIBLEMENTE SOSPECHOSO (Revisar detalles)")
    else:
        print("🟢 Veredicto General: SEGURO/NORMAL (Bajo riesgo)")
    print("=========================================")


def menu_url_detector():
    """Muestra el menú interactivo para la herramienta de detección de URLs."""
    while True:
        print("\n\n--- 🌐 DETECTOR DE URL SOSPECHOSAS 🌐 ---")
        print("1. Analizar una URL (Modo Interactivo)")
        print("2. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            url_input = input("Introduce la URL que deseas analizar: ")
            if url_input.strip():
                # Ejecuta el análisis
                resultados = analizar_url(url_input)
                # Muestra los resultados
                mostrar_resultado(url_input, resultados)
            else:
                print("Por favor, introduce una URL válida.")
        elif opcion == "2":
            print("\nSaliendo del Detector de URLs. ¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona 1 o 2.")


if __name__ == "__main__":
    menu_url_detector()

# Fin de url_detector.py