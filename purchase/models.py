import uuid
from django.db import models
from product.models import Product
from user.models import User
class Purchase(models.Model):
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
    is_payment_done=models.BooleanField(default=False)
    user=models.ForeignKey(
        User,on_delete=models.CASCADE
    )
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.DecimalField(decimal_places=5,
    max_digits=7
        ) 
    class Meta:
        db_table = 'purchase'
        verbose_name = 'purchase'
        verbose_name_plural = 'purchases'