""" Admin for 'products' app"""
from django.contrib import admin
from .models import Product, Category, Review, Wishlist


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'brand',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_title', 'review', 'review_author', 'product')


admin.site.register(Review, ReviewAdmin)

admin.site.register(Wishlist)
