from rest_framework import serializers
from lib import constants as const
from apps.product.models import Product

class ProductListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		exclude = [const.CATEGORY_PROPERTY, const.DESCRIPTION_PROPERTY]

class ProductDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = const.ALL_FIELDS_PROPERTY
		depth = 1
