from django.contrib import admin
from .models import User, Category, Dish, Item

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Dish)
