from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from lib import constants as const
from lib import commonutility as commonUtil
from lib import errorutility as errorUtil
from apps.product.models import Product
from apps.product.serializers.productserializer import ProductListSerializer, \
	ProductDetailSerializer

class ProductListView(ListAPIView):
	serializer_class = ProductListSerializer

	def get(self, request, *args, **kwargs):
		try:
			return self.list(request, *args, **kwargs)
		except:
			return errorUtil.getInternalServerErrorResponse()

	def get_queryset(self):
		categoryId = \
			self.request.query_params.get(const.CATEGORY_ID_QUERY_PARAM)
		search = self.request.query_params.get(const.SEARCH_QUERY_PARAM)
		page = self.request.query_params.get(const.PAGE_QUERY_PARAM)
		startItem, endItem = \
			commonUtil.getPaginationRange(page, const.PRODUCT_PER_PAGE)
		productFilter = {}
		if categoryId:
			productFilter[const.CATEGORY_ID_FILTER_PROPERTY] = categoryId
		if search:
			productFilter[const.TITLE_CONTAINS_FILTER_PROPERTY] = search
		queryset = Product.objects.filter(**productFilter)[startItem : endItem]
		return queryset

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)
		serializer = self.get_serializer(queryset, many=True)
		totalProduct = Product.objects.count()
		finalResponse = {
			const.TOTAL_PRODUCT_PROPERTY: totalProduct,
			const.PRODUCTS_PROPERTY: serializer.data
		}
		return Response(finalResponse)

class ProductDetailView(RetrieveAPIView):
	serializer_class = ProductDetailSerializer
	lookup_field = const.PRODUCT_ID_PROPERTY

	def get(self, request, *args, **kwargs):
		try:
			return self.retrieve(request, *args, **kwargs)
		except:
			return errorUtil.getInternalServerErrorResponse()

	def get_queryset(self):
		return Product.objects.filter(
			productId=self.kwargs[const.PRODUCT_ID_PROPERTY]
		)
