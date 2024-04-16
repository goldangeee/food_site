#customer/views.py
from django.shortcuts import render
from chinese.models import Category, Food

def customer_index(request):
    category = Category.objects.all()

    return render(request,'customer/index.html')