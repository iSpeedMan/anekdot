from django.shortcuts import render
from django.http import HttpResponse
from .models import Common
import random

def CommonListView(request):
    if request.method == 'POST':
        random_item = random.choice(Common.objects.all())
        return render(request, 'common/recepts_list.html', {'random_item': random_item})
    else:
        return render(request, 'common/recepts_list.html')

