from django.contrib import admin
from .models import post
# Register your models here.
class posttime(admin.ModelAdmin):
	list_display = ['title' , 'publishing_date']
admin.site.register(post ,posttime )