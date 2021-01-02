from django.contrib import admin
from .models import Order,BuyerReview,SellerReview,PaymentRecord
# Register your models here.
admin.site.register(Order)
admin.site.register(BuyerReview)
admin.site.register(SellerReview)
admin.site.register(PaymentRecord)