from django.shortcuts import render
from django.http import HttpResponse
from .models import Mems
import random

def MemsListView(request):
    if request.method == 'POST':
        random_item = random.choice(Mems.objects.all())
        return render(request, 'slaider/mem_list.html', {'random_item': random_item})
    else:
        return render(request, 'slaider/mem_list.html')

