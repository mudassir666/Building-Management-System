from django.contrib import admin
from .models import Buildings, BuildingUsers, Levels, Units, Members

# Register your models here.
admin.site.register(Buildings)
admin.site.register(BuildingUsers)
admin.site.register(Levels)
admin.site.register(Units)
admin.site.register(Members)