import base64
from io import BytesIO

from django.shortcuts import render
from order.models import Order
from store.models import Employees
from product.models import Product, Supplier
from matplotlib import pyplot as plt
from inventory.models import Inventory



def main(request):
    total_orders = Order.objects.count()
    total_employees = Employees.objects.count()
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()

    products = Product.objects.all()
    supplier_counts = {}

    for product in products:
        supplier_name = product.supplier.first_name
        supplier_counts[supplier_name] = supplier_counts.get(supplier_name, 0) + 1

    labels = list(supplier_counts.keys())
    sizes = list(supplier_counts.values())

    fig, ax = plt.subplots()
    ax.bar(labels, sizes, color='orange')
    ax.set_ylabel('Количество товаров')
    ax.set_xlabel('Поставщик')
    ax.set_title('Товары по поставщикам')
    plt.xticks(rotation=45, ha='right')

    buffer = BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graphic = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    positions = Employees.objects.values_list('position', flat=True)
    position_counts = {}
    for pos in positions:
        position_counts[pos] = position_counts.get(pos, 0) + 1

    labels = list(position_counts.keys())
    sizes = list(position_counts.values())

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graphic2 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    inventory_items = Inventory.objects.all()

    labels = [item.description for item in inventory_items]
    quantities = [item.quantity for item in inventory_items]

    fig, ax = plt.subplots()
    ax.bar(labels, quantities, color='skyblue')
    ax.set_ylabel('Количество')
    ax.set_xlabel('Описание товара')
    ax.set_title('Товары на складе')
    plt.xticks(rotation=45, ha='right')

    buffer = BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graphic3 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    ctx = {
        'total_orders': total_orders,
        'total_employees': total_employees,
        'total_product': total_product,
        'total_supplier': total_supplier,
        'chart': graphic,
        'chart2': graphic2,
        'chart3': graphic3
    }
    return render(request, 'base.html', ctx)