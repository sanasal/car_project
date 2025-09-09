from django.contrib import admin
from .models import *
from django.contrib import messages

class CarImageZipAdmin(admin.ModelAdmin):
    list_display = ["car", "zip_file"]

    def save_model(self, request, obj, form, change):
        """Save model and notify user that extraction happens asynchronously."""
        super().save_model(request, obj, form, change)
        messages.success(request, "ZIP file uploaded. Images will be extracted soon.")

admin.site.register(Product)
admin.site.register(CarModel)
admin.site.register(Color)
admin.site.register(Manufacturer)
admin.site.register(CarImage)
admin.site.register(CarImageZip , CarImageZipAdmin)