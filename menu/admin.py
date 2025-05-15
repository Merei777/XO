from django.contrib import admin
from .models import Category, SubCategory, Dish

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_subcategory', 'price', 'is_available')
    list_filter = ('subcategory__name', 'is_available')
    search_fields = ('name', 'subcategory__name')

    def get_subcategory(self, obj):
        return obj.subcategory.name
    get_subcategory.short_description = 'Подкатегория'
