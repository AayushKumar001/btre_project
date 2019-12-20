from django.contrib import admin
from . import models
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_mvp','email','hire_date')
    list_display_links = ('id','name',)
    search_fields = ('name',)
    list_per_page = 25
    list_editable = ('is_mvp',)
admin.site.register(models.Realtor,RealtorAdmin)
