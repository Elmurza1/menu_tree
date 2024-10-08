from django.shortcuts import render
from .models import MenuItem

from django.shortcuts import render
from .models import MenuItem


def menu_view(request):
    menu_items = MenuItem.objects.filter(parent__isnull=True).prefetch_related('children')
    return render(request, 'menu.html', {
        'menu_items': menu_items,
    })

