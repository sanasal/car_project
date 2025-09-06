from django.urls import path
from . import views

urlpatterns = [
    path('country/',view=views.country),
    path('country/<uuid:id>/',views.country),
    path('country/create/',view=views.country),
    path('country/<uuid:id>/update',views.country),
    path('country/<uuid:id>/delete',views.country),
    path('user/',view=views.user),
    path('user/login',view=views.login),
    path('user/<uuid:id>/',views.user),
    path('user/create/',view=views.user),
    path('user/<uuid:id>/update',views.user),
    path('user/<uuid:id>/delete',views.user),
    path('userinfo/',view=views.userinfo),
    path('userinfo/<uuid:id>/',views.userinfo),
    path('userinfo/create/',view=views.userinfo),
    path('userinfo/<uuid:id>/update',views.userinfo),
    path('userinfo/<uuid:id>/delete',views.userinfo),
    path('review/',view=views.review),
    path('review/<uuid:id>/',views.review),
    path('review/create/',view=views.review),
    path('review/<uuid:id>/update',views.review),
    path('review/<uuid:id>/delete',views.review)
]