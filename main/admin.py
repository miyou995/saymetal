from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Product, Reference
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category', 'active', 'date_added')
    list_display_links = ('id', 'name')
    list_display_links = ('id','name',)
    list_per_page = 40
    list_editable = ['active']
    list_filter = ('name',)
    readonly_fields = ('date_added',)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('id', 'name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Reference)
admin.site.unregister(User)
admin.site.unregister(Group)