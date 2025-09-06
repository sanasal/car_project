from django.contrib import admin
from .models import User
from .models import Userinfo
from .models import Review
from .models import Country
admin.site.register(User)
admin.site.register(Userinfo)
admin.site.register(Review)
admin.site.register(Country)
