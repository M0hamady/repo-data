from django.contrib import admin

# Register your models here.
from .models import  *
admin.site.register(Project)
admin.site.register(Step)
admin.site.register(Images_step)
admin.site.register(Moshtarayet)
