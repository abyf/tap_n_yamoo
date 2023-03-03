from django.contrib import admin
from .models import CardHolder,Merchant,Transaction
# Register your models here.
admin.site.register(CardHolder)
admin.site.register(Merchant)
admin.site.register(Transaction)

