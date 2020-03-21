from django.contrib import admin

# Register your models here.
from .models import Password,PasswordHeader

class PasswordHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'hint', 'special_letter', 'updt_date' ]

class PasswordAdmin(admin.ModelAdmin):
    list_display = ['site', 'pheader', 'ptail', 'updt_date' ]

admin.site.register(PasswordHeader,PasswordHeaderAdmin)
admin.site.register(Password,PasswordAdmin)
