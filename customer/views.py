from django.shortcuts import render,redirect
from django.shortcuts import redirect, get_object_or_404
from customer import models
from customer.models import Customer
from login.models import Login

# Create your views here.
def reg(request):
    if request.method == "POST":
        obj=Customer()
        obj.name=request.POST.get('name')
        obj.adress=request.POST.get('address')
        obj.email=request.POST.get('email')
        obj.phone=request.POST.get('phone')
        obj.gender=request.POST.get('gender')
        obj.status='pending'
        obj.password=request.POST.get('pass')
        obj.save()
        ob = Login()
        ob.u_id = obj.c_id
        ob.username = obj.email
        ob.password = obj.password
        ob.type = 'customer'
        ob.save()
        msg = "Successfully registered...!!!"
        context = {
            'msg': msg
        }
        return render(request, 'customer/reg.html', context)
    return render(request,'customer/reg.html')

def manage_reg(request):
    ob=Customer.objects.filter(status='pending')
    context={
        'obj':ob
    }
    return render(request,'customer/manage_reg.html',context)

# def approve(request,idd):
#     obj=Customer.objects.get(c_id=idd)
#     obj.status='approved'
#     obj.save()
#
#     return manage_reg(request)
#
# def reject(request,idd):
#     obj = Customer.objects.get(c_id=idd)
#     obj.status = 'rejected'
#     obj.save()
#     return manage_reg(request)
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, c_id=customer_id)
    customer.delete()
    return redirect('customer:manage')

    # return render(request,'customer/manage_reg.html')

def update_reg(request):
    aa=request.session["uid"]
    ob=Customer.objects.filter(c_id=aa)
    context={
        'obj':ob
    }
    return render(request,'customer/view_cus.html',context)

def update(request,idd):

    ob = Customer.objects.filter(c_id=idd)
    context = {
        'obj': ob
    }
    aa = request.session["uid"]
    if request.method == "POST":
        obj=Customer.objects.get(c_id=aa )
        obj.name=request.POST.get('name')
        obj.adress=request.POST.get('address')
        obj.email=request.POST.get('email')
        obj.phone=request.POST.get('phone')
        obj.gender=request.POST.get('gender')
        obj.status='pending'
        obj.password=request.POST.get('pass')
        obj.save()
    return render(request,'customer/update.html',context)


