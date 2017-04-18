from django.contrib import admin
from .models import Profile

# class ProfileAdmin(admin.ModelAdmin):
# 	list_display=['pk','user','address','job_title']

admin.site.register(Profile)

# Register your models here.
