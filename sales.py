# sales.py
"""
Módulo de ventas: registrar y consultar ventas, validar stock
y actualizar el inventario automáticamente.
"""

from models import CUSTOMER_DISCOUNTS, create_sale_record
from utils import (
    input_non_empty_string,
    input_int,
    print_error,
    print_success,
)
from inventory import list_products, find_product_by_id


def choose_customer_type():
    """
    Elegir el tipo de cliente.

    Muestra un pequeño menú:
    1. Regular
    2. VIP
    3. Wholesale (mayorista)

    Devuelve:
    - customer_type: cadena ('regular', 'vip', 'wholesale')
    - discount_rate: valor decimal del descuento según la constante CUSTOMER_DISCOUNTS.
    """
    print("\nCustomer types:")
    print("1. Regular (0% discount)")
    print("2. VIP (10% discount)")
    print("3. Wholesale (15% discount)")

    while True:
        option = input_int("Choose customer type (1-3): ")
        if option == 1:
            return "regular", CUSTOMER_DISCOUNTS["regular"]
        elif option == 2:
            return "vip", CUSTOMER_DISCOUNTS["vip"]
        elif option == 3:
            return "wholesale", CUSTOMER_DISCOUNTS["wholesale"]
        else:
            print_error("Invalid option. Please choose 1, 2, or 3.")


def get_next_sale_id(sales_history):
    """
    Obtener el siguiente ID para una venta.

    - Si no hay ventas, devuelve 1.
    - Si ya hay, toma el máximo id y suma 1.
    """
    if not sales_history:
        return 1
    max_id = max(sale["id"] for sale in sales_history)
    return max_id + 1


def register_sale(inventory, sales_history):
    """
    Registrar una nueva venta.

    Tareas principales:
    - Pedir nombre del cliente.
    - Permitir elegir tipo de cliente (y por tanto descuento).
    - Mostrar productos disponibles.
    - Validar que el producto exista y que tenga stock suficiente.
    - Pedir cantidad.
    - Crear el registro de venta (create_sale_record).
    - Actualizar el inventario:
      - reducir stock
      - aumentar total_sold
    - Agregar la venta al historial.
    """
    print("\n=== Register New Sale ===")

    if not inventory:
        print_error("There aren't products in inventory.")
        return

    # Se pide el nombre del cliente
    customer_name = input_non_empty_string("Customer name: ")

    # Se elige el tipo de cliente y se obtiene el descuento asociado
    customer_type, discount_rate = choose_customer_type()

    # Mostrar productos para que se seleccione uno
    list_products(inventory)

    product_id = input_int("Enter product ID to sell: ", min_value=1)
    product = find_product_by_id(inventory, product_id)

    if not product:
        print_error("Product not found.")
        return

    # Validar que haya stock disponible
    if product["stock"] <= 0:
        print_error("This product has no stock available.")
        return

    quantity = input_int("Quantity to sell: ", min_value=1)

    # Validar que la cantidad pedida no sea mayor que el stock disponible
    if quantity > product["stock"]:
        print_error(
            f"Not enough stock. Available: {product['stock']}, "
            f"Requested: {quantity}"
        )
        return

    # Generar ID de venta
    sale_id = get_next_sale_id(sales_history)

    # Crear el registro de venta con el modelo
    sale = create_sale_record(
        sale_id=sale_id,
        customer_name=customer_name,
        customer_type=customer_type,
        product=product,
        quantity=quantity,
        discount_rate=discount_rate,
    )

    # Actualizar inventario:
    # - reducir stock
    # - aumentar total_sold (para reportes)
    product["stock"] -= quantity
    product["total_sold"] += quantity

    # Guardar la venta en el historial
    sales_history.append(sale)

    print_success("Sale registered successfully.")
    # Mostrar resumen corto de la venta
    print(
        f"Sale ID: {sale['id']} | Customer: {sale['customer_name']} | "
        f"Product: {sale['product_title']} | Quantity: {sale['quantity']} | "
        f"Gross: {sale['gross_amount']:.2f} | "
        f"Discount: {sale['discount_amount']:.2f} | "
        f"Net: {sale['net_amount']:.2f} | "
        f"Date: {sale['date']} | "
    )


def show_sales_history(sales_history):
    """
    Mostrar historial de ventas.

    Si no hay ventas, muestra un mensaje.
    Cada venta muestra información de cliente, producto, autor, cantidades y montos (valor bruto, descuento y valor neto).
    """
    print("\n=== Sales History ===")

    if not sales_history:
        print("No sales registered yet.\n")
        return

    for sale in sales_history:
        print(
            f"ID: {sale['id']} | Date: {sale['date']} | "
            f"Customer: {sale['customer_name']} ({sale['customer_type']}) | "
            f"Product: {sale['product_title']} | Author: {sale['author']} | "
            f"Quantity: {sale['quantity']} | "
            f"Gross: {sale['gross_amount']:.2f} | "
            f"Discount: {sale['discount_amount']:.2f} | "
            f"Net: {sale['net_amount']:.2f} | "
            f"Date: {sale['date']} | "

        )
    print("")