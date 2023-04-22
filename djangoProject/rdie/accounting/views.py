from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import HistoryRecordForm
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


def record_expense(request):
    sub_category = request.POST.get('sub_category')
    time_now = timezone.now()
    if sub_category == "select value":
        try:
            account = request.POST.get('account')
            category = request.POST.get('category')
            currency = request.POST.get('currency')
            amount = request.POST.get('amount')
            comment = request.POST.get('comment')
            time_occur = request.POST.get('time_of_occurrence')
            history_record = HistoryRecord(account_id=account,
                                           category_id=category,
                                           currency_id=currency,
                                           amount=amount,
                                           comment=comment,
                                           time_of_occurrence=time_occur,
                                           created_date=time_now,
                                           updated_date=time_now
                                           )
            history_record.save()
        except Exception as e:
            print("not valid in request with error:%s" % str(e))
    else:
        form = HistoryRecordForm(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            category = form.cleaned_data['category']
            sub_category = form.cleaned_data['sub_category']
            currency = form.cleaned_data['currency']
            amount = form.cleaned_data['amount']
            comment = form.cleaned_data['comment']
            time_occur = form.cleaned_data['time_of_occurrence']
            history_record = HistoryRecord(
                account=account,
                category=category,
                sub_category=sub_category,
                currency=currency,
                amount=amount,
                comment=comment,
                time_of_occurrence=time_occur,
                created_date=time_now,
                update_date=time_now
            )
            history_record.save()
        else:
            print("not valid  in form")
    return redirect(index)
