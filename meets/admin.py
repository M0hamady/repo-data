from django.contrib import admin

# Register your models here.
from meets.models import Meeting

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    fields = ("bartment_space", "last_ip", "location",'created_by')