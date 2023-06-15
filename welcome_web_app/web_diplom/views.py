from django.shortcuts import render
from .models import Phone, Tarifs


def index(request):
    phones = Phone.objects.all()
    tarifs = Tarifs.objects.all()
    context = {'phones': phones,
               'tarifs': tarifs,}
    return render(request, 'web_diplom/index.html', context)

def basket(request):
    return render(request, 'web_diplom/basket.html', {'title': 'Корзина'})