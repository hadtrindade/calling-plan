from django.contrib import admin
from .models import Militares, SubUnidade, PostoGraduacao, Area

# Register your models here.
admin.site.register(Militares)
admin.site.register(SubUnidade)
admin.site.register(PostoGraduacao)
admin.site.register(Area)
