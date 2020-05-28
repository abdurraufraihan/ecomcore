from django.contrib import admin
from lib import constants as const
from apps.product.models import Product, Category

class ProductAdmin(admin.ModelAdmin):
	list_display = [
		const.ID_PROPERTY,
		const.PRODUCT_ID_PROPERTY,
		const.TITLE_PROPERTY,
		const.DESCRIPTION_PROPERTY,
		const.PRICE_PROPERTY,
		const.IMAGE_PROPERTY,
		const.CATEGORY_PROPERTY
	]

class CategoryAdmin(admin.ModelAdmin):
	list_display = [
		const.ID_PROPERTY,
		const.CATEGORY_ID_PROPERTY,
		const.NAME_PROPERTY
	]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
