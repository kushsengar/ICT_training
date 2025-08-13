# from django.contrib import admin
# from .models import Product

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price', 'discount', 'get_discounted_price']
#     search_fields = ['name']
#     list_editable = ['price', 'discount']
#     list_filter = ['discount']

#     def get_discounted_price(self, obj):
#         return obj.discounted_price()
#     get_discounted_price.short_description = 'Discounted Price'
