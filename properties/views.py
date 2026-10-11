from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Property, Unit


@login_required
def property_list(request):
    properties = Property.objects.all()
    context = {'properties': properties, 'total_units': Unit.objects.count()}
    return render(request, 'properties/property_list.html', context)