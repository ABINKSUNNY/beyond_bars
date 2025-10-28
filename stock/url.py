from django.urls import path
from . import views

urlpatterns=[
    # path('stock/',views.stock,name='stock'),
    path('manage_stock/',views.manage_stock,name='manage_stock'),
    path('st_ap/<int:idd>/w/', views.st_aprved, name='st_ap'),
    path('st_rej/<int:idd>/w/', views.st_rjct, name='st_rej'),
    # path('update_stock/',views.update_stock,name='update_stock'),
    # path('stock/<int:idd>/w/',views.stock,name='stock'),
    path('update_stockk/', views.update_stock, name='update_stock'),
]

