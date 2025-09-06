from django.contrib import admin
from .models import Payment
from .models import Currency
admin.site.register(Payment)
admin.site.register(Currency)