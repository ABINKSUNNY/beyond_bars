from django.urls import path
from temp import views
app_name='temp'
urlpatterns = [
path('index/',views.index,name='index'),
path('customer_home/',views.cust_home,name='customer_home'),
path('warden_home/',views.warden_home,name='warden_home'),
path('super_home/',views.sup_home,name='super_home'),
path('admin_home/',views.admin,name='admin_home'),
]