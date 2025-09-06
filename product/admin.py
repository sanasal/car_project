from django.contrib import admin
from .models import Product
from .models import CarModel
from .models import Color
admin.site.register(Product)
admin.site.register(CarModel)
admin.site.register(Color)