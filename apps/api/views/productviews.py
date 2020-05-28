from rest_framework.generics import ListAPIView
from lib import constants as const
from apps.product.models import Product
from apps.product.serializers.productserializer import ProductSerializer

class ProductListView(ListAPIView):
	serializer_class = ProductSerializer

	def get_queryset(self):
		categoryId = \
			self.request.query_params.get(const.CATEGORY_ID_QUERY_PARAM)
		search = self.request.query_params.get(const.SEARCH_QUERY_PARAM)
		productFilter = {}
		if categoryId:
			productFilter[const.CATEGORY_ID_FILTER_PROPERTY] = categoryId
		if search:
			productFilter[const.TITLE_CONTAINS_FILTER_PROPERTY] = search
		queryset = Product.objects.filter(**productFilter)
		return queryset
