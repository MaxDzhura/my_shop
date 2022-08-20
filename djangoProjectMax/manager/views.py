from django.shortcuts import render, HttpResponse, redirect
from base.models import Book_a_table
from django.contrib.auth.decorators import login_required, user_passes_test



def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/account/login/')
@user_passes_test(is_manager)
def reservation_list(request):
    lst = Book_a_table.objects.filter(is_processed=False)
    return render(request, 'reservetions_list.html', context={'lst': lst,})


@login_required(login_url='/account/login/')
@user_passes_test(is_manager)
def update_reservation(request,pk):
    Book_a_table.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservetions_list')