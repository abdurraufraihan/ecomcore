from django.urls import path
from lib import apiendpoints
from apps.api.views.productviews import ProductListView, ProductDetailView

urlpatterns = [
	path(
		apiendpoints.PRODUCT_URL,
		ProductListView.as_view(),
		name='productList'
	),
	path(
		apiendpoints.PRODUCT_DETAIL_URL,
		ProductDetailView.as_view(),
		name='productDetail'
	)
]
