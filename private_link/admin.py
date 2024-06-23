from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import PrvLink

class PrvLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'status', 'updt_date' ]


admin.site.register(PrvLink,PrvLinkAdmin)