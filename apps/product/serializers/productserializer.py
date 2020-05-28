from rest_framework import serializers
from lib import constants as const
from apps.product.models import Product
from apps.product.serializers.categoryserializer import CategorySerializer

class ProductListSerializer(serializers.ModelSerializer):
	id = serializers.UUIDField(source=const.PRODUCT_ID_PROPERTY)

	class Meta:
		model = Product
		exclude = [
			const.PRODUCT_ID_PROPERTY,
			const.CATEGORY_PROPERTY,
			const.DESCRIPTION_PROPERTY
		]

class ProductDetailSerializer(ProductListSerializer):
	category = CategorySerializer(read_only=True)

	class Meta:
		model = Product
		exclude = [const.PRODUCT_ID_PROPERTY]
