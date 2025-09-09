from django.db import models

# Create your models here.
class RequestsData(models.Model):
    car = models.TextField(default='', blank=True) 
    name = models.TextField(max_length=300, default='', blank=True)
    mobile_phone = models.TextField(blank=True, default='')
    Cash = 'Cash'
    Bank_Financing = 'Bank-Financing'

    PAYMENT_METHODS = [
        (Cash, 'Cash'),
        (Bank_Financing, 'Bank-Financing'),
    ]

    Arabic = 'Arabic'
    English = 'English'

    LANGUAGE = [
        (Arabic , 'Arabic'),
        (English , 'English')
    ]

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, blank=True)
    language = models.CharField(max_length=20 , choices=LANGUAGE , blank=True)
    created_at = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return f"cars:{self.car} - name:{self.name}"
    

class ContactData(models.Model):
    name = models.TextField(max_length=300, default='', blank=True)
    subject = models.TextField(blank=True, default='')
    email = models.EmailField(blank=True, default='')
    message = models.TextField(max_length=500, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True , null=True)