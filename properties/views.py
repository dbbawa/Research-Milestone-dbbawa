from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Unit
from .forms import PropertyForm, UnitForm


@login_required
def property_list(request):
    properties = Property.objects.all()
    context = {'properties': properties, 'total_units': Unit.objects.count()}
    return render(request, 'properties/property_list.html', context)


@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/add_property.html', {'form': form})


@login_required
def property_detail(request, pk):
    prop = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.property = prop
            unit.save()
            return redirect('property_detail', pk=prop.pk)
    else:
        form = UnitForm()
    return render(request, 'properties/property_detail.html',
                  {'prop': prop, 'units': prop.units.all(), 'form': form})

@login_required
def edit_property(request, pk):
    prop = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=prop)
        if form.is_valid():
            form.save()
            return redirect('property_detail', pk=prop.pk)
    else:
        form = PropertyForm(instance=prop)
    return render(request, 'properties/add_property.html',
                  {'form': form, 'title': 'Edit Property'})


@login_required
def delete_property(request, pk):
    prop = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        prop.delete()
    return redirect('property_list')