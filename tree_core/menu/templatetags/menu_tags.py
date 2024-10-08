from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu_item.html', takes_context=True)
def render_menu(context, parent=None):
    if parent is None:

        menu_items = MenuItem.objects.filter(parent__isnull=True)  # Получаем корневые элементы
        print(menu_items)  # Выводим их

    else:
        menu_items = parent.children.all()
    return {
        'menu_items': menu_items,
        'request': context['request'],
    }


