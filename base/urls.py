from django.urls import path
from . import views

urlpatterns=[
   path('', views.home,name="home"),
   path('over_due_bills/', views.overDueBillsList,name="over_due_bills"),
   path('bill/<str:pk>/', views.bill ,name="bill"),
   path('bill_form/', views.createBill ,name="bill_form"),
   path('update_bill/<str:pk>/', views.updateBill ,name="update_bill"),
   path('latest_payments/', views.latestPayments ,name="latest_payments")
]