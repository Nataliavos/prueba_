# models.py
"""
Modelos de dominio y constantes para el sistema de inventario y ventas.
"""

from datetime import datetime

# Diccionario con los tipos de cliente y su descuento asociado (en forma decimal)
# regular -> 0%, vip -> 10%, wholesale -> 15%
CUSTOMER_DISCOUNTS = {
    "regular": 0.0,
    "vip": 0.10,
    "wholesale": 0.15,
}


def create_initial_inventory():
    """
    Crear el inventario inicial con 5 productos precargados.

    Cada producto es un diccionario con:
    - id: identificador único del producto
    - title: título del libro
    - author: autor
    - category: categoría
    - unit_price: precio unitario
    - stock: cantidad en inventario
    - total_sold: cantidad total vendida (para reportes)
    """
    return [
        {
            "id": 1,
            "title": "One Hundred Years of Solitude",
            "author": "Gabriel García Márquez",
            "category": "novel",
            "unit_price": 95000.0,
            "stock": 20,
            "total_sold": 0,
        },
        {
            "id": 2,
            "title": "The Little Prince",
            "author": "Antoine de Saint-Exupéry",
            "category": "novel",
            "unit_price": 35000.0,
            "stock": 10,
            "total_sold": 0,
        },
        {
            "id": 3,
            "title": "The Lord of the Rings: The Fellowship of the Ring",
            "author": "J.R. Tolkien",
            "category": "fantasy",
            "unit_price": 80000.0,
            "stock": 30,
            "total_sold": 0,
        },
        {
            "id": 4,
            "title": "Harry Potter and the Philosopher's Stone\"",
            "author": "J.K. Rowling",
            "category": "fantasy",
            "unit_price": 65000.0,
            "stock": 8,
            "total_sold": 0,
        },
        {
            "id": 5,
            "title": "Eleven minutes",
            "author": "Paulo Cohelo",
            "category": "novel",
            "unit_price": 35000.0,
            "stock": 10,
            "total_sold": 0,
        },
    ]


def create_sale_record(
    sale_id,
    customer_name,
    customer_type,
    product,
    quantity,
    discount_rate,
):
    """
    Crear y devolver una venta (diccionario).

    Parámetros:
    - sale_id: ID de la venta
    - customer_name: nombre del cliente
    - customer_type: tipo de cliente (regular, vip, wholesale)
    - product: diccionario de producto tomado del inventario
    - quantity: cantidad vendida
    - discount_rate: tasa de descuento en forma decimal (0.10 = 10%)

    Cálculos:
    - gross_amount: total bruto (precio * cantidad)
    - discount_amount: valor del descuento aplicado
    - net_amount: total neto después del descuento
    """
    unit_price = product["unit_price"]
    gross_amount = unit_price * quantity
    discount_amount = gross_amount * discount_rate
    net_amount = gross_amount - discount_amount

    return {
        "id": sale_id,
        "customer_name": customer_name,
        "customer_type": customer_type,
        "product_id": product["id"],
        "product_title": product["title"],
        "author": product["author"],
        "quantity": quantity,
        "unit_price": unit_price,
        "discount_rate": discount_rate,
        "discount_amount": discount_amount,
        "gross_amount": gross_amount,
        "net_amount": net_amount,
        # Fecha y hora actual como string legible
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }