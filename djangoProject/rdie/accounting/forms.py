"""
@FileName：forms.py
@Author：stone
@Time：2023/4/22 13:04
@Description:
"""

from django import forms
from .models import HistoryRecord


class HistoryRecordForm(forms.ModelForm):
    class Meta:
        model = HistoryRecord
        exclude = ['created_date', 'update_date']
