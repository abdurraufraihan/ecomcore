from django.urls import path
from lib import apiendpoints
from apps.api.views.productviews import ProductListView

urlpatterns = [
	path(
		apiendpoints.PRODUCT_URL, ProductListView.as_view(), name='productList'
	)
]
