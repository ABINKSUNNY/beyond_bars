"""
URL configuration for beyond_bar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from temp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.url')),
    path('customer/', include('customer.url')),
    path('feedback/', include('feedback.url')),
    path('food/', include('food.url')),
    path('login/', include('login.url')),
    path('payment/', include('payment.url')),
    path('purchase/', include('purchase.url')),
    path('report/', include('report.url')),
    path('stock/', include('stock.url')),
    path('superintendent/', include('superintendent.url')),
    path('warden/', include('warden.url')),
    path('temp/', include('temp.url')),
    path('',views.index),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)