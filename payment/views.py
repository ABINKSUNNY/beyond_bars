from datetime import datetime

from django.shortcuts import render
from cart.models import Purchase
from payment.models import *
# Create your views here.
def add_pay(request):
    if request.method == "POST":
        obj=Payment()
        obj.price=request.POST.get('amount')
        obj.date = datetime.today()
        obj.time = datetime.today()
        obj.c_id=1
        obj.save()
    return render(request,'payment/add_payment.html')

def view_pay(request):
    obj = Purchase.objects.all()
    context = {
        'ob': obj
    }
    return render(request,'payment/view_pay.html',context)

def view_padwar(request):
    obj = Purchase.objects.all()
    context = {
        'ob': obj
    }
    return render(request,'payment/view_pay_admin.html',context)

