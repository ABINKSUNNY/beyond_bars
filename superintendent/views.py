from django.shortcuts import render
from superintendent import models
from superintendent.models import Superindentent
from login.models import Login

# Create your views here.
def manage_super(request):
    ob=Superindentent.objects.filter(status='pending')
    context = {
        'ob':ob
    }
    return render(request,'superintedent/manage_suprnt.html',context)
def aprved(request,idd):
    ob=Superindentent.objects.get(s_id=idd)
    ob.status='approved'
    ob.save()
    return manage_super(request)
def rjct(request,idd):
    ob=Superindentent.objects.get(s_id=idd)
    ob.status='rejected'
    ob.save()
    return manage_super(request)


def reg(request):
    if request.method == 'POST':
        obj=Superindentent()
        obj.name=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.email=request.POST.get('email')
        obj.phone=request.POST.get('contact')
        obj.address=request.POST.get('address')
        obj.gender=request.POST.get('gender')
        obj.status='pending'
        obj.save()
        ob = Login()
        ob.u_id = obj.s_id
        ob.username = request.POST.get('email')
        ob.password = request.POST.get('contact')
        ob.type = 'superindentent'
        ob.save()

        msg = "Successfully registered...!!!"
        context = {
            'msg': msg
        }
        return render(request, 'superintedent/reg.html', context)
    return render(request,'superintedent/reg.html')
