"""
@FileName：urls.py
@Author：stone
@Time：2023/4/21 18:31
@Description:创建app的路由
"""

from django.urls import path
from .  import  views

urlpatterns = [
    path('',views.index,name='index'),
    path('retrieve_category/',views.retrieve_category,name='retrieve_category'),
    path('record_income_expense/',views.record_expense,name='record_income_expense')

]
