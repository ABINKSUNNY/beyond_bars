from django.urls import path
from  superintendent import views

urlpatterns=[
    path('manage_su/',views.manage_super,name='manage_warden'),
    path('reg/',views.reg,name='reg'),
    path('aprved/<str:idd>/', views.aprved, name='aprved'),
    path('rejctt/<str:idd>/', views.rjct, name='rejctt'),
]
