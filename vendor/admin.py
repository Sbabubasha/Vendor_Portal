from django.contrib import admin

# Register your models here.

from vendor.models import *

admin.site.register(Vendor)

admin.site.register(PurchaseOrder)

admin.site.register(HistoricalPerformance)