from django.contrib import admin

from .models import Area, Graduation, Military, SubUnit

# Register your models here.
admin.site.register(Military)
admin.site.register(SubUnit)
admin.site.register(Graduation)
admin.site.register(Area)
