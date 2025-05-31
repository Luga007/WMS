from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier, Product
from .forms import SupplierForm, ProductForm


def supplier_view(request):
    suppliers = Supplier.objects.all()
    ctx = {'suppliers': suppliers}
    return render(request, 'supply.html', ctx)


def create_supplier(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('supplier')
    else:
        form = SupplierForm()
    ctx = {
        'form': form,
    }
    return render(request, 'createSupplier.html', ctx)



def update_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('supplier')
    else:
        form = SupplierForm(instance=supplier)

    ctx = {
        'form': form,
    }
    return render(request, 'updateSupplier.html', ctx)


def delete_supplier(request, pk):
    employee = get_object_or_404(Supplier, pk=pk)
    employee.delete()
    return redirect('supplier')





def product_view(request):
    product = Product.objects.all()
    ctx = {'products': product}
    return render(request, 'product.html', ctx)


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm()
    ctx = {
        'form': form,
    }
    return render(request, 'createProduct.html', ctx)




def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm(instance=product)

    ctx = {
        'form': form,
    }
    return render(request, 'updateProduct.html', ctx)


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product')