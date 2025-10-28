from django.urls import path
from . import views

urlpatterns=[
    path('payment/',views.add_pay,name='payment'),
    path('view_pay/',views.view_pay,name='view_pay'),
    path('view_pay_war/',views.view_padwar,name='view_pay_war'),
]