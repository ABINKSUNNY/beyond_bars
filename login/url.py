from django. urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('login/',views.login,name='login'),
     path('forgot-password/', views.forgot_password_request, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
     # path('reset-password/', views.reset_password, name='reset_password'),

]