from rest_framework.generics import ListAPIView
from lib import errorutility as errorUtil
from apps.product.models import Category
from apps.product.serializers.categoryserializer import CategoryListSerializer

class CategoryListView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryListSerializer

	def get(self, request, *args, **kwargs):
		try:
			return self.list(request, *args, **kwargs)
		except:
			return errorUtil.getInternalServerErrorResponse()
