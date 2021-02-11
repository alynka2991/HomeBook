from django.db import models


# Модель Measure - единицы измерения продуктов
class Measure(models.Model):
    # Поле measure_name - наименование единицы измерения
    measure_name = models.CharField(max_length=50, null=False, blank=False, unique=True, help_text="Единица измерения")
    # Поле short_measure_name - короткое наименование поля
    short_measure_name = models.CharField(max_length=10, null=True, blank=True, unique=True, default=measure_name,
                                          help_text="Короткое наименование единицы измерения")


# Модель Category - Категории продуктов
class Category(models.Model):
    # Поле category_name - наименование категории продукта
    category_name = models.CharField(max_length=50, null=False, blank=False, unique=True, help_text="Категория")
    # Поле category_description - описание категории продукта
    category_description = models.TextField(null=True, blank=True, unique=True, help_text="Описание категории")
