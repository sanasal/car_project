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
    path('send_financing_request/', views.send_financing_request_data, name='send_f_request_data'),
    path('FAQs & Help/' , views.FAQs , name='FAQs' ),
    path('testimonial/' , views.testimonial, name='testimonial'),
    path('team/' , views.team ,name='team'),
    path('car details/<uuid:car_id>/' , views.car_detail , name='car_details' ),
    path('contact_us/' , views.contact_us , name='contact_us'),
    path('send_contact/', views.send_contact ,name='send_contact' ),
    path('cars_inventory/' , views.cars ,name='cars'),
    path('cars-filter/', views.cars_filter_view, name='cars-filter'),
    path('log_in/' , views.log_in , name='log_in'),
    path('sign_in/' , views.sign_in , name='sign_in'), 
    path('log_out/' , views.log_out , name='log_out'),  
]