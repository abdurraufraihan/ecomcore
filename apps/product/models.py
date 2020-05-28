import uuid
from django.db import models

class Product(models.Model):
	productId = models.UUIDField(
		default=uuid.uuid4, editable=False, unique=True
	)
	title = models.CharField(max_length=50)
	description = models.TextField()
	price = models.FloatField()
	image = models.ImageField(upload_to='product/')

	def __str__(self):
		return self.title
