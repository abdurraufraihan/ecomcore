from rest_framework import serializers
from lib import constants as const
from apps.product.models import Product

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		exclude = [const.CATEGORY_PROPERTY, const.DESCRIPTION_PROPERTY]
