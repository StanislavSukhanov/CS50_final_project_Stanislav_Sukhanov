from .models import ProductInBasket

def getting_basket_info(request):
    session_key = request.session.session_key

    if not session_key:
        request.session.cycle_key()

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key)

    products_number_total = products_in_basket.count()

    print("hello world")
    return locals()
