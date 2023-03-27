from django.shortcuts import render
from rest_framework.response import Response

from .models import Product
from rest_framework.decorators import api_view
from .serializers import ProductSerializer


# Create your views here.




@api_view(['Get'])
def api_overview(request):
    api_urls={
        'List':'/product-list',
        'Detail View':'/product-detail/<int:id>',
        'Create':'/product-create/',
        'Update':'/product-update/<int:id>',
        'Delete':'/product-delete/<int:id>'
    }
    return Response(api_urls)

@api_view(['Get'])
def showall(request):
    products=Product.objects.all()
    serializer =ProductSerializer(products,many=True)
    return Response(serializer.data)

# create
@api_view(['Post'])
def createproduct(request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# single view

@api_view(['Get'])
def viewproduct(request,pk):
    product=Product.objects.get(id=pk)
    serialaizer= ProductSerializer(product,many=False)
    return Response(serialaizer.data)

# update
@api_view(['Post'])
def updateproduct(request,pk):
    product=Product.objects.get(id=pk)
    serializer= ProductSerializer(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['Delete'])
def deleteproduct(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    return Response("product is deleted successfully")

