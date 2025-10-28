
# Create your views here.
from datetime import datetime
from django.shortcuts import render, redirect
from feedback.models import Feedback
from customer.models import Customer
from django.utils import timezone
# import the Customer model

def add_feedback(request):
    if request.method == "POST":
        cc = request.session.get("uid")
        if not cc:
            return redirect('login')

        try:
            customer = Customer.objects.get(c_id=cc)
        except Customer.DoesNotExist:
            return redirect('login')

        description = request.POST.get('description')
        if not description:
            return render(request, 'feedback/add_feedback.html', {'error': 'Feedback cannot be empty.'})

        Feedback.objects.create(
            customer=customer,
            feedback=description,
            date=timezone.now().date(),
            time=timezone.now().time()
        )

        return render(request, 'feedback/add_feedback.html', {'message': 'Thank you for your feedback!'})

    return render(request, 'feedback/add_feedback.html')

def view_feedback(request):
    x = Feedback.objects.all().order_by('-date', '-time')  # optional ordering
    return render(request, 'feedback/view_feedbck.html', {'x': x})

def view_fee_s(request):
    x = Feedback.objects.all().order_by('-date', '-time')  # optional ordering
    return render(request, 'feedback/view_fee_sup.html', {'x': x})
