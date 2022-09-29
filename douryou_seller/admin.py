from django.contrib import admin
from douryou_seller.models import SellerProfile, SellerJobOffer, SellerSellFranchise, SellerTodaysDeals
# Register your models here.


admin.site.register(SellerProfile) 
admin.site.register(SellerJobOffer) 
admin.site.register(SellerSellFranchise) 
admin.site.register(SellerTodaysDeals) 

