from rest_framework.generics import ListAPIView
from apps.product.models import Product
from apps.product.serializers.productserializer import ProductSerializer

class ProductListView(ListAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()
