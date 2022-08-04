from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Balances, GetData, TransferAmount,Emp

# Register your models here.

admin.site.register(Balances)
admin.site.register(GetData)
admin.site.register(TransferAmount)
admin.site.register(Emp)