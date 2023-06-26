from django.shortcuts import render
from .models import Phone, Tarifs, Rewiev, User


def index(request):
    phones = Phone.objects.all()
    tarifs = Tarifs.objects.all()
    context = {'phones': phones,
               'tarifs': tarifs,}
    if request.method == 'POST':
        rewiev = request.POST.get('review', None)
        name = request.POST.get('userName', None)
        new_rewiev = Rewiev.objects.create(name=name, review=rewiev)
        new_rewiev.save()
    return render(request, 'web_diplom/index.html', context)

def basket(request):
    context = {'carts': 'члены',}
    return render(request, 'web_diplom/basket.html', context=context)

def rewievs(request):
    reviews = Rewiev.objects.all()
    context = {'reviews': reviews,}
    return render(request, 'web_diplom/reviews.html', context=context)