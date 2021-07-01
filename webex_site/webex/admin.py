from django.contrib import admin

# Register your models here.
from .models import *

class WebexAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'time_create', 'is_published', 'discount', 'left')
    # list_display_links = ('name')
    search_fields = ('name', 'category')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'price', 'category')
    # prepopulated_fields = {"slug": ("title",)}


admin.site.register(Product, WebexAdmin)
admin.site.register(Category)
admin.site.register(Users)
admin.site.register(Order)
admin.site.register(order_product)