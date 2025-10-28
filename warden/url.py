from django.urls import path
from . import views

urlpatterns=[
    # path('add_warden/',views.add_warden,name='add_warden'),
    path('warden/',views.add_warden),
    path('manage_warden/',views.manage_warden,name='manage_warden'),
    path('war_ap/<int:idd>/w/', views.war_aprv, name='war_ap'),
    path('war_rej/<int:idd>/w/', views.wr_rjct, name='war_rej'),
]