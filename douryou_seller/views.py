from ast import Not
from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
# from douryou.models import User
from douryou_seller.models import SellerProfile, SellerTodaysDeals, SellerJobOffer, SellerSellFranchise
# from django.contrib.auth import get_user_model

from django.contrib.auth import login, logout, authenticate

from douryou_user.models import douryou_login


# Create your views here.
# User = get_user_model()

def seller_login(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        print(phone_number, password)
        user = authenticate(username=phone_number, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"successuflly login")
            return redirect('seller_createprofile1')
        else:
            messages.warning(request, 'user not exist...')
    return render(request, 'seller_login.html')

# def seller_login(request):
#     if request.method == 'POST':
#         phone_number = request.POST['phone_number']
#         user = UserLogin(phone_number=phone_number)
#         user.save()
#     return render(request, 'seller_login.html')

# def seller_signup(request):
#     return render(request, 'seller_verify_otp.html')


def seller_otp(request):
    print('this is user : ', User.id)
    x = (request.user.id)
    print(x)
    print(type(x))
    print(SellerProfile.phone_number)
    print(User.username)
    print(User.pk)
    print(request.user)
    print(request.user.username)
    print(request.user.id)
    x = SellerProfile.objects.get(pk=request.user.id).OfficePic1
    print(x)
    
    

    return render(request, 'seller_otp.html')


def seller_createprofile1(request):
    
    if request.method == "POST":
        # phone_number = User.objects.get(id=).phone_number
        ContactPersonName = request.POST.get('ContactPersonName')
        ContactPersonNumber = request.POST.get('ContactPersonNumber')
        ContactPersonDesigation = request.POST.get('ContactPersonDesigation')
        CompanyName = request.POST.get('CompanyName')
        CompanyAddress = request.POST.get('CompanyAddress')
        CompanyDistrictName = request.POST.get('CompanyDistrictName')
        CompanyStateName = request.POST.get('CompanyStateName')
        CompanyEmailID = request.POST.get('CompanyEmailID')
        CompanyWebsiteLink = request.POST.get('CompanyWebsiteLink')
        CompanyLoginPhoneNo = request.POST.get('CompanyLoginPhoneNo')
        AboutCompany = request.POST.get('AboutCompany')
        SpecializationOfCompany = request.POST.get('SpecializationOfCompany')
        WhyJoin = request.POST.getlist('WhyJoin')
        ContactPersonPic = request.FILES.get('ContactPersonPic')
        CompanyLogo = request.FILES.get('CompanyLogo')

        date = request.POST.get('datetime.today()')

        data = SellerProfile(phone_number=request.user,ContactPersonPic=ContactPersonPic, ContactPersonName=ContactPersonName,
                             ContactPersonNumber=ContactPersonNumber,
                             ContactPersonDesigation=ContactPersonDesigation,
                             CompanyLogo=CompanyLogo,
                             CompanyName=CompanyName,
                             CompanyAddress=CompanyAddress,
                             CompanyDistrictName=CompanyDistrictName,
                             CompanyStateName=CompanyStateName,
                             CompanyEmailID=CompanyEmailID,
                             CompanyWebsiteLink=CompanyWebsiteLink,
                             CompanyLoginPhoneNo=CompanyLoginPhoneNo,
                             AboutCompany=AboutCompany,
                             SpecializationOfCompany=SpecializationOfCompany, WhyJoin=WhyJoin, date=date)
        data.save()
        return redirect('seller_images')
    return render(request, 'seller_createprofile1.html')


def seller_images(request):
    if request.method == "POST":

        OfficePic1 = request.FILES.get('office_pic1')
        OfficePic2 = request.FILES.get('office_pic2')
        OfficePic3 = request.FILES.get('office_pic3')
        OfficePic4 = request.FILES.get('office_pic4')
        OfficePic5 = request.FILES.get('office_pic5')
        OfficePic6 = request.FILES.get('office_pic6')
        OfficePic7 = request.FILES.get('office_pic7')
        OfficePic8 = request.FILES.get('office_pic8')
        OfficePic9 = request.FILES.get('office_pic9')
        OfficePic10 = request.FILES.get('office_pic10')
        OfficePic11 = request.FILES.get('office_pic11')
        OfficePic12 = request.FILES.get('office_pic12')

        CompanyCertificationPic1 = request.FILES.get('office_certificatte1')
        CompanyCertificationPic2 = request.FILES.get('office_certificatte2')
        CompanyCertificationPic3 = request.FILES.get('office_certificatte3')
        CompanyCertificationPic4 = request.FILES.get('office_certificatte4')
        CompanyCertificationPic5 = request.FILES.get('office_certificatte5')
        CompanyCertificationPic6 = request.FILES.get('office_certificatte6')
        CompanyCertificationPic7 = request.FILES.get('office_certificatte7')
        CompanyCertificationPic8 = request.FILES.get('office_certificatte8')
        CompanyCertificationPic9 = request.FILES.get('office_certificatte9')
        CompanyCertificationPic10 = request.FILES.get('office_certificatte10')
        CompanyCertificationPic11 = request.FILES.get('office_certificatte11')
        CompanyCertificationPic12 = request.FILES.get('office_certificatte12')

        CompanyPreviousResultsPic1 = request.FILES.get('office_prev_result1')
        CompanyPreviousResultsPic2 = request.FILES.get('office_prev_result2')
        CompanyPreviousResultsPic3 = request.FILES.get('office_prev_result3')
        CompanyPreviousResultsPic4 = request.FILES.get('office_prev_result4')
        CompanyPreviousResultsPic5 = request.FILES.get('office_prev_result5')
        CompanyPreviousResultsPic6 = request.FILES.get('office_prev_result6')
        CompanyPreviousResultsPic7 = request.FILES.get('office_prev_result7')
        CompanyPreviousResultsPic8 = request.FILES.get('office_prev_result8')
        CompanyPreviousResultsPic9 = request.FILES.get('office_prev_result9')
        CompanyPreviousResultsPic10 = request.FILES.get('office_prev_result10')
        CompanyPreviousResultsPic11 = request.FILES.get('office_prev_result11')
        CompanyPreviousResultsPic12 = request.FILES.get('office_prev_result12')

        CustomerReviewsPic1 = request.FILES.get('office_custmer_reviews_pic1')
        CustomerReviewsPic2 = request.FILES.get('office_custmer_reviews_pic2')
        CustomerReviewsPic3 = request.FILES.get('office_custmer_reviews_pic3')
        CustomerReviewsPic4 = request.FILES.get('office_custmer_reviews_pic4')
        CustomerReviewsPic5 = request.FILES.get('office_custmer_reviews_pic5')
        CustomerReviewsPic6 = request.FILES.get('office_custmer_reviews_pic6')
        CustomerReviewsPic7 = request.FILES.get('office_custmer_reviews_pic7')
        CustomerReviewsPic8 = request.FILES.get('office_custmer_reviews_pic8')
        CustomerReviewsPic9 = request.FILES.get('office_custmer_reviews_pic9')
        CustomerReviewsPic10 = request.FILES.get(
            'office_custmer_reviews_pic10')
        CustomerReviewsPic11 = request.FILES.get(
            'office_custmer_reviews_pic11')
        CustomerReviewsPic12 = request.FILES.get(
            'office_custmer_reviews_pic12')


        ###this isdjsabkdbaksdjbkasjd
        ContactPersonName = SellerProfile.objects.get(pk=request.user.id).ContactPersonName
        ContactPersonNumber = SellerProfile.objects.get(pk=request.user.id).ContactPersonNumber
        ContactPersonDesigation = SellerProfile.objects.get(pk=request.user.id).ContactPersonDesigation
        CompanyName = SellerProfile.objects.get(pk=request.user.id).CompanyName
        CompanyAddress = SellerProfile.objects.get(pk=request.user.id).CompanyAddress
        CompanyDistrictName = SellerProfile.objects.get(pk=request.user.id).CompanyDistrictName
        CompanyStateName = SellerProfile.objects.get(pk=request.user.id).CompanyStateName
        CompanyEmailID = SellerProfile.objects.get(pk=request.user.id).CompanyEmailID
        CompanyWebsiteLink = SellerProfile.objects.get(pk=request.user.id).CompanyWebsiteLink
        CompanyLoginPhoneNo = SellerProfile.objects.get(pk=request.user.id).CompanyLoginPhoneNo
        AboutCompany = SellerProfile.objects.get(pk=request.user.id).AboutCompany
        SpecializationOfCompany = SellerProfile.objects.get(pk=request.user.id).SpecializationOfCompany
        WhyJoin = SellerProfile.objects.get(pk=request.user.id).WhyJoin
        ContactPersonPic = SellerProfile.objects.get(pk=request.user.id).ContactPersonPic
        CompanyLogo = SellerProfile.objects.get(pk=request.user.id).CompanyLogo

        date = request.POST.get('datetime.today()')

        data = SellerProfile(phone_number=request.user, OfficePic1=OfficePic1,
                             OfficePic2=OfficePic2,
                             OfficePic3=OfficePic3,
                             OfficePic4=OfficePic4,
                             OfficePic5=OfficePic5,
                             OfficePic6=OfficePic6,
                             OfficePic7=OfficePic7,
                             OfficePic8=OfficePic8,
                             OfficePic9=OfficePic9,
                             OfficePic10=OfficePic10,
                             OfficePic11=OfficePic11,
                             OfficePic12=OfficePic12,

                             CompanyCertificationPic1=CompanyCertificationPic1,
                             CompanyCertificationPic2=CompanyCertificationPic2,
                             CompanyCertificationPic3=CompanyCertificationPic3,
                             CompanyCertificationPic4=CompanyCertificationPic4,
                             CompanyCertificationPic5=CompanyCertificationPic5,
                             CompanyCertificationPic6=CompanyCertificationPic6,
                             CompanyCertificationPic7=CompanyCertificationPic7,
                             CompanyCertificationPic8=CompanyCertificationPic8,
                             CompanyCertificationPic9=CompanyCertificationPic9,
                             CompanyCertificationPic10=CompanyCertificationPic10,
                             CompanyCertificationPic11=CompanyCertificationPic11,
                             CompanyCertificationPic12=CompanyCertificationPic12,

                             CompanyPreviousResultsPic1=CompanyPreviousResultsPic1,
                             CompanyPreviousResultsPic2=CompanyPreviousResultsPic2,
                             CompanyPreviousResultsPic3=CompanyPreviousResultsPic3,
                             CompanyPreviousResultsPic4=CompanyPreviousResultsPic4,
                             CompanyPreviousResultsPic5=CompanyPreviousResultsPic5,
                             CompanyPreviousResultsPic6=CompanyPreviousResultsPic6,
                             CompanyPreviousResultsPic7=CompanyPreviousResultsPic7,
                             CompanyPreviousResultsPic8=CompanyPreviousResultsPic8,
                             CompanyPreviousResultsPic9=CompanyPreviousResultsPic9,
                             CompanyPreviousResultsPic10=CompanyPreviousResultsPic10,
                             CompanyPreviousResultsPic11=CompanyPreviousResultsPic11,
                             CompanyPreviousResultsPic12=CompanyPreviousResultsPic12,

                             CustomerReviewsPic1=CustomerReviewsPic1,
                             CustomerReviewsPic2=CustomerReviewsPic2,
                             CustomerReviewsPic3=CustomerReviewsPic3,
                             CustomerReviewsPic4=CustomerReviewsPic4,
                             CustomerReviewsPic5=CustomerReviewsPic5,
                             CustomerReviewsPic6=CustomerReviewsPic6,
                             CustomerReviewsPic7=CustomerReviewsPic7,
                             CustomerReviewsPic8=CustomerReviewsPic8,
                             CustomerReviewsPic9=CustomerReviewsPic9,
                             CustomerReviewsPic10=CustomerReviewsPic10,
                             CustomerReviewsPic11=CustomerReviewsPic11,
                             CustomerReviewsPic12=CustomerReviewsPic12,


                             #asdasdasdsadasdsadsadsad

                             ContactPersonPic=ContactPersonPic, ContactPersonName=ContactPersonName,
                             ContactPersonNumber=ContactPersonNumber,
                             ContactPersonDesigation=ContactPersonDesigation,
                             CompanyLogo=CompanyLogo,
                             CompanyName=CompanyName,
                             CompanyAddress=CompanyAddress,
                             CompanyDistrictName=CompanyDistrictName,
                             CompanyStateName=CompanyStateName,
                             CompanyEmailID=CompanyEmailID,
                             CompanyWebsiteLink=CompanyWebsiteLink,
                             CompanyLoginPhoneNo=CompanyLoginPhoneNo,
                             AboutCompany=AboutCompany,
                             SpecializationOfCompany=SpecializationOfCompany, WhyJoin=WhyJoin,

                             date=date)

        data.save()
        return redirect('buy_your_plan')

    return render(request, 'seller_images.html')


def buy_your_plan(request):
    if request.method=="POST":
        professional = request.POST.get('professional')
        print(professional)

        if professional == 'Buy Professional Plan':
            pro = SellerProfile.objects.get(phone_number=request.user)
            pro.PORFENSSIONAL_Plan = True
            pro.save()
            messages.success(request, "You choose PORFENSSIONAL Plan !")
            return redirect('payment_getway')
        elif professional == 'Buy Business Plan':
            pro = SellerProfile.objects.get(phone_number=request.user)
            pro.BUSINESS_Plan = True
            pro.save()
            messages.success(request, "You choose BUSINESS Plan !")
            return redirect('payment_getway')
        elif professional == 'Buy Ultimate Plan':
            pro = SellerProfile.objects.get(phone_number=request.user)
            pro.ULTIMATE_Plan = True
            pro.save()
            messages.success(request, "You choose ULTIMATE Plan !")
            return redirect('payment_getway')
        else:
            messages.warning(request, "Your Submitted data Face an issue, we will back to you..!")
            return redirect('payment_getway')

    return render(request, 'buy_your_plan.html')


def payment_getway(request):
    if request.method == "POST":
        plan = request.POST.get('plan')
        if plan == 'Pay the Ammount':
            plann = SellerProfile.objects.get(phone_number=request.user)
            plann.is_payment_done = True
            plann.save()
            messages.success(request, "Payment Successfully DONE !")
            return redirect('seller_view_ads')
    return render(request, 'payment_getway.html')

###    selller profile handleing ...... view , update ......
def seller_profile(request):
    userprofiledata = SellerProfile.objects.get(phone_number=request.user)
    print(userprofiledata)
    context = {'userprofiledata' : userprofiledata}
    return render(request, 'seller_profile.html', context)

def seller_updateprofile(request):
    updateprofieid = SellerProfile.objects.get(phone_number=request.user)
    print(updateprofieid)
    context = {'updateprofieid' : updateprofieid}
    return render(request, 'seller_updateprofile.html', context)


def seller_editprofile(request):
    updateprofieid = SellerProfile.objects.get(phone_number=request.user)
    if request.method == "POST":
        # phone_number = User.objects.get(id=).phone_number
        updateprofieid.ContactPersonName = request.POST.get('ContactPersonName')
        if request.POST.get('ContactPersonNumber') is not None:
            updateprofieid.ContactPersonNumber = request.POST.get('ContactPersonNumber')
        else:
            updateprofieid.ContactPersonNumber = updateprofieid.ContactPersonNumber

        if request.POST.get('CompanyLoginPhoneNo') is not None:
            updateprofieid.CompanyLoginPhoneNo = updateprofieid.CompanyLoginPhoneNo
        else:
            updateprofieid.CompanyLoginPhoneNo = updateprofieid.CompanyLoginPhoneNo
        
        updateprofieid.ContactPersonDesigation = request.POST.get('ContactPersonDesigation')
        updateprofieid.CompanyName = request.POST.get('CompanyName')
        updateprofieid.CompanyAddress = request.POST.get('CompanyAddress')
        updateprofieid.CompanyDistrictName = request.POST.get('CompanyDistrictName')
        updateprofieid.CompanyStateName = request.POST.get('CompanyStateName')
        updateprofieid.CompanyEmailID = request.POST.get('CompanyEmailID')
        updateprofieid.CompanyWebsiteLink = request.POST.get('CompanyWebsiteLink')
        if request.POST.get('AboutCompany') is not None:
            updateprofieid.AboutCompany = request.POST.get('AboutCompany')
        else:
            updateprofieid.AboutCompany = updateprofieid.AboutCompany

        updateprofieid.SpecializationOfCompany = request.POST.get('SpecializationOfCompany')
        updateprofieid.WhyJoin = request.POST.getlist('WhyJoin')

        if request.FILES.get('ContactPersonPic') is not None:
            updateprofieid.ContactPersonPic = request.FILES.get('ContactPersonPic')
        else:
            updateprofieid.ContactPersonPic = updateprofieid.ContactPersonPic

        if request.FILES.get('CompanyLogo') is not None:
            updateprofieid.CompanyLogo = request.FILES.get('CompanyLogo')
        else:
            updateprofieid.CompanyLogo = updateprofieid.CompanyLogo
        
# images update handel...    

        if request.FILES.get('OfficePic1') is not None:
            updateprofieid.OfficePic1 = request.FILES.get('OfficePic1')
        else:
            updateprofieid.OfficePic1 = updateprofieid.OfficePic1
        

        if request.FILES.get('OfficePic2') is not None:
            updateprofieid.OfficePic2 = request.FILES.get('OfficePic2')
        else:
            updateprofieid.OfficePic2 = updateprofieid.OfficePic2
        

        if request.FILES.get('OfficePic3') is not None:
            updateprofieid.OfficePic3 = request.FILES.get('OfficePic3')
        else:
            updateprofieid.OfficePic3 = updateprofieid.OfficePic3
        

        if request.FILES.get('OfficePic4') is not None:
            updateprofieid.OfficePic4 = request.FILES.get('OfficePic4')
        else:
            updateprofieid.OfficePic4 = updateprofieid.OfficePic4
        

        if request.FILES.get('OfficePic5') is not None:
            updateprofieid.OfficePic5 = request.FILES.get('OfficePic5')
        else:
            updateprofieid.OfficePic5 = updateprofieid.OfficePic5
        

        if request.FILES.get('OfficePic6') is not None:
            updateprofieid.OfficePic6 = request.FILES.get('OfficePic6')
        else:
            updateprofieid.OfficePic6 = updateprofieid.OfficePic6
        

        if request.FILES.get('OfficePic7') is not None:
            updateprofieid.OfficePic7 = request.FILES.get('OfficePic7')
        else:
            updateprofieid.OfficePic7 = updateprofieid.OfficePic7
        

        if request.FILES.get('OfficePic8') is not None:
            updateprofieid.OfficePic8 = request.FILES.get('OfficePic8')
        else:
            updateprofieid.OfficePic8 = updateprofieid.OfficePic8
        

        if request.FILES.get('OfficePic9') is not None:
            updateprofieid.OfficePic9 = request.FILES.get('OfficePic9')
        else:
            updateprofieid.OfficePic9 = updateprofieid.OfficePic9
        

        if request.FILES.get('OfficePic10') is not None:
            updateprofieid.OfficePic10 = request.FILES.get('OfficePic10')
        else:
            updateprofieid.OfficePic10 = updateprofieid.OfficePic10
        

        if request.FILES.get('OfficePic11') is not None:
            updateprofieid.OfficePic11 = request.FILES.get('OfficePic11')
        else:
            updateprofieid.OfficePic11 = updateprofieid.OfficePic11
        

        if request.FILES.get('OfficePic12') is not None:
            updateprofieid.OfficePic12 = request.FILES.get('OfficePic12')
        else:
            updateprofieid.OfficePic12 = updateprofieid.OfficePic12
        



        if request.FILES.get('CompanyCertificationPic1') is not None:
            updateprofieid.CompanyCertificationPic1 = request.FILES.get('CompanyCertificationPic1')
        else:
            updateprofieid.CompanyCertificationPic1 = updateprofieid.CompanyCertificationPic1
        

        if request.FILES.get('CompanyCertificationPic2') is not None:
            updateprofieid.CompanyCertificationPic2 = request.FILES.get('CompanyCertificationPic2')
        else:
            updateprofieid.CompanyCertificationPic2 = updateprofieid.CompanyCertificationPic2
        

        if request.FILES.get('CompanyCertificationPic3') is not None:
            updateprofieid.CompanyCertificationPic3 = request.FILES.get('CompanyCertificationPic3')
        else:
            updateprofieid.CompanyCertificationPic3 = updateprofieid.CompanyCertificationPic3
        

        if request.FILES.get('CompanyCertificationPic4') is not None:
            updateprofieid.CompanyCertificationPic4 = request.FILES.get('CompanyCertificationPic4')
        else:
            updateprofieid.CompanyCertificationPic4 = updateprofieid.CompanyCertificationPic4
        

        if request.FILES.get('CompanyCertificationPic5') is not None:
            updateprofieid.CompanyCertificationPic5 = request.FILES.get('CompanyCertificationPic5')
        else:
            updateprofieid.CompanyCertificationPic5 = updateprofieid.CompanyCertificationPic5
        

        if request.FILES.get('CompanyCertificationPic6') is not None:
            updateprofieid.CompanyCertificationPic6 = request.FILES.get('CompanyCertificationPic6')
        else:
            updateprofieid.CompanyCertificationPic6 = updateprofieid.CompanyCertificationPic6
        

        if request.FILES.get('CompanyCertificationPic7') is not None:
            updateprofieid.CompanyCertificationPic7 = request.FILES.get('CompanyCertificationPic7')
        else:
            updateprofieid.CompanyCertificationPic7 = updateprofieid.CompanyCertificationPic7
        

        if request.FILES.get('CompanyCertificationPic8') is not None:
            updateprofieid.CompanyCertificationPic8 = request.FILES.get('CompanyCertificationPic8')
        else:
            updateprofieid.CompanyCertificationPic8 = updateprofieid.CompanyCertificationPic8
        

        if request.FILES.get('CompanyCertificationPic9') is not None:
            updateprofieid.CompanyCertificationPic9 = request.FILES.get('CompanyCertificationPic9')
        else:
            updateprofieid.CompanyCertificationPic9 = updateprofieid.CompanyCertificationPic9
        

        if request.FILES.get('CompanyCertificationPic10') is not None:
            updateprofieid.CompanyCertificationPic10 = request.FILES.get('CompanyCertificationPic10')
        else:
            updateprofieid.CompanyCertificationPic10 = updateprofieid.CompanyCertificationPic10
        

        if request.FILES.get('CompanyCertificationPic11') is not None:
            updateprofieid.CompanyCertificationPic11 = request.FILES.get('CompanyCertificationPic11')
        else:
            updateprofieid.CompanyCertificationPic11 = updateprofieid.CompanyCertificationPic11
        

        if request.FILES.get('CompanyCertificationPic12') is not None:
            updateprofieid.CompanyCertificationPic12 = request.FILES.get('CompanyCertificationPic12')
        else:
            updateprofieid.CompanyCertificationPic12 = updateprofieid.CompanyCertificationPic12





        if request.FILES.get('CompanyPreviousResultsPic1') is not None:
            updateprofieid.CompanyPreviousResultsPic1 = request.FILES.get('CompanyPreviousResultsPic1')
        else:
            updateprofieid.CompanyPreviousResultsPic1 = updateprofieid.CompanyPreviousResultsPic1
        

        if request.FILES.get('CompanyPreviousResultsPic2') is not None:
            updateprofieid.CompanyPreviousResultsPic2 = request.FILES.get('CompanyPreviousResultsPic2')
        else:
            updateprofieid.CompanyPreviousResultsPic2 = updateprofieid.CompanyPreviousResultsPic2
        

        if request.FILES.get('CompanyPreviousResultsPic3') is not None:
            updateprofieid.CompanyPreviousResultsPic3 = request.FILES.get('CompanyPreviousResultsPic3')
        else:
            updateprofieid.CompanyPreviousResultsPic3 = updateprofieid.CompanyPreviousResultsPic3
        

        if request.FILES.get('CompanyPreviousResultsPic4') is not None:
            updateprofieid.CompanyPreviousResultsPic4 = request.FILES.get('CompanyPreviousResultsPic4')
        else:
            updateprofieid.CompanyPreviousResultsPic4 = updateprofieid.CompanyPreviousResultsPic4
        

        if request.FILES.get('CompanyPreviousResultsPic5') is not None:
            updateprofieid.CompanyPreviousResultsPic5 = request.FILES.get('CompanyPreviousResultsPic5')
        else:
            updateprofieid.CompanyPreviousResultsPic5 = updateprofieid.CompanyPreviousResultsPic5
        

        if request.FILES.get('CompanyPreviousResultsPic6') is not None:
            updateprofieid.CompanyPreviousResultsPic6 = request.FILES.get('CompanyPreviousResultsPic6')
        else:
            updateprofieid.CompanyPreviousResultsPic6 = updateprofieid.CompanyPreviousResultsPic6
        

        if request.FILES.get('CompanyPreviousResultsPic7') is not None:
            updateprofieid.CompanyPreviousResultsPic7 = request.FILES.get('CompanyPreviousResultsPic7')
        else:
            updateprofieid.CompanyPreviousResultsPic7 = updateprofieid.CompanyPreviousResultsPic7
        

        if request.FILES.get('CompanyPreviousResultsPic8') is not None:
            updateprofieid.CompanyPreviousResultsPic8 = request.FILES.get('CompanyPreviousResultsPic8')
        else:
            updateprofieid.CompanyPreviousResultsPic8 = updateprofieid.CompanyPreviousResultsPic8
        

        if request.FILES.get('CompanyPreviousResultsPic9') is not None:
            updateprofieid.CompanyPreviousResultsPic9 = request.FILES.get('CompanyPreviousResultsPic9')
        else:
            updateprofieid.CompanyPreviousResultsPic9 = updateprofieid.CompanyPreviousResultsPic9
        

        if request.FILES.get('CompanyPreviousResultsPic10') is not None:
            updateprofieid.CompanyPreviousResultsPic10 = request.FILES.get('CompanyPreviousResultsPic10')
        else:
            updateprofieid.CompanyPreviousResultsPic10 = updateprofieid.CompanyPreviousResultsPic10
        

        if request.FILES.get('CompanyPreviousResultsPic11') is not None:
            updateprofieid.CompanyPreviousResultsPic11 = request.FILES.get('CompanyPreviousResultsPic11')
        else:
            updateprofieid.CompanyPreviousResultsPic11 = updateprofieid.CompanyPreviousResultsPic11
        

        if request.FILES.get('CompanyPreviousResultsPic12') is not None:
            updateprofieid.CompanyPreviousResultsPic12 = request.FILES.get('CompanyPreviousResultsPic12')
        else:
            updateprofieid.CompanyPreviousResultsPic12 = updateprofieid.CompanyPreviousResultsPic12





        if request.FILES.get('CustomerReviewsPic1') is not None:
            updateprofieid.CustomerReviewsPic1 = request.FILES.get('CustomerReviewsPic1')
        else:
            updateprofieid.CustomerReviewsPic1 = updateprofieid.CustomerReviewsPic1
        

        if request.FILES.get('CustomerReviewsPic2') is not None:
            updateprofieid.CustomerReviewsPic2 = request.FILES.get('CustomerReviewsPic2')
        else:
            updateprofieid.CustomerReviewsPic2 = updateprofieid.CustomerReviewsPic2
        

        if request.FILES.get('CustomerReviewsPic3') is not None:
            updateprofieid.CustomerReviewsPic3 = request.FILES.get('CustomerReviewsPic3')
        else:
            updateprofieid.CustomerReviewsPic3 = updateprofieid.CustomerReviewsPic3
        

        if request.FILES.get('CustomerReviewsPic4') is not None:
            updateprofieid.CustomerReviewsPic4 = request.FILES.get('CustomerReviewsPic4')
        else:
            updateprofieid.CustomerReviewsPic4 = updateprofieid.CustomerReviewsPic4
        

        if request.FILES.get('CustomerReviewsPic5') is not None:
            updateprofieid.CustomerReviewsPic5 = request.FILES.get('CustomerReviewsPic5')
        else:
            updateprofieid.CustomerReviewsPic5 = updateprofieid.CustomerReviewsPic5
        

        if request.FILES.get('CustomerReviewsPic6') is not None:
            updateprofieid.CustomerReviewsPic6 = request.FILES.get('CustomerReviewsPic6')
        else:
            updateprofieid.CustomerReviewsPic6 = updateprofieid.CustomerReviewsPic6
        

        if request.FILES.get('CustomerReviewsPic7') is not None:
            updateprofieid.CustomerReviewsPic7 = request.FILES.get('CustomerReviewsPic7')
        else:
            updateprofieid.CustomerReviewsPic7 = updateprofieid.CustomerReviewsPic7
        

        if request.FILES.get('CustomerReviewsPic8') is not None:
            updateprofieid.CustomerReviewsPic8 = request.FILES.get('CustomerReviewsPic8')
        else:
            updateprofieid.CustomerReviewsPic8 = updateprofieid.CustomerReviewsPic8
        

        if request.FILES.get('CustomerReviewsPic9') is not None:
            updateprofieid.CustomerReviewsPic9 = request.FILES.get('CustomerReviewsPic9')
        else:
            updateprofieid.CustomerReviewsPic9 = updateprofieid.CustomerReviewsPic9
        

        if request.FILES.get('CustomerReviewsPic10') is not None:
            updateprofieid.CustomerReviewsPic10 = request.FILES.get('CustomerReviewsPic10')
        else:
            updateprofieid.CustomerReviewsPic10 = updateprofieid.CustomerReviewsPic10
        

        if request.FILES.get('CustomerReviewsPic11') is not None:
            updateprofieid.CustomerReviewsPic11 = request.FILES.get('CustomerReviewsPic11')
        else:
            updateprofieid.CustomerReviewsPic11 = updateprofieid.CustomerReviewsPic11
        

        if request.FILES.get('CustomerReviewsPic12') is not None:
            updateprofieid.CustomerReviewsPic12 = request.FILES.get('CustomerReviewsPic12')
        else:
            updateprofieid.CustomerReviewsPic12 = updateprofieid.CustomerReviewsPic12

        # date = request.POST.get('datetime.today()')

        # data = SellerProfile(phone_number=request.user,ContactPersonPic=ContactPersonPic, ContactPersonName=ContactPersonName,
        #                      ContactPersonNumber=ContactPersonNumber,
        #                      ContactPersonDesigation=ContactPersonDesigation,
        #                      CompanyLogo=CompanyLogo,
        #                      CompanyName=CompanyName,
        #                      CompanyAddress=CompanyAddress,
        #                      CompanyDistrictName=CompanyDistrictName,
        #                      CompanyStateName=CompanyStateName,
        #                      CompanyEmailID=CompanyEmailID,
        #                      CompanyWebsiteLink=CompanyWebsiteLink,
        #                      CompanyLoginPhoneNo=CompanyLoginPhoneNo,
        #                      AboutCompany=AboutCompany,
        #                      SpecializationOfCompany=SpecializationOfCompany, WhyJoin=WhyJoin, date=date)
        updateprofieid.save()
        return redirect('seller_updateprofile')
    return render(request, 'seller_updateprofile.html')







def seller_view_profile(request):
    return render(request, 'seller_view_profile.html')


def seller_view_ads(request):
    return render(request, 'seller_view_ads.html')


def seller_like_ads(request):
    return render(request, 'seller_like_ads.html')


def seller_share_ads(request):
    return render(request, 'seller_share_ads.html')


def seller_share_interview(request):
    return render(request, 'seller_share_interview.html')


def seller_like_interview(request):
    return render(request, 'seller_like_interview.html')


def seller_view_interview(request):
    return render(request, 'seller_view_interview.html')


def seller_like_profile(request):
    return render(request, 'seller_like_profile.html')


def seller_share_profile(request):
    return render(request, 'seller_share_profile.html')


def seller_todays_deals(request):
    if request.method == "POST":
        from_compny_profile = SellerProfile.objects.get(pk=request.user)
        print(from_compny_profile)
        Catagery = request.POST.get('category')
        DealTitle = request.POST.get('title')
        DealPostDateandTime = request.POST.get('datetime.today()')
        DealAddDiscription = request.POST.get('dec')
        UploadAdsPhoto = request.FILES.get('AdsPic')
        print(UploadAdsPhoto)
        
        todaysdealdata = SellerTodaysDeals(from_user= request.user, from_compny_profile = from_compny_profile, DealTitle=DealTitle, Catagery=Catagery, DealPostDateandTime=DealPostDateandTime,
        DealAddDiscription=DealAddDiscription, UploadAdsPhoto=UploadAdsPhoto)
        todaysdealdata.save()
        print(UploadAdsPhoto)
        messages.success(request, "Today’s Deals is submitted Successfully..")
        # return redirect('seller_todays_deals')
    return render(request, 'seller_todays_deals.html')

def seller_offer_jobs(request):
    if request.method == "POST":
        JobTitle = request.POST.get('title')
        TotalEmployRequrid = request.POST.get('emp_req')
        WhoApply = request.POST.get('japply')
        SalaryPeriod = request.POST.get('category')
        LastDateToApply = request.POST.get('picdate')
        SalaryFrom = request.POST.get('jsfrom')
        SalaryTo = request.POST.get('jsto')
        PostionType = request.POST.get('jPosition')
        MinimumQualificationRequired = request.POST.get('jQualification')
        MinimumExperience = request.POST.get('jExperience')
        JobDiscription = request.POST.get('jdec')
        Location = request.POST.get('jLocation')
        BannerPhoto = request.FILES.get('jbanner')
        
        offerhobdata = SellerJobOffer(JobTitle=JobTitle, TotalEmployRequrid=TotalEmployRequrid,
        WhoApply=WhoApply, SalaryPeriod=SalaryPeriod,
        SalaryFrom=SalaryFrom,SalaryTo=SalaryTo,
        PostionType=PostionType,MinimumQualificationRequired=MinimumQualificationRequired,
        JobDiscription=JobDiscription,Location=Location,
        BannerPhoto=BannerPhoto,MinimumExperience=MinimumExperience,
        LastDateToApply=LastDateToApply

        )
        offerhobdata.save()
        messages.success(request, "Job Offer is submitted Successfully..")
    return render(request, 'seller_offer_jobs.html')


def seller_sell_franchise(request):
    if request.method == "POST":
        CompanyName = request.POST.get('C_Name')
        CompanyAddress = request.POST.get('C_Address')
        ContactPerson = request.POST.get('contectperonname')
        MobileNo = request.POST.get('mobilenumber')
        ContactPersonDesigation = request.POST.get('contactpersonDesigation')
        YearOfStabilization = request.POST.get('yearstablizaition')
        TotalNumberOfEmployees = request.POST.get('enum')
        DealIn = request.POST.get('edeail')
        FranchiseOfferFor = request.POST.get('C_cityy')
        AreaType = request.POST.get('c_areatype')
        TotalAreaRequired = request.POST.get('C_total_area')
        TotalInvestmentRequired = request.POST.get('C_inverster_required')
        EstimatedReturnOfInvestment = request.POST.get('C_inversted_return_estimat')
        TotalShareOfferOnSells = request.POST.get('totleinversted_return_estimat')
        UploadCompanyVisitingCard = request.FILES.get('C_card')
        
        sellfranchisedata = SellerSellFranchise(CompanyName=CompanyName,CompanyAddress=CompanyAddress,
        ContactPerson=ContactPerson,MobileNo=MobileNo,ContactPersonDesigation=ContactPersonDesigation,
        YearOfStabilization=YearOfStabilization,TotalNumberOfEmployees=TotalNumberOfEmployees,
        DealIn=DealIn,
        FranchiseOfferFor=FranchiseOfferFor,AreaType=AreaType,
        TotalAreaRequired=TotalAreaRequired,TotalInvestmentRequired=TotalInvestmentRequired,
        EstimatedReturnOfInvestment=EstimatedReturnOfInvestment,
        TotalShareOfferOnSells=TotalShareOfferOnSells,UploadCompanyVisitingCard=UploadCompanyVisitingCard
        )
        sellfranchisedata.save()
        messages.success(request, "data is submitted Successfully..")

    return render(request, 'seller_sell_franchise.html')





def seller_favorite_Customer(request):
    return render(request, 'seller_favorite_Customer.html')


def seller_intrested_visitor(request):
    letscreack = SellerProfile.objects.get(pk=request.user).WhyJoin
    userintrest = []

    a = letscreack.find('IELTS')
    b = letscreack.find('Passport')
    c = letscreack.find('Study Visa')
    d = letscreack.find('Education Loan')
    e = letscreack.find('Air Ticket')
    f = letscreack.find('Travel Insurance')
    g = letscreack.find('International Matrimonial')
    h = letscreack.find('Money Exchange')
    i = letscreack.find('Transport For Airport')
    j = letscreack.find('Luggage Adjustment')
    k = letscreack.find('Accommodation at Abroad')
    l = letscreack.find('Jobs at Abroad')
    m = letscreack.find('Tour Travel Package')
    n = letscreack.find('Work Permit')
    p = letscreack.find('Permanent Resident (PR)')
    q = letscreack.find('Tourist & Business Visa')
    r = letscreack.find('International Courier')
    s = letscreack.find('Legal Adviser')
    t = letscreack.find('Online IELTS Classes')

    if a >=0 :
        userintrest.append('IELTS')
    if b >=0 :
        userintrest.append('Passport')
    if c >=0 :
        userintrest.append('Study Visa')
    if d >=0 :
        userintrest.append('Education Loan')
    if e >=0 :
        userintrest.append('Air Ticket')
    if f >=0 :
        userintrest.append('Travel Insurance')
    if g >=0 :
        userintrest.append('International Matrimonial')
    if h >=0 :
        userintrest.append('Money Exchange')
    if i >=0 :
        userintrest.append('Transport For Airport')
    if j >=0 :
        userintrest.append('Luggage Adjustment')
    if k >=0 :
        userintrest.append('Accommodation at Abroad')
    if l >=0 :
        userintrest.append('Jobs at Abroad')
    if m >=0 :
        userintrest.append('Tour Travel Package')
    if n >=0 :
        userintrest.append('Work Permit')
    if p >=0 :
        userintrest.append('Permanent Resident (PR)')
    if q >=0 :
        userintrest.append('Tourist & Business Visa')
    if r >=0 :
        userintrest.append('International Courier')
    if s >=0 :
        userintrest.append('Legal Adviser')
    if t >=0 :
        userintrest.append('Online IELTS Classes')
    
        
    print(userintrest)
    print(type(userintrest))
    for i in userintrest:
        print(i)
    # print(a)
    # print(type(a))
  
    # print(a)
    # query = request.GET['query']
    # hotal = Add_Hotal.objects.filter(Hotal_Name__icontains=query)
    # x = list[a]
    # print(x)
    
    # for i in x:
    #     print(i)
   
    # for i in a:
    #     if i.intrestedin == 'Study Visa':
    #         print(i)

    return render(request, 'seller_intrested_visitor.html', {'userintrest':userintrest})
# email_list = User.objects.filter(is_active=True).values_list("email", flat=True)
##########################################################################3

def ilets_intrested_user(request):
    whyjoinx = douryou_login.objects.values('whyjoin')
    # print(type(whyjoinx))
    # whyjoiny = str(whyjoinx)
    # print(whyjoinx,"asdjlgasjdasdjgasjdgs")
    # users = douryou_login.objects.filter(whyjoin = if 'IELTS' in whyjoiny))
    # print(users,"thedbsae aewrwer ")
    return render(request, 'user_intrest/ilets_intrested_user.html')

def study_visa_intrested_user(request):
    return render(request, 'user_intrest/study_visa_intrested_user.html')

def passport_intrested_user(request):
    return render(request, 'user_intrest/passport_intrested_user.html')

def education_lone_intrested_user(request):
    return render(request, 'user_intrest/education_lone_intrested_user.html')

def travel_insureance_intrested_user(request):
    return render(request, 'user_intrest/travel_insureance_intrested_user.html')

def money_exchange_intrested_user(request):
    return render(request, 'user_intrest/money_exchange_intrested_user.html')

def air_ticket_intrested_user(request):
    return render(request, 'user_intrest/air_ticket_intrested_user.html')

def transport_for_airport_intrested_user(request):
    return render(request, 'user_intrest/transport_for_airport_intrested_user.html')

def tourest_bus_visa_intrested_user(request):
    return render(request, 'user_intrest/tourest_bus_visa_intrested_user.html')

def work_permit_intrested_user(request):
    return render(request, 'user_intrest/work_permit_intrested_user.html')

def job_at_abroad_intrested_user(request):
    return render(request, 'user_intrest/job_at_abroad_intrested_user.html')

def accomodation_intrested_user(request):
    return render(request, 'user_intrest/accomodation_intrested_user.html')

def permant_resident_intrested_user(request):
    return render(request, 'user_intrest/permant_resident_intrested_user.html')

def tour_and_travel_pacakage_intrested_user(request):
    return render(request, 'user_intrest/tour_and_travel_pacakage_intrested_user.html')

def international_couruer_intrested_user(request):
    return render(request, 'user_intrest/international_couruer_intrested_user.html')

def Legal_Advisor_intrested_user(request):
    return render(request, 'user_intrest/Legal_Advisor_intrested_user.html')

def online_ilet_classes_intrested_user(request):
    return render(request, 'user_intrest/online_ilet_classes_intrested_user.html')

def onlune_wekkly_test_intrested_user(request):
    return render(request, 'user_intrest/onlune_wekkly_test_intrested_user.html')






###############################################################################################################################
def seller_user_requrienment(request):
    return render(request, 'seller_user_requrienment.html')


def seller_pr_enquiry_form(request):
    return render(request, 'seller_pr_enquiry_form.html')


def seller_add_online_ielts_weeklytest(request):
    return render(request, 'seller_add_online_ielts_weeklytest.html')


def seller_dashboard_my_match(request):
    return render(request, 'seller_dashboard_my_match.html')


def seller_list_of_students(request):
    return render(request, 'seller_list_of_students.html')


def seller_book_event(request):
    return render(request, 'seller_book_event.html')


def seller_my_event(request):
    return render(request, 'seller_my_event.html')

def seller_stall_payment_getway(request):
    return render(request, 'seller_stall_payment_getway.html')

def seller_event_congratulation(request):
    return render(request, 'seller_event_congratulation.html')






# comming soon....


def seller_home_consultancy(request):
    return render(request, 'seller_home_consultancy.html')


def seller_hot_area_to_target(request):
    return render(request, 'seller_hot_area_to_target.html')


def seller_a_i_coustmor(request):
    return render(request, 'seller_a_i_coustmor.html')


def seller_demo_classes(request):
    return render(request, 'seller_demo_classes.html')


def seller_class_timing(request):
    return render(request, 'seller_class_timing.html')


def seller_student_fee(request):
    return render(request, 'seller_student_fee.html')


def seller_my_classroom(request):
    return render(request, 'seller_my_classroom.html')
