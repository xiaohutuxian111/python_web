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
]
