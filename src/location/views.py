from django.shortcuts import render, redirect, get_object_or_404
from .models import Location
from .forms import LocationForm

def location_view(request):
    location = Location.objects.all()
    ctx = {'locations': location}
    return render(request, 'location.html', ctx)


def create_location(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('location_v')
    else:
        form = LocationForm()
    ctx = {
        'form': form,
    }
    return render(request, 'createLocation.html', ctx)




def update_location(request, pk):
    product = get_object_or_404(Location, pk=pk)
    if request.method == "POST":
        form = LocationForm(request.POST, instance=product)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('location_v')
    else:
        form = LocationForm(instance=product)

    ctx = {
        'form': form,
    }
    return render(request, 'updateLocation.html', ctx)


def delete_location(request, pk):
    product = get_object_or_404(Location, pk=pk)
    product.delete()
    return redirect('location_v')