from django.shortcuts import render, redirect
from django.http import Http404
from .forms import ItemForm
from .models import Item
from django.db.models import Q, Sum
from django.contrib.auth.decorators import login_required

from datetime import date
from django.utils import timezone
import datetime

from django.contrib import auth
from django.contrib import messages
# Create your views here.


@login_required
def Home(request):
    today = date.today()

    bought = Item.objects.filter(type='-').filter(date__year=today.year, date__month=today.month, date__day=today.day
                                                                        ).filter(staff=request.user)
    sold = Item.objects.filter(type='+').filter(date__year=today.year, date__month=today.month, date__day=today.day
                                                                        ).filter(staff=request.user)
    miscellaneous = Item.objects.filter(type='--').filter(date__year=today.year, date__month=today.month, date__day=today.day
                                                                        ).filter(staff=request.user)

    # Items' Price Calculations
    boughtTotal = sum(item.value for item in bought)
    soldTotal = sum(item.value for item in sold)
    miscellaneousTotal = sum(item.value for item in miscellaneous)
    
    sumTotal = soldTotal - (boughtTotal + miscellaneousTotal)

    # For Item Entry Form
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            newitem = form.save(commit=False)
            newitem.staff = request.user
            newitem.save()

        return redirect('home')
    else:
        form = ItemForm()

    # For Date
    current_date = datetime.datetime.now()

    context = {
        'date': today,
        'bought': bought,
        'sold': sold,
        'miscellaneous': miscellaneous,
        'boughtTotal': boughtTotal,
        'soldTotal': soldTotal,
        'miscellaneousTotal': miscellaneousTotal,
        'sumTotal': sumTotal,
        'form': form,
        'current_date': current_date,
    }

    return render(request, 'store/home.html', context)


