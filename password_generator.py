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


def menu():
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


# Este bloque se ejecuta solo cuando el script se corre directamente (no cuando se importa como módulo).
if __name__ == "__main__":
    # Inicia un bucle infinito para permitir al usuario generar múltiples contraseñas.
    while True:
        # Llama a la función 'menu' para mostrar las opciones y obtener la entrada del usuario.
        menu()
        # Imprime una línea en blanco para mejorar la legibilidad entre interacciones.
        print("\n")
        # Pregunta al usuario si desea generar otra contraseña.
        continuar = input("¿Quieres generar otra? (s/n): ").lower()
        # Comprueba si la respuesta del usuario NO es 's'.
        if continuar != 's':
            # Si la respuesta no es 's', imprime un mensaje de despedida.
            print("¡Adiós!")
            # Rompe el bucle 'while True', terminando así la ejecución del script.
            break