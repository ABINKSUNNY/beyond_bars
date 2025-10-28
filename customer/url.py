from django.urls import path
from . import views
app_name='customer'
urlpatterns=[
    path('reg/',views.reg,name='reg'),
    path('manage_reg/',views.manage_reg,name='manage'),
    path('delete-customer/<int:customer_id>/', views.delete_customer,name='delete_customer'),
    # path('approve/<str:idd>/', views.approve, name='approved'),
    path('view_cus/',views.update_reg,name='up_view'),
   path('update/<str:idd>/',views.update,name='update'),

]