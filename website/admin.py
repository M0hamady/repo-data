from django.contrib import admin
from .models import Websiteindex, Montagat

# Register your models here.
admin.site.register(Websiteindex)
@admin.register(Montagat)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "qesm")

