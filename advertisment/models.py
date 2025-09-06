import uuid
from django.db import models
from product.models import Product
class Advertisment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    created_at=models.DateTimeField(
        auto_now_add=True,
        verbose_name='order_time'

        )
    updated_at=models.DateTimeField(
        auto_now=True
     )
    is_deleted=models.BooleanField(
        default=False
        )
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    img=models.ImageField(
        max_length=500,
        null= True,
        default= None
        )
    class Meta:
        db_table = 'advertisment'
        verbose_name = 'advertisment'
        verbose_name_plural = 'advertisments'