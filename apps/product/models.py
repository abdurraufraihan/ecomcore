import uuid
from django.db import models
from lib import constants

class Category(models.Model):
	categoryId = models.UUIDField(
		default=uuid.uuid4, editable=False, unique=True
	)
	name = models.CharField(max_length=constants.CATEGORY_NAME_MAX_LENGTH)

	def __str__(self):
		return self.name

class Product(models.Model):
	productId = models.UUIDField(
		default=uuid.uuid4, editable=False, unique=True
	)
	title = models.CharField(max_length=50)
	description = models.TextField()
	price = models.FloatField()
	image = models.ImageField(upload_to=constants.PRODUCT_IMAGE_UPLOAD_PATH)
	category = models.ForeignKey(
		Category, on_delete=models.SET_NULL, null=True, blank=True
	)

	def __str__(self):
		return self.title
