from django.shortcuts import render,redirect
# from food.models import *
# from .models import Food
# from cart.models import Cart
from datetime import datetime
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.shortcuts import render, redirect
from cart.models import Food
from django.contrib import messages

# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
# from .models import Food

def add_food(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        quantity = request.POST.get('quantity')
        stock = request.POST.get('stock')

        Food.objects.create(
            name=name,
            category=category,
            price=price,
            description=description,
            image=image,
            quantity=quantity,
            stock=stock
        )
        messages.success(request, "new item added successfully!")
        return redirect('add_food')

    return render(request, 'cart/add_food.html')

def view_food(request):
    obj=Food.objects.all()
    context = {
        'food': obj
    }

    return render(request,'food/view_food.html',context)

def admin_food(request):
    obj = Food.objects.all()
    context = {
        'obb': obj
    }
    return render(request,'food/admin_viewfood.html',context)


# def fd_rjct(request,idd):
#     ob=Food.objects.get(id=idd)
#     ob.save()
#     return admin_food(request)