from django.shortcuts import render, HttpResponse, redirect
from .models import Category, Dish,Events, Special,About, Why_us, Gallery
from .forms import UserReservationForm

# Create your views here.
def base(request):

    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/')


    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    special = Dish.objects.filter(special=True)
    about = About.objects.all()
    gallery = Gallery.objects.all()
    specials = Special.objects.all()
    reservation = UserReservationForm()
    events = Events.objects.filter(is_visible=True)
    why_us = Why_us.objects.all()

    data = {'categories': categories,
            'dishes': dishes,
            'special': special,
            'about': about,
            'gallery': gallery,
            'specials': specials,
            'reservation': reservation,
            'events': events,
            'why_us': why_us,

            }

    return render(request, 'base.html', context=data)