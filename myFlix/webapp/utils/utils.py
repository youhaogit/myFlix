from urllib.parse import urlsplit, parse_qs

from webapp.models import Customers

def get_qs_params(request):
    """
    return query param from url
    """
    _url = request.build_absolute_uri()
    _qs = urlsplit(_url).query
    if _qs:
        _params = parse_qs(_qs)
        _page_number = _params.get('pageNumber')
        _item_per_page = _params.get('itemPerPage')
    else:
        _page_number = 1
        _item_per_page = 20

    return _page_number,_item_per_page


def update_password():
    """
    :return: update plaintext password to cypher
    """
    customers = Customers.objects.all()
    for customer in customers:
        password = customer.password
        if password.startswith('pbkdf2'):
            continue
        customer.set_password(password)
        customer.save()
