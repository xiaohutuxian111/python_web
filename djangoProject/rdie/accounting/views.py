from django.shortcuts import render

from .models import *


def index(request):
    # return render(request, 'accounting/index.html')
    all_accounts = Account.objects.all()
    sub_categories = SubGategory.objects.all()
    context = {
        'accounts': all_accounts,
        'sub_categories': sub_categories
    }
    print(context)
    return render(request, 'accounting/index.html', context)
