# reports.py
"""
Módulo de reportes: generación de reportes a partir del inventario y del historial de ventas.
"""

from utils import print_error


def top_3_products(inventory):
    """
    Mostrar el top 3 de productos más vendidos.

    - Usa una función lambda para ordenar la lista de productos
      por el campo 'total_sold' de forma descendente.
    - Solo se consideran productos con total_sold > 0.
    """
    print("\n=== Top 3 Best-Selling Products ===")

    if not inventory:
        print_error("Inventory is empty.")
        return

    # Ordenar productos por 'total_sold' usando una lambda (requisito de lambda)
    sorted_products = sorted(
        inventory,
        key=lambda p: p["total_sold"],
        reverse=True,
    )

    # Filtrar productos que se han vendido
    sold_products = [p for p in sorted_products if p["total_sold"] > 0]

    if not sold_products:
        print("No products have been sold yet.\n")
        return

    # Tomar los tres primeros
    top_3 = sold_products[:3]

    for idx, product in enumerate(top_3, start=1):
        print(
            f"{idx}. {product['title']} | Author: {product['author']} | "
            f"Sold: {product['total_sold']} units"
        )
    print("")


def sales_by_author(sales_history):
    """
    Mostrar las ventas agrupadas por autor.

    Para cada autor:
    - Total de unidades vendidas.
    - Total de ingresos netos.

    Implementación:
    - Recorre la lista de ventas.
    - Usa un diccionario auxiliar 'author_stats' con:
      clave: nombre del autor
      valor: diccionario con 'total_quantity' y 'total_net'.
    """
    print("\n=== Sales by Author ===")

    if not sales_history:
        print("No sales registered yet.\n")
        return

    author_stats = {}

    for sale in sales_history:
        author = sale["author"]
        if author not in author_stats:
            author_stats[author] = {
                "total_quantity": 0,
                "total_net": 0.0,
            }
        author_stats[author]["total_quantity"] += sale["quantity"]
        author_stats[author]["total_net"] += sale["net_amount"]

    for author, data in author_stats.items():
        print(
            f"Brand: {author} | "
            f"Total quantity sold: {data['total_quantity']} | "
            f"Total net sales: {data['total_net']:.2f}"
        )
    print("")


def income_report(sales_history):
    """
    Calcular e imprimir el ingreso bruto y neto.

    - Gross income: suma de 'gross_amount' (valor bruto) de todas las ventas.
    - Net income: suma de 'net_amount' (valor neto) de todas las ventas.
      Se usa una lambda con map (para practicar funciones lambda)
    - Total discounts: diferencia entre bruto y neto.
    """
    #Informe de ingresos
    print("\n=== Income Report ===")

    if not sales_history:
        print("There isn't sales registered yet.\n")
        return

    # Ingreso bruto: suma directa del campo 'gross_amount' (valor bruto)
    gross_income = sum(sale["gross_amount"] for sale in sales_history)

    # Ingreso neto: se usa map + lambda (otra forma funcional)
    net_income = sum(map(lambda s: s["net_amount"], sales_history))

    total_discounts = gross_income - net_income

    print(f"Total gross income: {gross_income:.2f}")
    print(f"Total discounts:    {total_discounts:.2f}")
    print(f"Total net income:   {net_income:.2f}\n")


def inventory_performance_report(inventory):
    """
    Mostrar un reporte simple del rendimiento del inventario.

    Para cada producto muestra:
    - Stock actual.
    - Total vendido.
    """
    print("\n=== Inventory Performance Report ===")

    if not inventory:
        print_error("Inventory is empty.")
        return

    for product in inventory:
        stock = product["stock"]
        sold = product["total_sold"]

        print(
            f"Product: {product['title']} | Author: {product['author']} | "
            f"Stock: {stock} | Sold: {sold} | "
        )
    print("")