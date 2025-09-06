from django.urls import path
from . import views

urlpatterns = [
    path('currency/',view=views.currency),
    path('currency/<uuid:id>/',views.currency),
    path('currency/create/',view=views.currency),
    path('currency/<uuid:id>/update',views.currency),
    path('currency/<uuid:id>/delete',views.currency),
    path('payment/',view=views.payment),
    path('payment/<uuid:id>/',views.payment),
    path('payment/create/',view=views.payment),
    path('payment/<uuid:id>/update',views.payment),
    path('payment/<uuid:id>/delete',views.payment)

]