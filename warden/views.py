from django.shortcuts import render

from login.models import Login
from warden.models import Warden
# Create your views here.

def add_warden(request):
    if request.method == "POST":
        obj=Warden()
        obj.name=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.email=request.POST.get('email')
        obj.gender=request.POST.get('gender')
        obj.address=request.POST.get('address')
        obj.phone=request.POST.get('phone')
        obj.status='pending'
        obj.save()
        # ob = Login()
        # ob.u_id = obj.w_id
        # ob.username = request.POST.get('email')
        # ob.password = request.POST.get('phone')
        # ob.type = 'warden'
        # ob.save()

        msg = "Successfully registered...!!!"
        context = {
            'msg': msg
        }
        return render(request, 'warden/add_warden.html', context)
    return render(request,'warden/add_warden.html')




def manage_warden(request):
    obj=Warden.objects.filter(status='pending')
    context={
        'obj':obj
    }
    return render(request,'warden/manage_warden.html',context)

def war_aprv(request,idd):
    ob=Warden.objects.get(w_id=idd)
    ob.status='approved'
    ob.save()
    obj = Login()
    obj.u_id = ob.w_id
    obj.username =ob.email
    obj.password =ob.phone
    obj.type = 'warden'
    obj.save()

    return manage_warden(request)

def wr_rjct(request,idd):
    ob=Warden.objects.get(w_id=idd)
    ob.status='rejected'
    ob.save()
    return manage_warden(request)