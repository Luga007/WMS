from django.shortcuts import render, redirect, get_object_or_404
from .forms import InventoryForm
from .models import Inventory


def inventory_view(request):
    inventory = Inventory.objects.all()
    ctx = {'inventories': inventory}
    return render(request, 'inventory.html', ctx)


def create_inventory(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('inventory_i')
    else:
        form = InventoryForm()
    ctx = {
        'form': form,
    }
    return render(request, 'createInventory.html', ctx)




def update_inventory(request, pk):
    product = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=product)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('inventory_i')
    else:
        form = InventoryForm(instance=product)

    ctx = {
        'form': form,
    }
    return render(request, 'updateInventory.html', ctx)


def delete_inventory(request, pk):
    product = get_object_or_404(Inventory, pk=pk)
    product.delete()
    return redirect('inventory_i')