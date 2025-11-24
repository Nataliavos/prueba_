# utils.py
"""
Funciones utilitarias para validación de entradas y ayuda de interfaz.
"""


def input_non_empty_string(prompt):
    """
    Validar que la cadena no esté vacía
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input can't be empty. Please try again.")


def input_int(prompt, min_value=None):
    """
    Pedir al usuario un número entero.

    - prompt: mensaje que se muestra al usuario.
    - min_value: si se especifica, el valor debe ser >= min_value.

    Validar que se ingrese un entero válido.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def input_float(prompt, min_value=None):
    """
    Pedir al usuario un número flotante.

    - prompt: mensaje que se muestra al usuario.
    - min_value: si se especifica, el valor debe ser >= min_value.

    Manejar errores de conversión.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def print_error(message):
    """
    Imprimir un mensaje de error con formato.
    """
    print(f"\n[ERROR] {message}\n")


def print_success(message):
    """
    Imprimir un mensaje de éxito con formato.
    """
    print(f"\n[SUCCESS] {message}\n")


def pause():
    """
    Pausar la ejecución para que el usuario pueda leer la información.
    Espera que el usuario presione ENTER.
    """
    input("Press ENTER to continue...")