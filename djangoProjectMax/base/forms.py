from django import forms
from .models import Book_a_table


class UserReservationForm(forms.ModelForm):

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'name',
             'class': 'form-control',
            'id': 'name',
            'placeholder': 'Ваше имя',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
        })
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'phone',
            'class': 'form-control',
            'id': 'phone',
            'placeholder': 'Введите номер',
            'pattern': '^(\d{3}[- .]?){2}\d{4}$',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
        })
    )

    email = forms.EmailField(
        max_length=40,
        widget=forms.TextInput(attrs={
            'type': 'email',
            'name': 'email',
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Введите вашу почту',
            'data-rule': 'email',
            'pattern': '(^[A-Za-z0-9]+[\w_]+.[\w_]+@[0-9A-Za-z]+\.[a-z]{2,7}$)',
            'data-msg': 'Please enter at least 4 chars',
        })
    )


    persons = forms.IntegerField(

        widget=forms.NumberInput(attrs={
            'type': 'number',
            'name': 'persons',
            'class': 'form-control',
            'id': 'persons',
            'placeholder': 'Количество посетителей',
            'data-rule': 'minlen:1',
            'data-msg': 'Please enter at least 4 chars',
        })
    )



    message = forms.CharField(
        max_length=300,
        widget=forms.Textarea(attrs={
            'type': 'message',
            'name': 'message',
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Cообщение',
            'data-rule': 'minlen:4',
            'required': 'required',
            'rows' : '3',
        })
    )



    class Meta:
        model = Book_a_table
        fields = ('name', 'phone', 'email', 'persons', 'message')

