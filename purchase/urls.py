from django.urls import path
from . import views

urlpatterns = [
    path('purchase/',view=views.purchase),
    path('purchase/<uuid:id>/',views.purchase),
    path('purchase/create/',view=views.purchase),
    path('purchase/<uuid:id>/update',views.purchase),
    path('purchase/<uuid:id>/delete',views.purchase),
]