from django.contrib import admin
from .models import Category, Dish, Events, Special, About, Why_us, Gallery, Book_a_table

admin.site.register(Category)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',) ,}


admin.site.register(Events)
admin.site.register(Special)
admin.site.register(About)
admin.site.register(Why_us)
admin.site.register(Gallery)
admin.site.register(Book_a_table)