from datetime import datetime
from cart.models import  Food
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Stock

def update_stock(request):
    foods = Food.objects.all()

    if request.method == 'POST':
        for food in foods:
            stock_value = request.POST.get(f'stock_{food.id}')
            if stock_value and stock_value.isdigit():
                new_stock = int(stock_value)


                Stock.objects.create(
                    food=food,
                    stock=food.stock,
                    quandity=food.quantity,  # or use difference/new amount as needed
                    price=food.price,
                    status='Updated',
                    date=timezone.now().date(),
                    time=timezone.now().time()
                )

                # Update the Food stock value
                food.stock = new_stock
                food.save()

        return redirect('update_stock')

    return render(request, 'stock/stock_update.html', {'foods': foods})



def manage_stock(request):
    obj = Stock.objects.all()
    context = {
        'abb': obj
    }
    return render(request,'stock/manage_stock.html',context)


def st_aprved(request,idd):
    ob=Stock.objects.get(st_id=idd)
    ob.status='approved'
    ob.save()
    return manage_stock(request)

def st_rjct(request,idd):
    ob=Stock.objects.get(st_id=idd)
    ob.status='rejected'
    ob.save()
    return manage_stock(request)