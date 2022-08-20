from django.shortcuts import render, HttpResponse

# Create your views here.
def customer(request, customer_number):
    return HttpResponse(f'Hello dear customer with ID {customer_number}')

def customer_general(request):
    return HttpResponse(' Page of customer')