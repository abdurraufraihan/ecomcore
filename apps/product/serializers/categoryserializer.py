from rest_framework import serializers
from lib import constants as const
from apps.product.models import Category

class CategoryListSerializer(serializers.ModelSerializer):
	id = serializers.UUIDField(source=const.CATEGORY_ID_PROPERTY)

	class Meta:
		model = Category
		fields = [const.ID_PROPERTY, const.NAME_PROPERTY]
