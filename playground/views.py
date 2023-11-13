from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product,OrderItem




def say_hello(request):
    query_set=Product.objects.filter(unit_price__range=(20,30))
    return render(request, 'hello.html', {'name': 'Mosh','products':list(query_set)})
