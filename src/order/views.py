from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, ItemOrders
from .forms import OrderForm, ItemOrdersForm


def order_view(request):
    order = Order.objects.all()
    ctx = {'orders': order}
    return render(request, 'order.html', ctx)


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('order')
    else:
        form = OrderForm()
    ctx = {
        'form': form,
    }
    return render(request, 'createOrder.html', ctx)




def update_order(request, pk):
    product = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=product)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('order')
    else:
        form = OrderForm(instance=product)

    ctx = {
        'form': form,
    }
    return render(request, 'updateOrder.html', ctx)


def delete_order(request, pk):
    product = get_object_or_404(Order, pk=pk)
    product.delete()
    return redirect('order')




def orderItem_view(request):
    order_item = ItemOrders.objects.all()
    ctx = {
        'order_items11': order_item
    }
    return render(request, 'orderItem.html', ctx)



def create_orderItem(request):
    if request.method == "POST":
        form = ItemOrdersForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('orderItem22')
    else:
        form = ItemOrdersForm()
    ctx = {
        'form': form,
    }
    return render(request, 'createOrderItem.html', ctx)


def update_orderItem(request, pk):
    orders_i = get_object_or_404(ItemOrders, pk=pk)
    if request.method == "POST":
        form = ItemOrdersForm(request.POST, instance=orders_i)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('orderItem22')
    else:
        form = ItemOrdersForm(instance=orders_i)

    ctx = {
        'form': form,
    }
    return render(request, 'updateOrderItem.html', ctx)


def delete_orderItem(request, pk):
    product = get_object_or_404(ItemOrders, pk=pk)
    product.delete()
    return redirect('orderItem22')