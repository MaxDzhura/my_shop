from django.contrib import admin
from .models import *


class SubscriberAdmin (admin.ModelAdmin):
    # list_display = ["name", "email"]                                  #  выводит  поля модели которые укажем в админку
    list_display = [field.name for field in Subscriber._meta.fields]    # цикл выводит все поля модели в админку
    list_filter = ['name',]                                              #  фильтр по полю которые укажем
    search_fields = ['name', 'email']

    fields = ["name", "email"]

    # exclude = ["email"]
	# inlines = [FieldMappingInline]
	# fields = []                                                           #  поля модели в админку которые  хотим выводить
    # #exclude = ["type"]                                                    #  поля модели в админку которые не хотим выводить
	# #list_filter = ('report_data',)
	# search_fields = ['category', 'subCategory', 'suggestKeyword']          # инпут для поиска поля в админке

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)