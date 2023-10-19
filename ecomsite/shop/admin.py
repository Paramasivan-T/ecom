from django.contrib import admin
from .models import Product, Order

admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "World Bucket"
admin.site.index_title = "Manage Shopping" 


class ProductAdmin(admin.ModelAdmin):

    def change_category(self,request, queryset):
        queryset.update(category="default")


    list_display = ('title', 'price', 'discount_price', 'category', 'description')
    search_fields = ('title','price', 'discount_price', 'category', 'description')
    actions = (change_category,)
    list_editable = ('price',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)