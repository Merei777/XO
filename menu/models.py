from django.db import models

# 1. Основная категория блюд
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания категории

    def __str__(self):
        return self.name

# 2. Подкатегория для разделения блюд внутри категории (например, горячие, холодные закуски)
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)  # для сортировки подкатегорий
    is_active = models.BooleanField(default=True)  # возможность деактивации подкатегории

    def __str__(self):
        return f"{self.category.name} - {self.name}"

# 3. Модель блюда, привязанная к подкатегории
class Dish(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='dishes/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 4. Модель ингредиента, используемого в блюдах
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    allergens = models.CharField(max_length=255, blank=True, help_text="Укажите возможные аллергены")
    is_organic = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# 5. Промежуточная модель для связи блюда и ингредиента, с указанием количества
class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_dishes')
    quantity = models.CharField(max_length=50, blank=True, help_text="Например, '200 г', '1 шт.'")

    def __str__(self):
        return f"{self.dish.name} - {self.ingredient.name}"
