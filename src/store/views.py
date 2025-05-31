from django.shortcuts import render, redirect, get_object_or_404
from . models import Store, Employees
from .forms import StoreForm, EmployeesForm

def store(request):
    store = Store.objects.all()
    ctx = {
        'stores': store,
    }

    return render(request, 'store.html', ctx)


def create_store(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = StoreForm()

    ctx = {
        'form': form,
    }
    return render(request, 'createStore.html', ctx)




def update_store(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == "POST":
        form = StoreForm(request.POST, instance=store)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = StoreForm(instance=store)

    ctx = {
        'form': form,
    }
    return render(request, 'updateStore.html', ctx)


def delete_store(request, pk):
    store = get_object_or_404(Store, pk=pk)
    store.delete()
    return redirect('store')


def employees(request):
    employee = Employees.objects.all()


    ctx = {
        'employees': employee
    }
    return render(request, 'employee.html', ctx)


def create_employee(request):
    if request.method == "POST":
        form = EmployeesForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = EmployeesForm()
    ctx = {
        'form': form,
    }
    return render(request, 'createEmployee.html', ctx)



def update_employee(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    if request.method == "POST":
        form = EmployeesForm(request.POST, instance=employee)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = EmployeesForm(instance=employee)

    ctx = {
        'form': form,
    }
    return render(request, 'updateEmployee.html', ctx)


def delete_employee(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    employee.delete()
    return redirect('employees')


