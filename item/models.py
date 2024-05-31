from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering=('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True, null = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name="items")
    created_at = models.DateTimeField(auto_now_add = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    is_sold = models.BooleanField(default = False)
    image = models.ImageField(upload_to = 'item-images', blank = True, null = True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name="items")
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'items'

    def __str__(self):
        return self.name





