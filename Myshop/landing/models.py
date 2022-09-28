from django.db import models
from django.core.validators import RegexValidator


class Subscriber(models.Model):

    email_re = RegexValidator(regex=r'(^[A-Za-z0-9]+[\w_]+.[\w_]+@[0-9A-Za-z]+\.[a-z]{2,7}$)', message='your email')

    email = models.EmailField(max_length=40, validators=[email_re])
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}, {self.email}'


    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'