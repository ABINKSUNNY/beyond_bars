from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('foods/', views.view_foods, name='view_foods'),
    path('add-to-cart/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    # path('update/', views.update_cart, name='update_cart'),
    path('complete-payment/', views.complete_payment, name='complete_payment'),
     path('my-orders/', views.orders, name='view_orders'),
     path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('all_order/',views.admin_view_all_orders,name='allorder')
]
