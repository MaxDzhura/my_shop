import uuid
import os
from django.db import models
from django.core.validators import RegexValidator


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)


class Dish(models.Model):

    def get_file_name(self, filename):
        ext_file = filename.strip().split(',')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('dishes/', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=500, blank=True)
    ingredients = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    special = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} '

    class Meta:
        ordering = ('position', 'price',)
        index_together = (('id', 'slug'),)


class Events(models.Model):

    def get_file_name(self, filename):
        ext_file = filename.strip().split(',')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('events/', new_filename)


    name = models.CharField(unique=True, max_length=100, db_index=True)
    description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to=get_file_name)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    data_time = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('name',)


class Special(models.Model):

    def get_file_name(self, filename):
        ext_file = filename.strip().split(',')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('special/', new_filename)

    name = models.CharField(unique=True, max_length=100, db_index=True)
    description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('name',)


class About(models.Model):

    name = models.CharField(unique=True, max_length=200, db_index=True)
    description = models.TextField(max_length=600, blank=True)
    video = models.URLField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('name',)


class Why_us(models.Model):

    name = models.CharField(unique=True, max_length=50, db_index=True)
    description = models.TextField(max_length=300, blank=True)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('name',)


class Gallery(models.Model):

    def get_file_name(self, filename):
        ext_file = filename.strip().split(',')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('gallery/', new_filename)


    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)


class Book_a_table(models.Model):
    mobile_re = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Формат номера : xxx xxx xxxx')
    email_re = RegexValidator(regex=r'(^[A-Za-z0-9]+[\w_]+.[\w_]+@[0-9A-Za-z]+\.[a-z]{2,7}$)', message='your email')

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, validators=[mobile_re])
    persons = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=40, validators=[email_re])
    message = models.TextField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)


    class Meta:
        ordering = ('-date', '-is_processed')

    def __str__(self):
        return f'{self.name}, {self.phone}: {self.message[:50]} '











