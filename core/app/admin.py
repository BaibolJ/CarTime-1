from django.contrib import admin
from .models import *

admin.site.register(Car)
admin.site.register(ImgFile)
admin.site.register(Category)
admin.site.register(BrandCars)
admin.site.register(Rental)

