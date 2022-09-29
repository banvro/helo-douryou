from rest_framework import serializers

from douryou_user.models import your_requirement,education_loan,travel_insurance,appy_job_requirement, passport, douryou_login, ApplyLuggageAdliodtmet, ApplyPurchaseFrancbise

from douryou_seller.models import SellerTodaysDeals,SellerProfile

###################### start new task about show ads to user........ ################3333

# class SellerProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SellerProfile
#         fields = '__all__'
#         # fields = ['phone_number','phone_number', 'ContactPersonName','ads']
#         print(fields)

class SellerTodaysDealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerTodaysDeals
        # fields = '__all__'
        fields = ['from_compny_profile','TodaysDealID', 'Catagery', 'DealTitle', 'DealPostDateandTime', 'DealAddDiscription', 'UploadAdsPhoto', 'from_compny_profile']
        # print(fields)

        depth = 1









class Your_RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = your_requirement
        fields = '__all__'
        print(fields)

class Education_LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = education_loan
        fields = '__all__'

class Travel_InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = travel_insurance
        fields = '__all__'

class Appy_Job_RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = appy_job_requirement
        fields = '__all__'

class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = passport
        fields = '__all__'

class Douryou_LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = douryou_login
        fields = '__all__'

class ApplyLuggageAdliodtmetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyLuggageAdliodtmet
        fields = '__all__'

class ApplyPurchaseFrancbiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyPurchaseFrancbise
        fields = '__all__'








