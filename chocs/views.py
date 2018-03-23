from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.http import JsonResponse

from .models import *
# Create your views here.
def show_idex_page(request):

    print (request.session.session_key)
    return render(request, 'show_index_page.html' )

class SetsListView(generic.ListView):
    model = Sets

class SetsDetailView(generic.DetailView):
    model = Sets

class BarListView(generic.ListView):
    model = Bar

class BarDetailView(generic.DetailView):
    model = Bar

def basket_adding(request):
    data = request.POST
    return_dict = {}
    session_key = request.session.session_key
    product_name = data.get("name")
    number = data.get("number")
    price_per_item = data.get("price_per_item")

    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_name=product_name, price_per_item=price_per_item, defaults={"number":number,"price_per_item":price_per_item,})
    if not created:
        new_product.number += int(number)
        new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key)
    products_number_total = products_in_basket.count()

    return_dict["products_number_total"] = products_number_total
    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["product_name"] = item.product_name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["number"] = item.number
        return_dict["products"].append(product_dict)

    print(return_dict)
    print (request.POST)
    return JsonResponse (return_dict)

"""
# to store basket data in a backend
def product(request, product_id):
    product = Chocs.objects.get(pk=product_id)

    #getting session key
    session_key = request.session.session_key

    #if user isn not auth, we get cycle key from django
    if not session_key:
        request.session.cycle_key()
        print('dig deeper!')

    print(request.session.session_key)
    print('hello')

    return render(request, 'sets_detail.html', locals())
"""
