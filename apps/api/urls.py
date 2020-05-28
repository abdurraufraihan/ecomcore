from django.urls import path
from lib import apiendpoints
from apps.api.views.productviews import ProductListView, ProductDetailView
from apps.api.views.categoryviews import CategoryListView

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
	),
	path(
		apiendpoints.CATEGORY_URL,
		CategoryListView.as_view(),
		name='categoryList'
	)
]
