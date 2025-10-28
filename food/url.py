from django.urls import path
from . import views


urlpatterns=[
    path('add_food/', views.add_food, name='add_food'),
    path('view_food/',views.view_food,name='view_food'),
    path('admin_view/',views.admin_food,name='admin_view'),
# path('fd_rej/<int:idd>/w/', views.fd_rjct, name='fd_rej'),
]

