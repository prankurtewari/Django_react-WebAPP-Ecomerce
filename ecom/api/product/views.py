from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all().order_by('name')
    serializer_class=ProductSerializer