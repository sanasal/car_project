from django import views
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static      
from django.conf import settings    
from . import views      

app_name='frontend'

urlpatterns = [          
    path('' , views.home , name='home'),    
    path('about/' , views.about ,name='about'),
    path('services/' , views.service , name='service' ),
    path('contact_us/' , views.contact_us , name='contact'),
    path('financing/' , views.financing ,name='financing'),
    path('FAQs & Help/' , views.FAQs , name='FAQs' ),
    path('testimonial/' , views.testimonial, name='testimonial'),
    path('team/' , views.team ,name='team'),
    path('car details/' , views.car_detail , name='car_details' ),
    path('contact_us/' , views.contact_us , name='contact_us'),
    path('cars_inventory/' , views.cars ,name='cars'),
]