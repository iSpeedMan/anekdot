from django.shortcuts import render
from django.http import HttpResponse
from .models import Anekdot
import random

def AnekdotListView(request):
    if request.method == 'POST':
        random_item = random.choice(Anekdot.objects.all())
        return render(request, 'common/anekdot_list.html', {'random_item': random_item})
    else:
        return render(request, 'common/anekdot_list.html')

