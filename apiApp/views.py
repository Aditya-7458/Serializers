from django.shortcuts import render
from .serializers import ProductsSerializer
from .models import Products
from django.http import JsonResponse



def Home(request):
    info = Products.objects.all()
    ser = ProductsSerializer(info, many=True)
    return render(request, 'home.html', {'productsData': ser.data})
