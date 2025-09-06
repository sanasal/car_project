import uuid
from django.db import models
class Manufacturer(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at=models.DateTimeField(
        auto_now_add=True
        )
    updated_at=models.DateTimeField(
        auto_now=True
     )
    is_deleted=models.BooleanField(
        default=False
        )
class CarModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        null=True,
        default= None,
        related_name= 'carmodels',
        related_query_name= 'carmodel'
  )
    name = models.CharField(max_length=255)
    model_date = models.DateField()
    created_at=models.DateTimeField(
        auto_now_add=True
        )
    specs = models.TextField(
        blank=True
    )
    img=models.ImageField(
        null=True,
        upload_to='imgs/carModel',
        max_length=500
    )
    updated_at=models.DateTimeField(
        auto_now=True
     )
    is_deleted=models.BooleanField(
        default=False
        )
    class Meta:
        db_table = 'model'
        verbose_name = 'model'
        verbose_name_plural = 'models'

class Color(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=255)
    created_at=models.DateTimeField(
        auto_now_add=True
        )
    red_value=models.IntegerField(default=0)
    green_value=models.IntegerField(default=0)
    blue_value=models.IntegerField(default=0)
    updated_at=models.DateTimeField(
        auto_now=True
     )
    is_deleted=models.BooleanField(
        default=False
        )
    class Meta:
        db_table = 'color'
        verbose_name = 'color'
        verbose_name_plural = 'colors'

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    license_plate = models.CharField(max_length=30)
    color = models.ForeignKey(
        Color,
        on_delete=models.SET_NULL,
        null=True
    )
    features = models.TextField(blank=True)
    is_new=models.BooleanField(default=True)
    current_kilometer = models.IntegerField(default=0)
    created_at=models.DateTimeField(
        auto_now_add=True
        )
    engine = models.IntegerField(null =True)

    updated_at=models.DateTimeField(
        auto_now=True
     )
    is_deleted=models.BooleanField(
        default=False
        )
    carModel = models.ForeignKey(
        CarModel,
        on_delete=models.SET_NULL,
        null=True,
        default= None,
        related_name= 'products',
        related_query_name= 'product'
  )
    price=models.DecimalField(decimal_places=5,
    max_digits=7
        )
    is_sold=models.BooleanField(default=False)
    img=models.ImageField(
        upload_to='imgs/product',
        max_length=500,
        null= True,
        default= None
        )
    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'        