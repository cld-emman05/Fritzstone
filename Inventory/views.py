from django.shortcuts import render
from django.http import HttpResponse
from .models import Inventory
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

# Create your views here.
def index(request):

    product = Inventory.objects.all()[:3]

    context = {
        'title': 'Inventory',
        'products': product
    }

    return render(request, 'inventory/index.html', context)
