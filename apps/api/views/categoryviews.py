from rest_framework.generics import ListAPIView
from apps.product.models import Category
from apps.product.serializers.categoryserializer import CategoryListSerializer

class CategoryListView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryListSerializer
