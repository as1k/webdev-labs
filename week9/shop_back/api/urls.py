from django.urls import path, re_path
from api.views import product_list, product_by_id, category_list,category_by_id, products_by_category

urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>/', product_by_id),
    path('categories/', category_list),
    path('categories/<int:category_id>/', category_by_id),
    path('categories/<int:category_id>/products', products_by_category),
]