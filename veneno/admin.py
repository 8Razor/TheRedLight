from django.contrib import admin
from .models import Person, Car, Manufacturer


admin.site.register(Person)
admin.site.register(Manufacturer)
admin.site.register(Car)
