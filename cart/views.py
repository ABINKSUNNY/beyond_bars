import razorpay
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Food, CartItem, Purchase
from customer.models import Customer
from django.db.models import Q

razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))



# def orders(request):
#     customer_id = request.session.get('customer_id')
#
#     # if not customer_id:
#     #     return redirect('login')  # redirect if not logged in
#
#     orders = Purchase.objects.filter(customer_id=customer_id).order_by('-timestamp')
#     context = {
#         'orders': orders
#     }
#     return render(request, 'cart/view_order.html', context)



def admin_view_all_orders(request):
    orders = Purchase.objects.all().order_by('-timestamp')
    context = {
        'orders': orders
    }
    return render(request, 'cart/view_allorder.html', context)

def get_customer_and_session(request):
    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key
    customer_id = request.session.get("uid")
    customer = Customer.objects.filter(c_id=customer_id).first() if customer_id else None
    return customer, session_key

def view_foods(request):
    query = request.GET.get('q')
    if query:
        foods = Food.objects.filter(name__icontains=query)
    else:
        foods = Food.objects.all()
    return render(request, 'cart/view_food.html', {'foods': foods})

def add_to_cart(request, food_id):
    customer, session_key = get_customer_and_session(request)
    food = get_object_or_404(Food, id=food_id)
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = CartItem.objects.get_or_create(
        customer=customer, session_key=session_key, food=food
    )
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    return redirect('cart')


def cart(request):
    customer, session_key = get_customer_and_session(request)
    cart_items = CartItem.objects.filter(customer=customer, session_key=session_key)

    total = sum(item.get_total_price() for item in cart_items)

    razorpay_order = None
    if total > 0:
        razorpay_order = razorpay_client.order.create({
            'amount': int(total * 100),  # Razorpay uses paise
            'currency': 'INR',
            'payment_capture': '1'
        })
        request.session['razorpay_order_id'] = razorpay_order['id']

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'razorpay_order_id': razorpay_order['id'] if razorpay_order else None,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'amount_paise': int(total * 100),
        'customer': customer
    })

@csrf_exempt
def complete_payment(request):
    if request.method == 'POST':
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.session.get('razorpay_order_id')
        customer, session_key = get_customer_and_session(request)
        cart_items = CartItem.objects.filter(customer=customer, session_key=session_key)
        total = sum(item.get_total_price() for item in cart_items)

        for item in cart_items:
            Purchase.objects.create(
                customer=customer,
                food=item.food,
                quantity=item.quantity,
                price=item.food.price,
                payment_id=payment_id,
                order_id=order_id,
                total_amount=total
            )

        cart_items.delete()
        return render(request, 'cart/order_success.html', {'order_id': order_id, 'total': total})
    return redirect('cart')


def orders(request):
    customer_id = request.session.get('customer_id') or request.session.get('uid')  # adapt to your session key

    # if not customer_id:
    #     return redirect('/login/login/')  # update to your actual login URL if different

    orders = Purchase.objects.filter(customer_id=customer_id).order_by('-timestamp')

    context = {
        'orders': orders
    }
    return render(request, 'cart/view_order.html', context)



def cancel_order(request, order_id):
    order = get_object_or_404(Purchase, order_id)
    order.delete()
    return redirect('view_orders')