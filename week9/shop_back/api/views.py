from django.http import HttpResponse, HttpRequest, JsonResponse
from api.models import Product, Category
from api.models import Category, Product



def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

def product_by_id(request,product_id):
    product = Product.objects.get(id = product_id)
    product_json = product.to_json()
    return JsonResponse(product_json, safe= False)

def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_by_id(request, category_id):
    category = Category.objects.get(id = category_id)
    category_json = category.to_json()
    return JsonResponse(category_json, safe= False)


def products_by_category(request, category_id):
    products = Product.objects.filter(category = category_id)
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)