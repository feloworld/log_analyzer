# Importa el módulo 'random' para generar números y secuencias aleatorias.
import random
# Importa el módulo 'string' que contiene colecciones útiles de caracteres (letras, dígitos, etc.).
import string


def generar_contrasena(longitud, mayusculas=True, minusculas=True, numeros=True, simbolos=True):

    """Genera una contraseña aleatoria basada en los parámetros proporcionados.


    Args:
        longitud (int): La longitud deseada para la contraseña.
        mayusculas (bool): Incluir letras mayúsculas (por defecto True).
        minusculas (bool): Incluir letras minúsculas (por defecto True).
        numeros (bool): Incluir dígitos (por defecto True).
        simbolos (bool): Incluir símbolos de puntuación (por defecto True).

    Returns:
        str: La contraseña generada o un mensaje de error si no se seleccionó ningún tipo de carácter.
    """
    
    # Inicializa una cadena vacía que contendrá todos los caracteres permitidos para la contraseña.
    caracteres = ""
    # Si el usuario quiere mayúsculas, añade todas las letras mayúsculas disponibles (A-Z) al conjunto de caracteres.
    if mayusculas:
        caracteres += string.ascii_uppercase
    # Si el usuario quiere minúsculas, añade todas las letras minúsculas disponibles (a-z).
    if minusculas:
        caracteres += string.ascii_lowercase
    # Si el usuario quiere números, añade todos los dígitos disponibles (0-9).
    if numeros:
        caracteres += string.digits
    # Si el usuario quiere símbolos, añade todos los caracteres de puntuación comunes (como !, @, #, etc.).
    if simbolos:
        caracteres += string.punctuation


    # Comprueba si la cadena 'caracteres' está vacía. Esto sucede si el usuario no seleccionó ningún tipo de carácter.
    if not caracteres:
        # Si no hay caracteres disponibles, devuelve un mensaje de error.
        return "Error: Debes seleccionar al menos un tipo de carácter."



    # Genera la contraseña seleccionando caracteres aleatoriamente de la cadena 'caracteres'.
    # 'random.choice(caracteres)' elige un carácter al azar.
    # 'for _ in range(longitud)' repite esta elección tantas veces como la 'longitud' especificada.
    # '"".join(...)' une todos los caracteres seleccionados en una única cadena de texto.
    password = "".join(random.choice(caracteres) for _ in range(longitud))
    
    # Devuelve la contraseña generada.
    return password


def menu_generador():
    """Muestra el menú interactivo para generar contraseñas y maneja la entrada del usuario."""
    
    # Imprime un título decorativo para la herramienta.
    print("--- 🔐 GENERADOR DE CONTRASEÑAS 🔐 ---")

    # Utiliza un bloque try-except para manejar posibles errores si el usuario introduce datos no válidos.
    try:

        # Solicita al usuario que introduzca la longitud deseada para la contraseña.
        # También le ofrece la opción de escribir 'salir' para terminar el programa.
        longitud_input = input("Introduce la longitud de la contraseña (o escribe \'salir\' para terminar): ")
        
        # Convierte la entrada del usuario a minúsculas y comprueba si es igual a 'salir'.
        if longitud_input.lower() == 'salir':
            # Si el usuario escribió 'salir', la función 'menu' retorna, lo que eventualmente terminará el programa.
            return

        # Intenta convertir la entrada del usuario (que es una cadena) a un número entero.
        longitud = int(longitud_input)
        
        # Validación: Comprueba si la longitud introducida es menor o igual a cero.
        if longitud <= 0:
            # Si la longitud no es válida, muestra un mensaje de error.
            print("La longitud debe ser mayor a 0.")
            # Sale de la función 'menu'.
            return

        # Informa al usuario sobre los siguientes pasos: seleccionar tipos de caracteres.
        print("\nSelecciona qué caracteres incluir (s/n):")
        
        # Pregunta al usuario si desea incluir letras mayúsculas. Convierte la respuesta a minúsculas y compara con 's'.
        # El resultado (True o False) se guarda en 'usar_mayus'.
        usar_mayus = input("¿Incluir MAYÚSCULAS? (s/n) ").lower() == 's'
        # Pregunta lo mismo para las letras minúsculas.
        usar_min = input("¿Incluir minúsculas? (s/n) ").lower() == 's'
        # Pregunta lo mismo para los números.
        usar_num = input("¿Incluir números? (s/n) ").lower() == 's'
        # Pregunta lo mismo para los símbolos.
        usar_sim = input("¿Incluir símbolos? (s/n) ").lower() == 's'

        # Llama a la función 'generar_contrasena' con la longitud y las preferencias booleanas del usuario.
        resultado = generar_contrasena(longitud, usar_mayus, usar_min, usar_num, usar_sim)

        # Imprime una línea decorativa antes de mostrar la contraseña generada.
        print("\n" + "=" * 30)
        # Muestra la contraseña resultante formateada.
        print(f"Tu nueva contraseña es: {resultado}")
        # Imprime otra línea decorativa después de la contraseña.
        print("=" * 30)

    # Si ocurre un error de tipo 'ValueError' (por ejemplo, si el usuario introduce texto en lugar de un número para la longitud),
    # se ejecuta este bloque.
    except ValueError:
        # Muestra un mensaje de error indicando que la entrada no fue válida.
        print("Error: Por favor, introduce un número válido para la longitud.")


def analizar_contrasena(contrasena):
    """Devuelve los requisitos de seguridad que cumple una contraseña."""
    return {
        "Tener al menos 8 caracteres": len(contrasena) >= 8,
        "Incluir una letra mayúscula": any(caracter.isupper() for caracter in contrasena),
        "Incluir una letra minúscula": any(caracter.islower() for caracter in contrasena),
        "Incluir un número": any(caracter.isdigit() for caracter in contrasena),
        "Incluir un símbolo": any(
            not caracter.isalnum() and not caracter.isspace()
            for caracter in contrasena
        ),
    }


def menu():
    """Muestra las opciones principales de la herramienta."""
    print("--- HERRAMIENTA DE CONTRASEÑAS ---")
    print("1. Generar contraseña")
    print("2. Analizar contraseña")
    print("3. Salir")
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        menu_generador()
    elif opcion == "2":
        contrasena = input("Introduce la contraseña que deseas analizar: ")
        if not contrasena.strip():
            print("Error: La contraseña no puede estar vacía.")
            return True

        requisitos = analizar_contrasena(contrasena)
        cumplidos = sum(requisitos.values())
        print("\nResultado del análisis:")
        for requisito, cumple in requisitos.items():
            estado = "Cumple" if cumple else "No cumple"
            print(f"- {requisito}: {estado}")

        if cumplidos == len(requisitos):
            print("Nivel de seguridad: Fuerte")
            print("La contraseña cumple todos los requisitos.")
        else:
            nivel = "Mejorable" if cumplidos >= 3 else "Débil"
            print(f"Nivel de seguridad: {nivel}")
            print("Recomendaciones:")
            for requisito, cumple in requisitos.items():
                if not cumple:
                    print(f"- {requisito}.")
    elif opcion != "3":
        print("Opción no válida. Selecciona 1, 2 o 3.")

    return opcion != "3"


if __name__ == "__main__":
    while menu():
        print()
    print("¡Adiós!")