from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, dashb

admin.site.register(Blog)

# admin.site.register(dashb)

@admin.register(dashb)
class dashbAdmin(admin.ModelAdmin):
    pass 
