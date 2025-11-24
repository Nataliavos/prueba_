# main.py
"""
Módulo principal: menú de consola para el sistema de
gestión de inventario y ventas.

"""

from models import create_initial_inventory
from utils import input_int, pause
from inventory import list_products, add_product, update_product, delete_product
from sales import register_sale, show_sales_history
from reports import (
    top_3_products,
    sales_by_author,
    income_report,
    inventory_performance_report,
)


def show_main_menu():
    """
    Mostrar el menú principal.

    Este menú se muestra en cada iteración del bucle principal.
    """
    print("=========================================")
    print("  Inventory and Sales Management System  ")
    print("=========================================")
    print("1. List products")
    print("2. Add product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Register sale")
    print("6. Show sales history")
    print("7. Reports")
    print("0. Exit")
    print("=========================================")


def show_reports_menu():
    """
    Mostrar el submenú de reportes.

    Desde aquí se accede a:
    - Top 3 productos más vendidos
    - Ventas por autor
    - Ingresos brutos y netos
    - Rendimiento del inventario
    """
    print("\n========== Reports Menu ==========")
    print("1. Top 3 best-selling products")
    print("2. Sales by author")
    print("3. Income report (gross and net)")
    print("4. Inventory performance")
    print("0. Back to main menu")
    print("==================================")


def handle_reports_menu(inventory, sales_history):
    """
    Manejar la lógica del submenú de reportes.

    Parámetros:
    - inventory: lista de productos
    - sales_history: lista de ventas

    Esta función se mantiene en un bucle hasta que el usuario
    elige la opción 0 para volver al menú principal.
    """
    while True:
        show_reports_menu()
        choice = input_int("Choose an option: ")

        if choice == 1:
            top_3_products(inventory)
            pause()
        elif choice == 2:
            sales_by_author(sales_history)
            pause()
        elif choice == 3:
            income_report(sales_history)
            pause()
        elif choice == 4:
            inventory_performance_report(inventory)
            pause()
        elif choice == 0:
            # Salir del submenú de reportes y volver al menú principal
            break
        else:
            print("Invalid option. Please try again.\n")


def main():
    """
    Punto de entrada de la aplicación.

    Responsabilidades:
    - Crear el inventario inicial con 5 productos.
    - Crear la lista vacía de historial de ventas.
    - Controlar el bucle principal del menú.
    - Manejar algunas excepciones para que el programa no se cierre de forma abrupta.
    """
    # Inventario inicial precargado
    inventory = create_initial_inventory()
    # Historial de ventas inicialmente vacío
    sales_history = []

    # Bucle principal del programa
    while True:
        try:
            show_main_menu()
            choice = input_int("Choose an option: ")

            if choice == 1:
                list_products(inventory)
                pause()
            elif choice == 2:
                add_product(inventory)
                pause()
            elif choice == 3:
                update_product(inventory)
                pause()
            elif choice == 4:
                delete_product(inventory)
                pause()
            elif choice == 5:
                register_sale(inventory, sales_history)
                pause()
            elif choice == 6:
                show_sales_history(sales_history)
                pause()
            elif choice == 7:
                handle_reports_menu(inventory, sales_history)
            elif choice == 0:
                print("\nExiting the program. Goodbye!\n")
                break
            else:
                print("\nInvalid option. Please try again.\n")

        # Manejo de Ctrl + C para evitar cierre feo
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Use option 0 to exit.\n")
        # Manejo genérico de errores inesperados
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            print("The program will continue.\n")


if __name__ == "__main__":
    main()