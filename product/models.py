import uuid
from django.db import models
import os
import zipfile
from django.core.files.base import ContentFile
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
    model_date = models.PositiveIntegerField(null=True)
    created_at=models.DateTimeField(
        auto_now_add=True
        )
    specs = models.TextField(
        blank=True
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
    updated_at=models.DateTimeField(
        auto_now=True
     )
    is_deleted=models.BooleanField(
        default=False
        )
    
    def __str__(self):
        return self.name
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


class CarImage(models.Model):
    car = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="car_images/" , null=True)

    def __str__(self):
        return f"{self.car.carModel.manufacturer.name} {self.car.carModel.name}"


class CarImageZip(models.Model):
    car = models.ForeignKey(Product, on_delete=models.CASCADE , related_name="zip_files")
    zip_file = models.FileField(upload_to="car_zips/" , null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # أول شي نخزن الملف
        self.extract_images()

    def extract_images(self):
        if not self.zip_file:
            return

        zip_path = self.zip_file.path
        if not os.path.exists(zip_path):
            print(f"ZIP file does NOT exist: {zip_path}")
            return

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            for filename in zip_ref.namelist():
                if filename.endswith((".jpg", ".jpeg", ".png")):
                    # تنظيف الاسم من المجلدات (بعض الـ ZIP بيكون فيه مسارات مثل folder/image.png)
                    clean_name = os.path.basename(filename)
                    if not clean_name:  # إذا كان اسم فارغ (مجلد) نطنش
                        continue

                    img_data = zip_ref.read(filename)

                    new_image = CarImage(car=self.car)
                    new_image.image.save(clean_name, ContentFile(img_data), save=True)
                    print(f"✅ Extracted and saved: {clean_name}") 