@login_required
def DeleteItem(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    messages.add_message(request, messages.INFO, 'Item deleted')

    return redirect('home')


@login_required
def MonthlyRecords(request):
    today = date.today()

    # JANUARY
    Janday1 = Item.objects.filter(date__year=today.year, date__month=1, date__day=1).filter(staff=request.user)
    Janday2 = Item.objects.filter(date__year=today.year, date__month=1, date__day=2).filter(staff=request.user)
    Janday3 = Item.objects.filter(date__year=today.year, date__month=1, date__day=3).filter(staff=request.user)
    Janday4 = Item.objects.filter(date__year=today.year, date__month=1, date__day=4).filter(staff=request.user)
    Janday5 = Item.objects.filter(date__year=today.year, date__month=1, date__day=5).filter(staff=request.user)
    Janday6 = Item.objects.filter(date__year=today.year, date__month=1, date__day=6).filter(staff=request.user)
    Janday7 = Item.objects.filter(date__year=today.year, date__month=1, date__day=7).filter(staff=request.user)
    Janday8 = Item.objects.filter(date__year=today.year, date__month=1, date__day=8).filter(staff=request.user)
    Janday9 = Item.objects.filter(date__year=today.year, date__month=1, date__day=9).filter(staff=request.user)
    Janday10 = Item.objects.filter(date__year=today.year, date__month=1, date__day=10).filter(staff=request.user)
    Janday11 = Item.objects.filter(date__year=today.year, date__month=1, date__day=11).filter(staff=request.user)
    Janday12 = Item.objects.filter(date__year=today.year, date__month=1, date__day=12).filter(staff=request.user)
    Janday13 = Item.objects.filter(date__year=today.year, date__month=1, date__day=13).filter(staff=request.user)
    Janday14 = Item.objects.filter(date__year=today.year, date__month=1, date__day=14).filter(staff=request.user)
    Janday15 = Item.objects.filter(date__year=today.year, date__month=1, date__day=15).filter(staff=request.user)
    Janday16 = Item.objects.filter(date__year=today.year, date__month=1, date__day=16).filter(staff=request.user)
    Janday17 = Item.objects.filter(date__year=today.year, date__month=1, date__day=17).filter(staff=request.user)
    Janday18 = Item.objects.filter(date__year=today.year, date__month=1, date__day=18).filter(staff=request.user)
    Janday19 = Item.objects.filter(date__year=today.year, date__month=1, date__day=19).filter(staff=request.user)
    Janday20 = Item.objects.filter(date__year=today.year, date__month=1, date__day=20).filter(staff=request.user)
    Janday21 = Item.objects.filter(date__year=today.year, date__month=1, date__day=21).filter(staff=request.user)
    Janday22 = Item.objects.filter(date__year=today.year, date__month=1, date__day=22).filter(staff=request.user)
    Janday23 = Item.objects.filter(date__year=today.year, date__month=1, date__day=23).filter(staff=request.user)
    Janday24 = Item.objects.filter(date__year=today.year, date__month=1, date__day=24).filter(staff=request.user)
    Janday25 = Item.objects.filter(date__year=today.year, date__month=1, date__day=25).filter(staff=request.user)
    Janday26 = Item.objects.filter(date__year=today.year, date__month=1, date__day=26).filter(staff=request.user)
    Janday27 = Item.objects.filter(date__year=today.year, date__month=1, date__day=27).filter(staff=request.user)
    Janday28 = Item.objects.filter(date__year=today.year, date__month=1, date__day=28).filter(staff=request.user)
    Janday29 = Item.objects.filter(date__year=today.year, date__month=1, date__day=29).filter(staff=request.user)
    Janday30 = Item.objects.filter(date__year=today.year, date__month=1, date__day=30).filter(staff=request.user)
    Janday31 = Item.objects.filter(date__year=today.year, date__month=1, date__day=31).filter(staff=request.user)

    # FEBRUARY
    Febday1 = Item.objects.filter(date__year=today.year, date__month=2, date__day=1).filter(staff=request.user)
    Febday2 = Item.objects.filter(date__year=today.year, date__month=2, date__day=2).filter(staff=request.user)
    Febday3 = Item.objects.filter(date__year=today.year, date__month=2, date__day=3).filter(staff=request.user)
    Febday4 = Item.objects.filter(date__year=today.year, date__month=2, date__day=4).filter(staff=request.user)
    Febday5 = Item.objects.filter(date__year=today.year, date__month=2, date__day=5).filter(staff=request.user)
    Febday6 = Item.objects.filter(date__year=today.year, date__month=2, date__day=6).filter(staff=request.user)
    Febday7 = Item.objects.filter(date__year=today.year, date__month=2, date__day=7).filter(staff=request.user)
    Febday8 = Item.objects.filter(date__year=today.year, date__month=2, date__day=8).filter(staff=request.user)
    Febday9 = Item.objects.filter(date__year=today.year, date__month=2,  date__day=9).filter(staff=request.user)
    Febday10 = Item.objects.filter(date__year=today.year, date__month=2, date__day=10).filter(staff=request.user)
    Febday11 = Item.objects.filter(date__year=today.year, date__month=2, date__day=11).filter(staff=request.user)
    Febday12 = Item.objects.filter(date__year=today.year, date__month=2, date__day=12).filter(staff=request.user)
    Febday13 = Item.objects.filter(date__year=today.year, date__month=2, date__day=13).filter(staff=request.user)
    Febday14 = Item.objects.filter(date__year=today.year, date__month=2, date__day=14).filter(staff=request.user)
    Febday15 = Item.objects.filter(date__year=today.year, date__month=2, date__day=15).filter(staff=request.user)
    Febday16 = Item.objects.filter(date__year=today.year, date__month=2, date__day=16).filter(staff=request.user)
    Febday17 = Item.objects.filter(date__year=today.year, date__month=2, date__day=17).filter(staff=request.user)
    Febday18 = Item.objects.filter(date__year=today.year, date__month=2, date__day=18).filter(staff=request.user)
    Febday19 = Item.objects.filter(date__year=today.year, date__month=2, date__day=19).filter(staff=request.user)
    Febday20 = Item.objects.filter(date__year=today.year, date__month=2, date__day=20).filter(staff=request.user)
    Febday21 = Item.objects.filter(date__year=today.year, date__month=2, date__day=21).filter(staff=request.user)
    Febday22 = Item.objects.filter(date__year=today.year, date__month=2, date__day=22).filter(staff=request.user)
    Febday23 = Item.objects.filter(date__year=today.year, date__month=2, date__day=23).filter(staff=request.user)
    Febday24 = Item.objects.filter(date__year=today.year, date__month=2, date__day=24).filter(staff=request.user)
    Febday25 = Item.objects.filter(date__year=today.year, date__month=2, date__day=25).filter(staff=request.user)
    Febday26 = Item.objects.filter(date__year=today.year, date__month=2, date__day=26).filter(staff=request.user)
    Febday27 = Item.objects.filter(date__year=today.year, date__month=2, date__day=27).filter(staff=request.user)
    Febday28 = Item.objects.filter(date__year=today.year, date__month=2, date__day=28).filter(staff=request.user)
    Febday29 = Item.objects.filter(date__year=today.year, date__month=2, date__day=29).filter(staff=request.user)
    
    # MARCH
    Marday1 = Item.objects.filter(date__year=today.year, date__month=3, date__day=1).filter(staff=request.user)
    Marday2 = Item.objects.filter(date__year=today.year, date__month=3, date__day=2).filter(staff=request.user)
    Marday3 = Item.objects.filter(date__year=today.year, date__month=3, date__day=3).filter(staff=request.user)
    Marday4 = Item.objects.filter(date__year=today.year, date__month=3, date__day=4).filter(staff=request.user)
    Marday5 = Item.objects.filter(date__year=today.year, date__month=3, date__day=5).filter(staff=request.user)
    Marday6 = Item.objects.filter(date__year=today.year, date__month=3, date__day=6).filter(staff=request.user)
    Marday7 = Item.objects.filter(date__year=today.year, date__month=3, date__day=7).filter(staff=request.user)
    Marday8 = Item.objects.filter(date__year=today.year, date__month=3, date__day=8).filter(staff=request.user)
    Marday9 = Item.objects.filter(date__year=today.year, date__month=3, date__day=9).filter(staff=request.user)
    Marday10 = Item.objects.filter(date__year=today.year, date__month=3, date__day=10).filter(staff=request.user)
    Marday11 = Item.objects.filter(date__year=today.year, date__month=3, date__day=11).filter(staff=request.user)
    Marday12 = Item.objects.filter(date__year=today.year, date__month=3, date__day=12).filter(staff=request.user)
    Marday13 = Item.objects.filter(date__year=today.year, date__month=3, date__day=13).filter(staff=request.user)
    Marday14 = Item.objects.filter(date__year=today.year, date__month=3, date__day=14).filter(staff=request.user)
    Marday15 = Item.objects.filter(date__year=today.year, date__month=3, date__day=15).filter(staff=request.user)
    Marday16 = Item.objects.filter(date__year=today.year, date__month=3, date__day=16).filter(staff=request.user)
    Marday17 = Item.objects.filter(date__year=today.year, date__month=3, date__day=17).filter(staff=request.user)
    Marday18 = Item.objects.filter(date__year=today.year, date__month=3, date__day=18).filter(staff=request.user)
    Marday19 = Item.objects.filter(date__year=today.year, date__month=3, date__day=19).filter(staff=request.user)
    Marday20 = Item.objects.filter(date__year=today.year, date__month=3, date__day=20).filter(staff=request.user)
    Marday21 = Item.objects.filter(date__year=today.year, date__month=3, date__day=21).filter(staff=request.user)
    Marday22 = Item.objects.filter(date__year=today.year, date__month=3, date__day=22).filter(staff=request.user)
    Marday23 = Item.objects.filter(date__year=today.year, date__month=3, date__day=23).filter(staff=request.user)
    Marday24 = Item.objects.filter(date__year=today.year, date__month=3, date__day=24).filter(staff=request.user)
    Marday25 = Item.objects.filter(date__year=today.year, date__month=3, date__day=25).filter(staff=request.user)
    Marday26 = Item.objects.filter(date__year=today.year, date__month=3, date__day=26).filter(staff=request.user)
    Marday27 = Item.objects.filter(date__year=today.year, date__month=3, date__day=27).filter(staff=request.user)
    Marday28 = Item.objects.filter(date__year=today.year, date__month=3, date__day=28).filter(staff=request.user)
    Marday29 = Item.objects.filter(date__year=today.year, date__month=3, date__day=29).filter(staff=request.user)
    Marday30 = Item.objects.filter(date__year=today.year, date__month=3, date__day=30).filter(staff=request.user)
    Marday31 = Item.objects.filter(date__year=today.year, date__month=3, date__day=31).filter(staff=request.user)

    # APRIL
    Aprday1 = Item.objects.filter(date__year=today.year, date__month=4, date__day=1).filter(staff=request.user)
    Aprday2 = Item.objects.filter(date__year=today.year, date__month=4, date__day=2).filter(staff=request.user)
    Aprday3 = Item.objects.filter(date__year=today.year, date__month=4, date__day=3).filter(staff=request.user)
    Aprday4 = Item.objects.filter(date__year=today.year, date__month=4, date__day=4).filter(staff=request.user)
    Aprday5 = Item.objects.filter(date__year=today.year, date__month=4, date__day=5).filter(staff=request.user)
    Aprday6 = Item.objects.filter(date__year=today.year, date__month=4, date__day=6).filter(staff=request.user)
    Aprday7 = Item.objects.filter(date__year=today.year, date__month=4, date__day=7).filter(staff=request.user)
    Aprday8 = Item.objects.filter(date__year=today.year, date__month=4, date__day=8).filter(staff=request.user)
    Aprday9 = Item.objects.filter(date__year=today.year, date__month=4, date__day=9).filter(staff=request.user)
    Aprday10 = Item.objects.filter(date__year=today.year, date__month=4, date__day=10).filter(staff=request.user)
    Aprday11 = Item.objects.filter(date__year=today.year, date__month=4, date__day=11).filter(staff=request.user)
    Aprday12 = Item.objects.filter(date__year=today.year, date__month=4, date__day=12).filter(staff=request.user)
    Aprday13 = Item.objects.filter(date__year=today.year, date__month=4, date__day=13).filter(staff=request.user)
    Aprday14 = Item.objects.filter(date__year=today.year, date__month=4, date__day=14).filter(staff=request.user)
    Aprday15 = Item.objects.filter(date__year=today.year, date__month=4, date__day=15).filter(staff=request.user)
    Aprday16 = Item.objects.filter(date__year=today.year, date__month=4, date__day=16).filter(staff=request.user)
    Aprday17 = Item.objects.filter(date__year=today.year, date__month=4, date__day=17).filter(staff=request.user)
    Aprday18 = Item.objects.filter(date__year=today.year, date__month=4, date__day=18).filter(staff=request.user)
    Aprday19 = Item.objects.filter(date__year=today.year, date__month=4, date__day=19).filter(staff=request.user)
    Aprday20 = Item.objects.filter(date__year=today.year, date__month=4, date__day=20).filter(staff=request.user)
    Aprday21 = Item.objects.filter(date__year=today.year, date__month=4, date__day=21).filter(staff=request.user)
    Aprday22 = Item.objects.filter(date__year=today.year, date__month=4, date__day=22).filter(staff=request.user)
    Aprday23 = Item.objects.filter(date__year=today.year, date__month=4, date__day=23).filter(staff=request.user)
    Aprday24 = Item.objects.filter(date__year=today.year, date__month=4, date__day=24).filter(staff=request.user)
    Aprday25 = Item.objects.filter(date__year=today.year, date__month=4, date__day=25).filter(staff=request.user)
    Aprday26 = Item.objects.filter(date__year=today.year, date__month=4, date__day=26).filter(staff=request.user)
    Aprday27 = Item.objects.filter(date__year=today.year, date__month=4, date__day=27).filter(staff=request.user)
    Aprday28 = Item.objects.filter(date__year=today.year, date__month=4, date__day=28).filter(staff=request.user)
    Aprday29 = Item.objects.filter(date__year=today.year, date__month=4, date__day=29).filter(staff=request.user)
    Aprday30 = Item.objects.filter(date__year=today.year, date__month=4, date__day=30).filter(staff=request.user)

    # MAY
    Mayday1 = Item.objects.filter(date__year=today.year, date__month=5, date__day=1).filter(staff=request.user)
    Mayday2 = Item.objects.filter(date__year=today.year, date__month=5, date__day=2).filter(staff=request.user)
    Mayday3 = Item.objects.filter(date__year=today.year, date__month=5, date__day=3).filter(staff=request.user)
    Mayday4 = Item.objects.filter(date__year=today.year, date__month=5, date__day=4).filter(staff=request.user)
    Mayday5 = Item.objects.filter(date__year=today.year, date__month=5, date__day=5).filter(staff=request.user)
    Mayday6 = Item.objects.filter(date__year=today.year, date__month=5, date__day=6).filter(staff=request.user)
    Mayday7 = Item.objects.filter(date__year=today.year, date__month=5, date__day=7).filter(staff=request.user)
    Mayday8 = Item.objects.filter(date__year=today.year, date__month=5, date__day=8).filter(staff=request.user)
    Mayday9 = Item.objects.filter(date__year=today.year, date__month=5, date__day=9).filter(staff=request.user)
    Mayday10 = Item.objects.filter(date__year=today.year, date__month=5, date__day=10).filter(staff=request.user)
    Mayday11 = Item.objects.filter(date__year=today.year, date__month=5, date__day=11).filter(staff=request.user)
    Mayday12 = Item.objects.filter(date__year=today.year, date__month=5, date__day=12).filter(staff=request.user)
    Mayday13 = Item.objects.filter(date__year=today.year, date__month=5, date__day=13).filter(staff=request.user)
    Mayday14 = Item.objects.filter(date__year=today.year, date__month=5, date__day=14).filter(staff=request.user)
    Mayday15 = Item.objects.filter(date__year=today.year, date__month=5, date__day=15).filter(staff=request.user)
    Mayday16 = Item.objects.filter(date__year=today.year, date__month=5, date__day=16).filter(staff=request.user)
    Mayday17 = Item.objects.filter(date__year=today.year, date__month=5, date__day=17).filter(staff=request.user)
    Mayday18 = Item.objects.filter(date__year=today.year, date__month=5, date__day=18).filter(staff=request.user)
    Mayday19 = Item.objects.filter(date__year=today.year, date__month=5, date__day=19).filter(staff=request.user)
    Mayday20 = Item.objects.filter(date__year=today.year, date__month=5, date__day=20).filter(staff=request.user)
    Mayday21 = Item.objects.filter(date__year=today.year, date__month=5, date__day=21).filter(staff=request.user)
    Mayday22 = Item.objects.filter(date__year=today.year, date__month=5, date__day=22).filter(staff=request.user)
    Mayday23 = Item.objects.filter(date__year=today.year, date__month=5, date__day=23).filter(staff=request.user)
    Mayday24 = Item.objects.filter(date__year=today.year, date__month=5, date__day=24).filter(staff=request.user)
    Mayday25 = Item.objects.filter(date__year=today.year, date__month=5, date__day=25).filter(staff=request.user)
    Mayday26 = Item.objects.filter(date__year=today.year, date__month=5, date__day=26).filter(staff=request.user)
    Mayday27 = Item.objects.filter(date__year=today.year, date__month=5, date__day=27).filter(staff=request.user)
    Mayday28 = Item.objects.filter(date__year=today.year, date__month=5, date__day=28).filter(staff=request.user)
    Mayday29 = Item.objects.filter(date__year=today.year, date__month=5, date__day=29).filter(staff=request.user)
    Mayday30 = Item.objects.filter(date__year=today.year, date__month=5, date__day=30).filter(staff=request.user)
    Mayday31 = Item.objects.filter(date__year=today.year, date__month=5, date__day=31).filter(staff=request.user)

    # JUNE
    Junday1 = Item.objects.filter(date__year=today.year, date__month=6, date__day=1).filter(staff=request.user)
    Junday2 = Item.objects.filter(date__year=today.year, date__month=6, date__day=2).filter(staff=request.user)
    Junday3 = Item.objects.filter(date__year=today.year, date__month=6, date__day=3).filter(staff=request.user)
    Junday4 = Item.objects.filter(date__year=today.year, date__month=6, date__day=4).filter(staff=request.user)
    Junday5 = Item.objects.filter(date__year=today.year, date__month=6, date__day=5).filter(staff=request.user)
    Junday6 = Item.objects.filter(date__year=today.year, date__month=6, date__day=6).filter(staff=request.user)
    Junday7 = Item.objects.filter(date__year=today.year, date__month=6, date__day=7).filter(staff=request.user)
    Junday8 = Item.objects.filter(date__year=today.year, date__month=6, date__day=8).filter(staff=request.user)
    Junday9 = Item.objects.filter(date__year=today.year, date__month=6, date__day=9).filter(staff=request.user)
    Junday10 = Item.objects.filter(date__year=today.year, date__month=6, date__day=10).filter(staff=request.user)
    Junday11 = Item.objects.filter(date__year=today.year, date__month=6, date__day=11).filter(staff=request.user)
    Junday12 = Item.objects.filter(date__year=today.year, date__month=6, date__day=12).filter(staff=request.user)
    Junday13 = Item.objects.filter(date__year=today.year, date__month=6, date__day=13).filter(staff=request.user)
    Junday14 = Item.objects.filter(date__year=today.year, date__month=6, date__day=14).filter(staff=request.user)
    Junday15 = Item.objects.filter(date__year=today.year, date__month=6, date__day=15).filter(staff=request.user)
    Junday16 = Item.objects.filter(date__year=today.year, date__month=6, date__day=16).filter(staff=request.user)
    Junday17 = Item.objects.filter(date__year=today.year, date__month=6, date__day=17).filter(staff=request.user)
    Junday18 = Item.objects.filter(date__year=today.year, date__month=6, date__day=18).filter(staff=request.user)
    Junday19 = Item.objects.filter(date__year=today.year, date__month=6, date__day=19).filter(staff=request.user)
    Junday20 = Item.objects.filter(date__year=today.year, date__month=6, date__day=20).filter(staff=request.user)
    Junday21 = Item.objects.filter(date__year=today.year, date__month=6, date__day=21).filter(staff=request.user)
    Junday22 = Item.objects.filter(date__year=today.year, date__month=6, date__day=22).filter(staff=request.user)
    Junday23 = Item.objects.filter(date__year=today.year, date__month=6, date__day=23).filter(staff=request.user)
    Junday24 = Item.objects.filter(date__year=today.year, date__month=6, date__day=24).filter(staff=request.user)
    Junday25 = Item.objects.filter(date__year=today.year, date__month=6, date__day=25).filter(staff=request.user)
    Junday26 = Item.objects.filter(date__year=today.year, date__month=6, date__day=26).filter(staff=request.user)
    Junday27 = Item.objects.filter(date__year=today.year, date__month=6, date__day=27).filter(staff=request.user)
    Junday28 = Item.objects.filter(date__year=today.year, date__month=6, date__day=28).filter(staff=request.user)
    Junday29 = Item.objects.filter(date__year=today.year, date__month=6, date__day=29).filter(staff=request.user)
    Junday30 = Item.objects.filter(date__year=today.year, date__month=6, date__day=30).filter(staff=request.user)

    # JULY
    Julday1 = Item.objects.filter(date__year=today.year, date__month=7, date__day=1).filter(staff=request.user)
    Julday2 = Item.objects.filter(date__year=today.year, date__month=7, date__day=2).filter(staff=request.user)
    Julday3 = Item.objects.filter(date__year=today.year, date__month=7, date__day=3).filter(staff=request.user)
    Julday4 = Item.objects.filter(date__year=today.year, date__month=7, date__day=4).filter(staff=request.user)
    Julday5 = Item.objects.filter(date__year=today.year, date__month=7, date__day=5).filter(staff=request.user)
    Julday6 = Item.objects.filter(date__year=today.year, date__month=7, date__day=6).filter(staff=request.user)
    Julday7 = Item.objects.filter(date__year=today.year, date__month=7, date__day=7).filter(staff=request.user)
    Julday8 = Item.objects.filter(date__year=today.year, date__month=7, date__day=8).filter(staff=request.user)
    Julday9 = Item.objects.filter(date__year=today.year, date__month=7, date__day=9).filter(staff=request.user)
    Julday10 = Item.objects.filter(date__year=today.year, date__month=7, date__day=10).filter(staff=request.user)
    Julday11 = Item.objects.filter(date__year=today.year, date__month=7, date__day=11).filter(staff=request.user)
    Julday12 = Item.objects.filter(date__year=today.year, date__month=7, date__day=12).filter(staff=request.user)
    Julday13 = Item.objects.filter(date__year=today.year, date__month=7, date__day=13).filter(staff=request.user)
    Julday14 = Item.objects.filter(date__year=today.year, date__month=7, date__day=14).filter(staff=request.user)
    Julday15 = Item.objects.filter(date__year=today.year, date__month=7, date__day=15).filter(staff=request.user)
    Julday16 = Item.objects.filter(date__year=today.year, date__month=7, date__day=16).filter(staff=request.user)
    Julday17 = Item.objects.filter(date__year=today.year, date__month=7, date__day=17).filter(staff=request.user)
    Julday18 = Item.objects.filter(date__year=today.year, date__month=7, date__day=18).filter(staff=request.user)
    Julday19 = Item.objects.filter(date__year=today.year, date__month=7, date__day=19).filter(staff=request.user)
    Julday20 = Item.objects.filter(date__year=today.year, date__month=7, date__day=20).filter(staff=request.user)
    Julday21 = Item.objects.filter(date__year=today.year, date__month=7, date__day=21).filter(staff=request.user)
    Julday22 = Item.objects.filter(date__year=today.year, date__month=7, date__day=22).filter(staff=request.user)
    Julday23 = Item.objects.filter(date__year=today.year, date__month=7, date__day=23).filter(staff=request.user)
    Julday24 = Item.objects.filter(date__year=today.year, date__month=7, date__day=24).filter(staff=request.user)
    Julday25 = Item.objects.filter(date__year=today.year, date__month=7, date__day=25).filter(staff=request.user)
    Julday26 = Item.objects.filter(date__year=today.year, date__month=7, date__day=26).filter(staff=request.user)
    Julday27 = Item.objects.filter(date__year=today.year, date__month=7, date__day=27).filter(staff=request.user)
    Julday28 = Item.objects.filter(date__year=today.year, date__month=7, date__day=28).filter(staff=request.user)
    Julday29 = Item.objects.filter(date__year=today.year, date__month=7, date__day=29).filter(staff=request.user)
    Julday30 = Item.objects.filter(date__year=today.year, date__month=7, date__day=30).filter(staff=request.user)
    Julday31 = Item.objects.filter(date__year=today.year, date__month=7, date__day=31).filter(staff=request.user)

    # AUGUST
    Augday1 = Item.objects.filter(date__year=today.year, date__month=8, date__day=1).filter(staff=request.user)
    Augday2 = Item.objects.filter(date__year=today.year, date__month=8, date__day=2).filter(staff=request.user)
    Augday3 = Item.objects.filter(date__year=today.year, date__month=8, date__day=3).filter(staff=request.user)
    Augday4 = Item.objects.filter(date__year=today.year, date__month=8, date__day=4).filter(staff=request.user)
    Augday5 = Item.objects.filter(date__year=today.year, date__month=8, date__day=5).filter(staff=request.user)
    Augday6 = Item.objects.filter(date__year=today.year, date__month=8, date__day=6).filter(staff=request.user)
    Augday7 = Item.objects.filter(date__year=today.year, date__month=8, date__day=7).filter(staff=request.user)
    Augday8 = Item.objects.filter(date__year=today.year, date__month=8, date__day=8).filter(staff=request.user)
    Augday9 = Item.objects.filter(date__year=today.year, date__month=8, date__day=9).filter(staff=request.user)
    Augday10 = Item.objects.filter(date__year=today.year, date__month=8, date__day=10).filter(staff=request.user)
    Augday11 = Item.objects.filter(date__year=today.year, date__month=8, date__day=11).filter(staff=request.user)
    Augday12 = Item.objects.filter(date__year=today.year, date__month=8, date__day=12).filter(staff=request.user)
    Augday13 = Item.objects.filter(date__year=today.year, date__month=8, date__day=13).filter(staff=request.user)
    Augday14 = Item.objects.filter(date__year=today.year, date__month=8, date__day=14).filter(staff=request.user)
    Augday15 = Item.objects.filter(date__year=today.year, date__month=8, date__day=15).filter(staff=request.user)
    Augday16 = Item.objects.filter(date__year=today.year, date__month=8, date__day=16).filter(staff=request.user)
    Augday17 = Item.objects.filter(date__year=today.year, date__month=8, date__day=17).filter(staff=request.user)
    Augday18 = Item.objects.filter(date__year=today.year, date__month=8, date__day=18).filter(staff=request.user)
    Augday19 = Item.objects.filter(date__year=today.year, date__month=8, date__day=19).filter(staff=request.user)
    Augday20 = Item.objects.filter(date__year=today.year, date__month=8, date__day=20).filter(staff=request.user)
    Augday21 = Item.objects.filter(date__year=today.year, date__month=8, date__day=21).filter(staff=request.user)
    Augday22 = Item.objects.filter(date__year=today.year, date__month=8, date__day=22).filter(staff=request.user)
    Augday23 = Item.objects.filter(date__year=today.year, date__month=8, date__day=23).filter(staff=request.user)
    Augday24 = Item.objects.filter(date__year=today.year, date__month=8, date__day=24).filter(staff=request.user)
    Augday25 = Item.objects.filter(date__year=today.year, date__month=8, date__day=25).filter(staff=request.user)
    Augday26 = Item.objects.filter(date__year=today.year, date__month=8, date__day=26).filter(staff=request.user)
    Augday27 = Item.objects.filter(date__year=today.year, date__month=8, date__day=27).filter(staff=request.user)
    Augday28 = Item.objects.filter(date__year=today.year, date__month=8, date__day=28).filter(staff=request.user)
    Augday29 = Item.objects.filter(date__year=today.year, date__month=8, date__day=29).filter(staff=request.user)
    Augday30 = Item.objects.filter(date__year=today.year, date__month=8, date__day=30).filter(staff=request.user)
    Augday31 = Item.objects.filter(date__year=today.year, date__month=8, date__day=31).filter(staff=request.user)

    # SEPTEMBER
    Sepday1 = Item.objects.filter(date__year=today.year, date__month=9, date__day=1).filter(staff=request.user)
    Sepday2 = Item.objects.filter(date__year=today.year, date__month=9, date__day=2).filter(staff=request.user)
    Sepday3 = Item.objects.filter(date__year=today.year, date__month=9, date__day=3).filter(staff=request.user)
    Sepday4 = Item.objects.filter(date__year=today.year, date__month=9, date__day=4).filter(staff=request.user)
    Sepday5 = Item.objects.filter(date__year=today.year, date__month=9, date__day=5).filter(staff=request.user)
    Sepday6 = Item.objects.filter(date__year=today.year, date__month=9, date__day=6).filter(staff=request.user)
    Sepday7 = Item.objects.filter(date__year=today.year, date__month=9, date__day=7).filter(staff=request.user)
    Sepday8 = Item.objects.filter(date__year=today.year, date__month=9, date__day=8).filter(staff=request.user)
    Sepday9 = Item.objects.filter(date__year=today.year, date__month=9, date__day=9).filter(staff=request.user)
    Sepday10 = Item.objects.filter(date__year=today.year, date__month=9, date__day=10).filter(staff=request.user)
    Sepday11 = Item.objects.filter(date__year=today.year, date__month=9, date__day=11).filter(staff=request.user)
    Sepday12 = Item.objects.filter(date__year=today.year, date__month=9, date__day=12).filter(staff=request.user)
    Sepday13 = Item.objects.filter(date__year=today.year, date__month=9, date__day=13).filter(staff=request.user)
    Sepday14 = Item.objects.filter(date__year=today.year, date__month=9, date__day=14).filter(staff=request.user)
    Sepday15 = Item.objects.filter(date__year=today.year, date__month=9, date__day=15).filter(staff=request.user)
    Sepday16 = Item.objects.filter(date__year=today.year, date__month=9, date__day=16).filter(staff=request.user)
    Sepday17 = Item.objects.filter(date__year=today.year, date__month=9, date__day=17).filter(staff=request.user)
    Sepday18 = Item.objects.filter(date__year=today.year, date__month=9, date__day=18).filter(staff=request.user)
    Sepday19 = Item.objects.filter(date__year=today.year, date__month=9, date__day=19).filter(staff=request.user)
    Sepday20 = Item.objects.filter(date__year=today.year, date__month=9, date__day=20).filter(staff=request.user)
    Sepday21 = Item.objects.filter(date__year=today.year, date__month=9, date__day=21).filter(staff=request.user)
    Sepday22 = Item.objects.filter(date__year=today.year, date__month=9, date__day=22).filter(staff=request.user)
    Sepday23 = Item.objects.filter(date__year=today.year, date__month=9, date__day=23).filter(staff=request.user)
    Sepday24 = Item.objects.filter(date__year=today.year, date__month=9, date__day=24).filter(staff=request.user)
    Sepday25 = Item.objects.filter(date__year=today.year, date__month=9, date__day=25).filter(staff=request.user)
    Sepday26 = Item.objects.filter(date__year=today.year, date__month=9, date__day=26).filter(staff=request.user)
    Sepday27 = Item.objects.filter(date__year=today.year, date__month=9, date__day=27).filter(staff=request.user)
    Sepday28 = Item.objects.filter(date__year=today.year, date__month=9, date__day=28).filter(staff=request.user)
    Sepday29 = Item.objects.filter(date__year=today.year, date__month=9, date__day=29).filter(staff=request.user)
    Sepday30 = Item.objects.filter(date__year=today.year, date__month=9, date__day=30).filter(staff=request.user)

    # OCTOBER
    Octday1 = Item.objects.filter(date__year=today.year, date__month=10, date__day=1).filter(staff=request.user)
    Octday2 = Item.objects.filter(date__year=today.year, date__month=10, date__day=2).filter(staff=request.user)
    Octday3 = Item.objects.filter(date__year=today.year, date__month=10, date__day=3).filter(staff=request.user)
    Octday4 = Item.objects.filter(date__year=today.year, date__month=10, date__day=4).filter(staff=request.user)
    Octday5 = Item.objects.filter(date__year=today.year, date__month=10, date__day=5).filter(staff=request.user)
    Octday6 = Item.objects.filter(date__year=today.year, date__month=10, date__day=6).filter(staff=request.user)
    Octday7 = Item.objects.filter(date__year=today.year, date__month=10, date__day=7).filter(staff=request.user)
    Octday8 = Item.objects.filter(date__year=today.year, date__month=10, date__day=8).filter(staff=request.user)
    Octday9 = Item.objects.filter(date__year=today.year, date__month=10, date__day=9).filter(staff=request.user)
    Octday10 = Item.objects.filter(date__year=today.year, date__month=10, date__day=10).filter(staff=request.user)
    Octday11 = Item.objects.filter(date__year=today.year, date__month=10, date__day=11).filter(staff=request.user)
    Octday12 = Item.objects.filter(date__year=today.year, date__month=10, date__day=12).filter(staff=request.user)
    Octday13 = Item.objects.filter(date__year=today.year, date__month=10, date__day=13).filter(staff=request.user)
    Octday14 = Item.objects.filter(date__year=today.year, date__month=10, date__day=14).filter(staff=request.user)
    Octday15 = Item.objects.filter(date__year=today.year, date__month=10, date__day=15).filter(staff=request.user)
    Octday16 = Item.objects.filter(date__year=today.year, date__month=10, date__day=16).filter(staff=request.user)
    Octday17 = Item.objects.filter(date__year=today.year, date__month=10, date__day=17).filter(staff=request.user)
    Octday18 = Item.objects.filter(date__year=today.year, date__month=10, date__day=18).filter(staff=request.user)
    Octday19 = Item.objects.filter(date__year=today.year, date__month=10, date__day=19).filter(staff=request.user)
    Octday20 = Item.objects.filter(date__year=today.year, date__month=10, date__day=20).filter(staff=request.user)
    Octday21 = Item.objects.filter(date__year=today.year, date__month=10, date__day=21).filter(staff=request.user)
    Octday22 = Item.objects.filter(date__year=today.year, date__month=10, date__day=22).filter(staff=request.user)
    Octday23 = Item.objects.filter(date__year=today.year, date__month=10, date__day=23).filter(staff=request.user)
    Octday24 = Item.objects.filter(date__year=today.year, date__month=10, date__day=24).filter(staff=request.user)
    Octday25 = Item.objects.filter(date__year=today.year, date__month=10, date__day=25).filter(staff=request.user)
    Octday26 = Item.objects.filter(date__year=today.year, date__month=10, date__day=26).filter(staff=request.user)
    Octday27 = Item.objects.filter(date__year=today.year, date__month=10, date__day=27).filter(staff=request.user)
    Octday28 = Item.objects.filter(date__year=today.year, date__month=10, date__day=28).filter(staff=request.user)
    Octday29 = Item.objects.filter(date__year=today.year, date__month=10, date__day=29).filter(staff=request.user)
    Octday30 = Item.objects.filter(date__year=today.year, date__month=10, date__day=30).filter(staff=request.user)
    Octday31 = Item.objects.filter(date__year=today.year, date__month=10, date__day=31).filter(staff=request.user)

    # NOVEMBER
    Novday1 = Item.objects.filter(date__year=today.year, date__month=11, date__day=1).filter(staff=request.user)
    Novday2 = Item.objects.filter(date__year=today.year, date__month=11, date__day=2).filter(staff=request.user)
    Novday3 = Item.objects.filter(date__year=today.year, date__month=11, date__day=3).filter(staff=request.user)
    Novday4 = Item.objects.filter(date__year=today.year, date__month=11, date__day=4).filter(staff=request.user)
    Novday5 = Item.objects.filter(date__year=today.year, date__month=11, date__day=5).filter(staff=request.user)
    Novday6 = Item.objects.filter(date__year=today.year, date__month=11, date__day=6).filter(staff=request.user)
    Novday7 = Item.objects.filter(date__year=today.year, date__month=11, date__day=7).filter(staff=request.user)
    Novday8 = Item.objects.filter(date__year=today.year, date__month=11, date__day=8).filter(staff=request.user)
    Novday9 = Item.objects.filter(date__year=today.year, date__month=11, date__day=9).filter(staff=request.user)
    Novday10 = Item.objects.filter(date__year=today.year, date__month=11, date__day=10).filter(staff=request.user)
    Novday11 = Item.objects.filter(date__year=today.year, date__month=11, date__day=11).filter(staff=request.user)
    Novday12 = Item.objects.filter(date__year=today.year, date__month=11, date__day=12).filter(staff=request.user)
    Novday13 = Item.objects.filter(date__year=today.year, date__month=11, date__day=13).filter(staff=request.user)
    Novday14 = Item.objects.filter(date__year=today.year, date__month=11, date__day=14).filter(staff=request.user)
    Novday15 = Item.objects.filter(date__year=today.year, date__month=11, date__day=15).filter(staff=request.user)
    Novday16 = Item.objects.filter(date__year=today.year, date__month=11, date__day=16).filter(staff=request.user)
    Novday17 = Item.objects.filter(date__year=today.year, date__month=11, date__day=17).filter(staff=request.user)
    Novday18 = Item.objects.filter(date__year=today.year, date__month=11, date__day=18).filter(staff=request.user)
    Novday19 = Item.objects.filter(date__year=today.year, date__month=11, date__day=19).filter(staff=request.user)
    Novday20 = Item.objects.filter(date__year=today.year, date__month=11, date__day=20).filter(staff=request.user)
    Novday21 = Item.objects.filter(date__year=today.year, date__month=11, date__day=21).filter(staff=request.user)
    Novday22 = Item.objects.filter(date__year=today.year, date__month=11, date__day=22).filter(staff=request.user)
    Novday23 = Item.objects.filter(date__year=today.year, date__month=11, date__day=23).filter(staff=request.user)
    Novday24 = Item.objects.filter(date__year=today.year, date__month=11, date__day=24).filter(staff=request.user)
    Novday25 = Item.objects.filter(date__year=today.year, date__month=11, date__day=25).filter(staff=request.user)
    Novday26 = Item.objects.filter(date__year=today.year, date__month=11, date__day=26).filter(staff=request.user)
    Novday27 = Item.objects.filter(date__year=today.year, date__month=11, date__day=27).filter(staff=request.user)
    Novday28 = Item.objects.filter(date__year=today.year, date__month=11, date__day=28).filter(staff=request.user)
    Novday29 = Item.objects.filter(date__year=today.year, date__month=11, date__day=29).filter(staff=request.user)
    Novday30 = Item.objects.filter(date__year=today.year, date__month=11, date__day=30).filter(staff=request.user)

    # DECEMBER
    Decday1 = Item.objects.filter(date__year=today.year, date__month=12, date__day=1).filter(staff=request.user)
    Decday2 = Item.objects.filter(date__year=today.year, date__month=12, date__day=2).filter(staff=request.user)
    Decday3 = Item.objects.filter(date__year=today.year, date__month=12, date__day=3).filter(staff=request.user)
    Decday4 = Item.objects.filter(date__year=today.year, date__month=12, date__day=4).filter(staff=request.user)
    Decday5 = Item.objects.filter(date__year=today.year, date__month=12, date__day=5).filter(staff=request.user)
    Decday6 = Item.objects.filter(date__year=today.year, date__month=12, date__day=6).filter(staff=request.user)
    Decday7 = Item.objects.filter(date__year=today.year, date__month=12, date__day=7).filter(staff=request.user)
    Decday8 = Item.objects.filter(date__year=today.year, date__month=12, date__day=8).filter(staff=request.user)
    Decday9 = Item.objects.filter(date__year=today.year, date__month=12, date__day=9).filter(staff=request.user)
    Decday10 = Item.objects.filter(date__year=today.year, date__month=12, date__day=10).filter(staff=request.user)
    Decday11 = Item.objects.filter(date__year=today.year, date__month=12, date__day=11).filter(staff=request.user)
    Decday12 = Item.objects.filter(date__year=today.year, date__month=12, date__day=12).filter(staff=request.user)
    Decday13 = Item.objects.filter(date__year=today.year, date__month=12, date__day=13).filter(staff=request.user)
    Decday14 = Item.objects.filter(date__year=today.year, date__month=12, date__day=14).filter(staff=request.user)
    Decday15 = Item.objects.filter(date__year=today.year, date__month=12, date__day=15).filter(staff=request.user)
    Decday16 = Item.objects.filter(date__year=today.year, date__month=12, date__day=16).filter(staff=request.user)
    Decday17 = Item.objects.filter(date__year=today.year, date__month=12, date__day=17).filter(staff=request.user)
    Decday18 = Item.objects.filter(date__year=today.year, date__month=12, date__day=18).filter(staff=request.user)
    Decday19 = Item.objects.filter(date__year=today.year, date__month=12, date__day=19).filter(staff=request.user)
    Decday20 = Item.objects.filter(date__year=today.year, date__month=12, date__day=20).filter(staff=request.user)
    Decday21 = Item.objects.filter(date__year=today.year, date__month=12, date__day=21).filter(staff=request.user)
    Decday22 = Item.objects.filter(date__year=today.year, date__month=12, date__day=22).filter(staff=request.user)
    Decday23 = Item.objects.filter(date__year=today.year, date__month=12, date__day=23).filter(staff=request.user)
    Decday24 = Item.objects.filter(date__year=today.year, date__month=12, date__day=24).filter(staff=request.user)
    Decday25 = Item.objects.filter(date__year=today.year, date__month=12, date__day=25).filter(staff=request.user)
    Decday26 = Item.objects.filter(date__year=today.year, date__month=12, date__day=26).filter(staff=request.user)
    Decday27 = Item.objects.filter(date__year=today.year, date__month=12, date__day=27).filter(staff=request.user)
    Decday28 = Item.objects.filter(date__year=today.year, date__month=12, date__day=28).filter(staff=request.user)
    Decday29 = Item.objects.filter(date__year=today.year, date__month=12, date__day=29).filter(staff=request.user)
    Decday30 = Item.objects.filter(date__year=today.year, date__month=12, date__day=30).filter(staff=request.user)
    Decday31 = Item.objects.filter(date__year=today.year, date__month=12, date__day=31).filter(staff=request.user)

    context = {
        'date': today,
        # JANUARY 
        'Janday1': Janday1, 'Janday2': Janday2, 'Janday3': Janday3, 'Janday4': Janday4, 'Janday5': Janday5, 'Janday6': Janday6, 'Janday7': Janday7, 'Janday8': Janday8,
        'Janday9': Janday9, 'Janday10': Janday10, 'Janday11': Janday11, 'Janday12': Janday12, 'Janday13': Janday13, 'Janday14': Janday14, 'Janday15': Janday15, 'Janday16': Janday16,
        'Janday17': Janday17, 'Janday18': Janday18, 'Janday19': Janday19, 'Janday20': Janday20, 'Janday21': Janday21, 'Janday22': Janday22, 'Janday23': Janday23, 'Janday24': Janday24,
        'Janday25': Janday25, 'Janday26': Janday26, 'Janday27': Janday27, 'Janday28': Janday28, 'Janday29': Janday29, 'Janday30': Janday30, 'Janday31': Janday31,
         
        # FEBRUARY
        'Febday1': Febday1, 'Febday2': Febday2, 'Febday3': Febday3, 'Febday4': Febday4, 'Febday5': Febday5, 'Febday6': Febday6, 'Febday7': Febday7, 'Febday8': Febday8, 
        'Febday9':Febday9, 'Febday10': Febday10, 'Febday11': Febday11, 'Febday12': Febday12, 'Febday13': Febday13, 'Febday14': Febday14, 'Febday15': Febday15, 'Febday16': Febday16,
        'Febday17': Febday17, 'Febday18': Febday18, 'Febday19': Febday19, 'Febday20': Febday20, 'Febday21': Febday21, 'Febday22': Febday22, 'Febday23': Febday23, 'Febday24': Febday24,
        'Febday25': Febday25, 'Febday26': Febday26, 'Febday27': Febday27, 'Febday28': Febday28, 'Febday29': Febday29,

        # MARCH
        'Marday1': Marday1, 'Marday2': Marday2, 'Marday3': Marday3, 'Marday4': Marday4, 'Marday5': Marday5, 'Marday6': Marday6, 'Marday7': Marday7, 'Marday8': Marday8,
        'Marday9': Marday9, 'Marday10': Marday10, 'Marday11': Marday11, 'Marday12': Marday12, 'Marday13': Marday13, 'Marday14': Marday14, 'Marday15': Marday15, 'Marday16': Marday16,
        'Marday17': Marday17, 'Marday18': Marday18, 'Marday19': Marday19, 'Marday20': Marday20, 'Marday21': Marday21, 'Marday22': Marday22, 'Marday23': Marday23, 'Marday24': Marday24,
        'Marday25': Marday25, 'Marday26': Marday26, 'Marday27': Marday27, 'Marday28': Marday28, 'Marday29': Marday29, 'Marday30': Marday30, 'Marday31': Marday31,

        # APRIL 
        'Aprday1': Aprday1, 'Aprday2': Aprday2, 'Aprday3': Aprday3, 'Aprday4': Aprday4, 'Aprday5': Aprday5, 'Aprday6': Aprday6, 'Aprday7': Aprday7, 'Aprday8': Aprday8,
        'Aprday9': Aprday9, 'Aprday10': Aprday10, 'Aprday11': Aprday11, 'Aprday12': Aprday12, 'Aprday13': Aprday13, 'Aprday14': Aprday14, 'Aprday15': Aprday15, 'Aprday16': Aprday16,
        'Aprday17': Aprday17, 'Aprday18': Aprday18, 'Aprday19': Aprday19, 'Aprday20': Aprday20, 'Aprday21': Aprday21, 'Aprday22': Aprday22, 'Aprday23': Aprday23, 'Aprday24': Aprday24,
        'Aprday25': Aprday25, 'Aprday26': Aprday26, 'Aprday27': Aprday27, 'Aprday28': Aprday28, 'Aprday29': Aprday29, 'Aprday30': Aprday30,
         
        # MAY
        'Mayday1': Mayday1, 'Mayday2': Mayday2, 'Mayday3': Mayday3, 'Mayday4': Mayday4, 'Mayday5': Mayday5, 'Mayday6': Mayday6, 'Mayday7': Mayday7, 'Mayday8': Mayday8, 
        'Mayday9': Mayday9, 'Mayday10': Mayday10, 'Mayday11': Mayday11, 'Mayday12': Mayday12, 'Mayday13': Mayday13, 'Mayday14': Mayday14, 'Mayday15': Mayday15, 'Mayday16': Mayday16,
        'Mayday17': Mayday17, 'Mayday18': Mayday18, 'Mayday19': Mayday19, 'Mayday20': Mayday20, 'Mayday21': Mayday21, 'Mayday22': Mayday22, 'Mayday23': Mayday23, 'Mayday24': Mayday24,
        'Mayday25': Mayday25, 'Mayday26': Mayday26, 'Mayday27': Mayday27, 'Mayday28': Mayday28, 'Mayday29': Mayday29, 'Mayday30': Mayday30, 'Mayday31': Mayday31,

        # JUNE
        'Junday1': Junday1, 'Junday2': Junday2, 'Junday3': Junday3, 'Junday4': Junday4, 'Junday5': Junday5, 'Junday6': Junday6, 'Junday7': Junday7, 'Junday8': Junday8,
        'Junday9': Junday9, 'Junday10': Junday10, 'Junday11': Junday11, 'Junday12': Junday12, 'Junday13': Junday13, 'Junday14': Junday14, 'Junday15': Junday15, 'Junday16': Junday16,
        'Junday17': Junday17, 'Junday18': Junday18, 'Junday19': Junday19, 'Junday20': Junday20, 'Junday21': Junday21, 'Junday22': Junday22, 'Junday23': Junday23, 'Junday24': Junday24,
        'Junday25': Junday25, 'Junday26': Junday26, 'Junday27': Junday27, 'Junday28': Junday28, 'Junday29': Junday29, 'Junday30': Junday30,

        # JULY 
        'Julday1': Julday1, 'Julday2': Julday2, 'Julday3': Julday3, 'Julday4': Julday4, 'Julday5': Julday5, 'Julday6': Julday6, 'Julday7': Julday7, 'Julday8': Julday8,
        'Julday9': Julday9, 'Julday10': Julday10, 'Julday11': Julday11, 'Julday12': Julday12, 'Julday13': Julday13, 'Julday14': Julday14, 'Julday15': Julday15, 'Julday16': Julday16,
        'Julday17': Julday17, 'Julday18': Julday18, 'Julday19': Julday19, 'Julday20': Julday20, 'Julday21': Julday21, 'Julday22': Julday22, 'Julday23': Julday23, 'Julday24': Julday24,
        'Julday25': Julday25, 'Julday26': Julday26, 'Julday27': Julday27, 'Julday28': Julday28, 'Julday29': Julday29, 'Julday30': Julday30, 'Julday31': Julday31,
         
        # AUGUST
        'Augday1': Augday1, 'Augday2': Augday2, 'Augday3': Augday3, 'Augday4': Augday4, 'Augday5': Augday5, 'Augday6': Augday6, 'Augday7': Augday7, 'Augday8': Augday8, 
        'Augday9': Augday9, 'Augday10': Augday10, 'Augday11': Augday11, 'Augday12': Augday12, 'Augday13': Augday13, 'Augday14': Augday14, 'Augday15': Augday15, 'Augday16': Augday16,
        'Augday17': Augday17, 'Augday18': Augday18, 'Augday19': Augday19, 'Augday20': Augday20, 'Augday21': Augday21, 'Augday22': Augday22, 'Augday23': Augday23, 'Augday24': Augday24,
        'Augday25': Augday25, 'Augday26': Augday26, 'Augday27': Augday27, 'Augday28': Augday28, 'Augday29': Augday29, 'Augday30': Augday30, 'Augday31': Augday31,

        # SEPTEMBER
        'Sepday1': Sepday1, 'Sepday2': Sepday2, 'Sepday3': Sepday3, 'Sepday4': Sepday4, 'Sepday5': Sepday5, 'Sepday6': Sepday6, 'Sepday7': Sepday7, 'Sepday8': Sepday8,
        'Sepday9': Sepday9, 'Sepday10': Sepday10, 'Sepday11': Sepday11, 'Sepday12': Sepday12, 'Sepday13': Sepday13, 'Sepday14': Sepday14, 'Sepday15': Sepday15, 'Sepday16': Sepday16,
        'Sepday17': Sepday17, 'Sepday18': Sepday18, 'Sepday19': Sepday19, 'Sepday20': Sepday20, 'Sepday21': Sepday21, 'Sepday22': Sepday22, 'Sepday23': Sepday23, 'Sepday24': Sepday24,
        'Sepday25': Sepday25, 'Sepday26': Sepday26, 'Sepday27': Sepday27, 'Sepday28': Sepday28, 'Sepday29': Sepday29, 'Sepday30': Sepday30,

        # OCTOBER 
        'Octday1': Octday1, 'Octday2': Octday2, 'Octday3': Octday3, 'Octday4': Octday4, 'Octday5': Octday5, 'Octday6': Octday6, 'Octday7': Octday7, 'Octday8': Octday8,
        'Octday9': Octday9, 'Octday10': Octday10, 'Octday11': Octday11, 'Octday12': Octday12, 'Octday13': Octday13, 'Octday14': Octday14, 'Octday15': Octday15, 'Octday16': Octday16,
        'Octday17': Octday17, 'Octday18': Octday18, 'Octday19': Octday19, 'Octday20': Octday20, 'Octday21': Octday21, 'Octday22': Octday22, 'Octday23': Octday23, 'Octday24': Octday24,
        'Octday25': Octday25, 'Octday26': Octday26, 'Octday27': Octday27, 'Octday28': Octday28, 'Octday29': Octday29, 'Octday30': Octday30, 'Octday31': Octday31,

        # NOVEMBER
        'Novday1': Novday1, 'Novday2': Novday2, 'Novday3': Novday3, 'Novday4': Novday4, 'Novday5': Novday5, 'Novday6': Novday6, 'Novday7': Novday7, 'Novday8': Novday8, 
        'Novday9': Novday9, 'Novday10': Novday10, 'Novday11': Novday11, 'Novday12': Novday12, 'Novday13': Novday13, 'Novday14': Novday14, 'Novday15': Novday15, 'Novday16': Novday16,
        'Novday17': Novday17, 'Novday18': Novday18, 'Novday19': Novday19, 'Novday20': Novday20, 'Novday21': Novday21, 'Novday22': Novday22, 'Novday23': Novday23, 'Novday24': Novday24,
        'Novday25': Novday25, 'Novday26': Novday26, 'Novday27': Novday27, 'Novday28': Novday28, 'Novday29': Novday29, 'Novday30': Novday30,

        # DECEMBER
        'Decday1': Decday1, 'Decday2': Decday2, 'Decday3': Decday3, 'Decday4': Decday4, 'Decday5': Decday5, 'Decday6': Decday6, 'Decday7': Decday7, 'Decday8': Decday8,
        'Decday9': Decday9, 'Decday10': Decday10, 'Decday11': Decday11, 'Decday12': Decday12, 'Decday13': Decday13, 'Decday14': Decday14, 'Decday15': Decday15, 'Decday16': Decday16,
        'Decday17': Decday17, 'Decday18': Decday18, 'Decday19': Decday19, 'Decday20': Decday20, 'Decday21': Decday21, 'Decday22': Decday22, 'Decday23': Decday23, 'Decday24': Decday24,
        'Decday25': Decday25, 'Decday26': Decday26, 'Decday27': Decday27, 'Decday28': Decday28, 'Decday29': Decday29, 'Decday30': Decday30, 'Decday31': Decday31,
    }

    return render(request, 'store/month.html', context)


@login_required
def Search(request):
    today = date.today()

    query = request.GET.get('query')

    if query != '' and query is not None:
        results = Item.objects.filter(Q(description__icontains=query)).filter(staff=request.user)
    else:
        raise Http404
    
    result = results

    context = {
        'results': result,
        'query': query
    }

    return render(request, 'store/search.html', context)


@login_required
def MonthlyCalculations(request):
    today = date.today()

    # MONTHLY CALCULATIONS FOR PURCHASED
    boughtJanuary = Item.objects.filter(type='-').filter(date__year=today.year, date__month=1).filter(staff=request.user)
    boughtFebruary = Item.objects.filter(type='-').filter(date__year=today.year, date__month=2).filter(staff=request.user)
    boughtMarch = Item.objects.filter(type='-').filter(date__year=today.year, date__month=3).filter(staff=request.user)
    boughtApril = Item.objects.filter(type='-').filter(date__year=today.year, date__month=4).filter(staff=request.user)
    boughtMay = Item.objects.filter(type='-').filter(date__year=today.year, date__month=5).filter(staff=request.user)
    boughtJune = Item.objects.filter(type='-').filter(date__year=today.year, date__month=6).filter(staff=request.user)
    boughtJuly = Item.objects.filter(type='-').filter(date__year=today.year, date__month=7).filter(staff=request.user)
    boughtAugust = Item.objects.filter(type='-').filter(date__year=today.year, date__month=8).filter(staff=request.user)
    boughtSeptember = Item.objects.filter(type='-').filter(date__year=today.year, date__month=9).filter(staff=request.user)
    boughtOctober = Item.objects.filter(type='-').filter(date__year=today.year, date__month=10).filter(staff=request.user)
    boughtNovember = Item.objects.filter(type='-').filter(date__year=today.year, date__month=11).filter(staff=request.user)
    boughtDecember = Item.objects.filter(type='-').filter(date__year=today.year, date__month=12).filter(staff=request.user)

    # MONTHLY CALCULATIONS FOR SOLD
    soldJanuary = Item.objects.filter(type='+').filter(date__year=today.year, date__month=1).filter(staff=request.user)
    soldFebruary = Item.objects.filter(type='+').filter(date__year=today.year, date__month=2).filter(staff=request.user)
    soldMarch = Item.objects.filter(type='+').filter(date__year=today.year, date__month=3).filter(staff=request.user)
    soldApril = Item.objects.filter(type='+').filter(date__year=today.year, date__month=4).filter(staff=request.user)
    soldMay = Item.objects.filter(type='+').filter(date__year=today.year, date__month=5).filter(staff=request.user)
    soldJune = Item.objects.filter(type='+').filter(date__year=today.year, date__month=6).filter(staff=request.user)
    soldJuly = Item.objects.filter(type='+').filter(date__year=today.year, date__month=7).filter(staff=request.user)
    soldAugust = Item.objects.filter(type='+').filter(date__year=today.year, date__month=8).filter(staff=request.user)
    soldSeptember = Item.objects.filter(type='+').filter(date__year=today.year, date__month=9).filter(staff=request.user)
    soldOctober = Item.objects.filter(type='+').filter(date__year=today.year, date__month=10).filter(staff=request.user)
    soldNovember = Item.objects.filter(type='+').filter(date__year=today.year, date__month=11).filter(staff=request.user)
    soldDecember = Item.objects.filter(type='+').filter(date__year=today.year, date__month=12).filter(staff=request.user)

    # MONTHLY CALCULATIONS FOR MISCELLANEOUS
    miscellaneousJanuary = Item.objects.filter(type='--').filter(date__year=today.year, date__month=1).filter(staff=request.user)
    miscellaneousFebruary = Item.objects.filter(type='--').filter(date__year=today.year, date__month=2).filter(staff=request.user)
    miscellaneousMarch = Item.objects.filter(type='--').filter(date__year=today.year, date__month=3).filter(staff=request.user)
    miscellaneousApril = Item.objects.filter(type='--').filter(date__year=today.year, date__month=4).filter(staff=request.user)
    miscellaneousMay = Item.objects.filter(type='--').filter(date__year=today.year, date__month=5).filter(staff=request.user)
    miscellaneousJune = Item.objects.filter(type='--').filter(date__year=today.year, date__month=6).filter(staff=request.user)
    miscellaneousJuly = Item.objects.filter(type='--').filter(date__year=today.year, date__month=7).filter(staff=request.user)
    miscellaneousAugust = Item.objects.filter(type='--').filter(date__year=today.year, date__month=8).filter(staff=request.user)
    miscellaneousSeptember = Item.objects.filter(type='--').filter(date__year=today.year, date__month=9).filter(staff=request.user)
    miscellaneousOctober = Item.objects.filter(type='--').filter(date__year=today.year, date__month=10).filter(staff=request.user)
    miscellaneousNovember = Item.objects.filter(type='--').filter(date__year=today.year, date__month=11).filter(staff=request.user)
    miscellaneousDecember = Item.objects.filter(type='--').filter(date__year=today.year, date__month=12).filter(staff=request.user)

    # Items' Monthly Price Calculations For Purchased
    boughtTotalJanuary = sum(item.value for item in boughtJanuary)
    boughtTotalFebruary = sum(item.value for item in boughtFebruary)
    boughtTotalMarch = sum(item.value for item in boughtMarch)
    boughtTotalApril = sum(item.value for item in boughtApril)
    boughtTotalMay = sum(item.value for item in boughtMay)
    boughtTotalJune = sum(item.value for item in boughtJune)
    boughtTotalJuly = sum(item.value for item in boughtJuly)
    boughtTotalAugust = sum(item.value for item in boughtAugust)
    boughtTotalSeptember = sum(item.value for item in boughtSeptember)
    boughtTotalOctober = sum(item.value for item in boughtOctober)
    boughtTotalNovember = sum(item.value for item in boughtNovember)
    boughtTotalDecember = sum(item.value for item in boughtDecember)

    # Items' Monthly Price Calculations For Sold
    soldTotalJanuary = sum(item.value for item in soldJanuary)
    soldTotalFebruary = sum(item.value for item in soldFebruary)
    soldTotalMarch = sum(item.value for item in soldMarch)
    soldTotalApril = sum(item.value for item in soldApril)
    soldTotalMay = sum(item.value for item in soldMay)
    soldTotalJune = sum(item.value for item in soldJune)
    soldTotalJuly = sum(item.value for item in soldJuly)
    soldTotalAugust = sum(item.value for item in soldAugust)
    soldTotalSeptember = sum(item.value for item in soldSeptember)
    soldTotalOctober = sum(item.value for item in soldOctober)
    soldTotalNovember = sum(item.value for item in soldNovember)
    soldTotalDecember = sum(item.value for item in soldDecember)

    # Items' Monthly Price Calculations For Miscellaneous
    miscellaneousTotalJanuary = sum(item.value for item in miscellaneousJanuary)
    miscellaneousTotalFebruary = sum(item.value for item in miscellaneousFebruary)
    miscellaneousTotalMarch = sum(item.value for item in miscellaneousMarch)
    miscellaneousTotalApril = sum(item.value for item in miscellaneousApril)
    miscellaneousTotalMay = sum(item.value for item in miscellaneousMay)
    miscellaneousTotalJune = sum(item.value for item in miscellaneousJune)
    miscellaneousTotalJuly = sum(item.value for item in miscellaneousJuly)
    miscellaneousTotalAugust = sum(item.value for item in miscellaneousAugust)
    miscellaneousTotalSeptember = sum(item.value for item in miscellaneousSeptember)
    miscellaneousTotalOctober = sum(item.value for item in miscellaneousOctober)
    miscellaneousTotalNovember = sum(item.value for item in miscellaneousNovember)
    miscellaneousTotalDecember = sum(item.value for item in miscellaneousDecember)

    # Monthly Sum Total
    monthlySumTotalJanuary = soldTotalJanuary - (boughtTotalJanuary + miscellaneousTotalJanuary)
    monthlySumTotalFebruary = soldTotalFebruary - (boughtTotalFebruary + miscellaneousTotalFebruary)
    monthlySumTotalMarch = soldTotalMarch - (boughtTotalMarch + miscellaneousTotalMarch)
    monthlySumTotalApril = soldTotalApril - (boughtTotalApril + miscellaneousTotalApril)
    monthlySumTotalMay = soldTotalMay - (boughtTotalMay + miscellaneousTotalMay)
    monthlySumTotalJune = soldTotalJune - (boughtTotalJune + miscellaneousTotalJune)
    monthlySumTotalJuly = soldTotalJuly - (boughtTotalJuly + miscellaneousTotalJuly)
    monthlySumTotalAugust = soldTotalAugust - (boughtTotalAugust + miscellaneousTotalAugust)
    monthlySumTotalSeptember = soldTotalSeptember - (boughtTotalSeptember + miscellaneousTotalSeptember)
    monthlySumTotalOctober = soldTotalOctober - (boughtTotalOctober + miscellaneousTotalOctober)
    monthlySumTotalNovember = soldTotalNovember - (boughtTotalNovember + miscellaneousTotalNovember)
    monthlySumTotalDecember = soldTotalDecember - (boughtTotalDecember + miscellaneousTotalDecember)

    context = {
        'date': today,
        
        # Items' Monthly Price Calculations For Purchased
        'boughtTotalJanuary': boughtTotalJanuary,
        'boughtTotalFebruary': boughtTotalFebruary,
        'boughtTotalMarch': boughtTotalMarch,
        'boughtTotalApril': boughtTotalApril,
        'boughtTotalMay': boughtTotalMay,
        'boughtTotalJune': boughtTotalJune,
        'boughtTotalJuly': boughtTotalJuly,
        'boughtTotalAugust': boughtTotalAugust,
        'boughtTotalSeptember': boughtTotalSeptember,
        'boughtTotalOctober': boughtTotalOctober,
        'boughtTotalNovember': boughtTotalNovember,
        'boughtTotalDecember': boughtTotalDecember,

        # Items' Monthly Price Calculations For Sold
        'soldTotalJanuary': soldTotalJanuary,
        'soldTotalFebruary': soldTotalFebruary,
        'soldTotalMarch': soldTotalMarch,
        'soldTotalApril': soldTotalApril,
        'soldTotalMay': soldTotalMay,
        'soldTotalJune': soldTotalJune,
        'soldTotalJuly': soldTotalJuly,
        'soldTotalAugust': soldTotalAugust,
        'soldTotalSeptember': soldTotalSeptember,
        'soldTotalOctober': soldTotalOctober,
        'soldTotalNovember': soldTotalNovember,
        'soldTotalDecember': soldTotalDecember,

        # Items' Monthly Price Calculations For Miscellaneous
        'miscellaneousTotalJanuary': miscellaneousTotalJanuary,
        'miscellaneousTotalFebruary': miscellaneousTotalFebruary,
        'miscellaneousTotalMarch': miscellaneousTotalMarch,
        'miscellaneousTotalApril': miscellaneousTotalApril,
        'miscellaneousTotalMay': miscellaneousTotalMay,
        'miscellaneousTotalJune': miscellaneousTotalJune,
        'miscellaneousTotalJuly': miscellaneousTotalJuly,
        'miscellaneousTotalAugust': miscellaneousTotalAugust,
        'miscellaneousTotalSeptember': miscellaneousTotalSeptember,
        'miscellaneousTotalOctober': miscellaneousTotalOctober,
        'miscellaneousTotalNovember': miscellaneousTotalNovember,
        'miscellaneousTotalDecember': miscellaneousTotalDecember,

        # Monthly Sum Total
        'monthlySumTotalJanuary': monthlySumTotalJanuary,
        'monthlySumTotalFebruary': monthlySumTotalFebruary,
        'monthlySumTotalMarch': monthlySumTotalMarch,
        'monthlySumTotalApril': monthlySumTotalApril,
        'monthlySumTotalMay': monthlySumTotalMay,
        'monthlySumTotalJune': monthlySumTotalJune,
        'monthlySumTotalJuly': monthlySumTotalJuly,
        'monthlySumTotalAugust': monthlySumTotalAugust,
        'monthlySumTotalSeptember': monthlySumTotalSeptember,
        'monthlySumTotalOctober': monthlySumTotalOctober,
        'monthlySumTotalNovember': monthlySumTotalNovember,
        'monthlySumTotalDecember': monthlySumTotalDecember,
    }

    return render(request, 'store/monthlycalc.html', context)
