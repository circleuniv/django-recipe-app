from django.contrib import admin
from .models import MenuItems


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('meal','status')
    list_filter = ('status',)
    search_fields = ('meal','description')


admin.site.register(MenuItems,MenuItemAdmin)
