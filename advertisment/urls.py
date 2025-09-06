from django.urls import path
from . import views

urlpatterns = [
    path('advertisment/',view=views.advertisment),
    path('advertisment/<uuid:id>/',views.advertisment),
    path('advertisment/create/',view=views.advertisment),
    path('advertisment/<uuid:id>/update',views.advertisment),
    path('advertisment/<uuid:id>/delete',views.advertisment),
]