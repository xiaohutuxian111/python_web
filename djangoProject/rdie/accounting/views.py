from django.http import JsonResponse
from django.shortcuts import render

from .models import *


def index(request):
    all_accounts = Account.objects.all()
    categories = Category.objects.all()
    sub_categories = SubGategory.objects.all()
    currencies = Currency.objects.all()
    ie_types = []
    for t in Category.GATEGORY_TYPES:
        ie_types.append(t[0])
    context = {
        'accounts': all_accounts,
        'categories': categories,
        'sub_categories': sub_categories,
        'currencies': currencies,
        'ie_types': ie_types
    }
    return render(request, 'accounting/index.html', context)


def retrieve_category(request):
    """获取类别"""
    ie_type = request.POST.get('ie_type')
    categories = Category.objects.filter(category_type=ie_type)
    category_list = []
    for c in categories:
        category_list.append(c.name)
    return JsonResponse({"categories": category_list})
