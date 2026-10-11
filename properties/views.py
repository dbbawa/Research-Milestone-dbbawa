from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Property, Unit
from .forms import PropertyForm


@login_required
def property_list(request):
    properties = Property.objects.all()
    context = {'properties': properties, 'total_units': Unit.objects.count()}
    return render(request, 'properties/property_list.html', context)


@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/add_property.html', {'form': form})