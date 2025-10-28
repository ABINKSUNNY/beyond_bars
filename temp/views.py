from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'temp/index.html')

def warden_home(request):
    return render(request,'temp/warden.html')

def sup_home(request):
    return render(request,'temp/suprt.html')

def cust_home(request):
    return render(request,'temp/customer.html')

def admin(request):
    return render(request,'temp/admin.html')
