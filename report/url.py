from django.urls import path
from . import views

urlpatterns=[
    path('generate-report/',views.generate_daily_purchase_report, name='generate_report'),
    path('manage_report/',views.manage_report,name='manage_report'),
    path('rejct/<str:idd>/', views.rjct, name='rejct'),
    path('aprv/<str:idd>/', views.aprv, name='aprv'),
    path('download-report/<int:rid>/', views.download_report, name='download_report'),
    path('view-report/', views.view_report, name='view_report'),
    # path('add_report/',views.add_report,name='add_report'),
# path('view_report/',views.view_report,name='view_report'),
    # path('download/', views.download_report, name='download_report'),
    # path('upload/',views.upload_daily_report, name='upload_daily_report'),
    # path('purchase-report/', views.purchase_report, name='purchase_report'),
    # path('purchase-report/<str:report_date>/', views.purchase_report_detail, name='purchase_report_detail'),
]