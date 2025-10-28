from django.urls import path
from . import views

urlpatterns=[
    path('add_feed/',views.add_feedback,name='add_feed'),

    path('view_feed/',views.view_feedback,name='view_feed'),

    path('sup_view/',views.view_fee_s,name='sup_view'),
]