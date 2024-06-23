from django.contrib import admin

from .models import Portal,Webtoon


# Register your models here.
class PortalAdmin(admin.ModelAdmin):
    list_display = ['name', 'search_form', 'list_webtoon', 'contents_webtoon','main_url','etc', 'updt_date']

class WebtoonAdmin(admin.ModelAdmin):
    list_display = ['portal', 'title', 'today_title', 'title_id','lastno','dates', 'status']

admin.site.register(Portal,PortalAdmin)
admin.site.register(Webtoon,WebtoonAdmin)