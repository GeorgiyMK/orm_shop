from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from main.models import Car, Sale

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def home_view(request):
    template_name = 'main/home.html'
    pages = {

        'Показать список автомобилей доступных для покупки': reverse('list'),
        'Показать статистику продаж': reverse('all_sales'),

    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

# Для доступа к информации о полной статистике по продажам требуем логин и пароль админа
@login_required
def all_sales_view(request):
    if not request.user.is_staff:
        raise PermissionDenied()
    sales = Sale.objects.select_related('car', 'client').all()
    return render(request, 'main/sales.html', {'sales': sales})

def cars_list_view(request):
    cars = Car.objects.all() # получаем список авто
    template_name = 'main/list.html'
    context = {'cars': cars}
    return render(request, template_name, context)



def car_details_view(request, car_id):
    car = get_object_or_404(Car, id = car_id)# получите авто, если же его нет, выбросьте ошибку 404
    template_name = 'main/details.html'
    context = {'car': car}
    return render(request, template_name, context)


def sales_by_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    sales = Sale.objects.filter(car=car)
    template_name = 'main/sales.html'
    context = {
        'car': car,
        'sales': sales
    }
    return render(request, template_name, context)
