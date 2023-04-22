from django.contrib import admin

from  .models import *

# Register your models here.


admin.register(Currency)
admin.register(Account)
admin.register(Category)
admin.register(SubGategory)
admin.register(HistoryRecord)
