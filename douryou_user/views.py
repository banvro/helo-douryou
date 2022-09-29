from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from douryou_user.serializers import Your_RequirementSerializer, Education_LoanSerializer, Appy_Job_RequirementSerializer, ApplyLuggageAdliodtmetSerializer, PassportSerializer, Douryou_LoginSerializer, Travel_InsuranceSerializer, ApplyPurchaseFrancbiseSerializer
from douryou_user.models import your_requirement,education_loan,travel_insurance,appy_job_requirement, passport, douryou_login, ApplyLuggageAdliodtmet, ApplyPurchaseFrancbise

# from  rest_framework.exceptions import AuthenticationFailed
import os
from twilio.rest import Client
from rest_framework import status
# Create views for mobie number registration..
from django.conf import settings

# Your Requirement all views..............................
@api_view(['GET'])
def AllYourRequirement(request):
    show_all_user = your_requirement.objects.all()
    serializer = Your_RequirementSerializer(show_all_user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewSingleYourReqirement(request, pk):
    show_single_user_detail = your_requirement.objects.get(id=pk)
    serializer = Your_RequirementSerializer(show_single_user_detail, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AddNewRequirement(request):
    serializer = Your_RequirementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Education loan all views..............................
@api_view(['GET'])
def AllEducationLoan(request):
    show_all_user = education_loan.objects.all()
    serializer = Education_LoanSerializer(show_all_user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewSingleEducationLoan(request, pk):
    show_single_user_detail = education_loan.objects.get(id=pk)
    serializer = Education_LoanSerializer(show_single_user_detail, many=False)
    return Response(serializer.data)
@api_view(['POST'])
def AddNewEducationLone(request):
    serializer = Education_LoanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Travel Insurance all views..............................
@api_view(['GET'])
def AllTravelInsurance(request):
    show_all_user = travel_insurance.objects.all()
    serializer = Travel_InsuranceSerializer(show_all_user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewSingleTravelInsurance(request, pk):
    show_single_user_detail = travel_insurance.objects.get(id=pk)
    serializer = Travel_InsuranceSerializer(show_single_user_detail, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AddNewTravelInsurance(request):
    serializer = Travel_InsuranceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Appy Job Requirement all views..............................
@api_view(['GET'])
def AllAppyJobRequirement(request):
    show_all_user = appy_job_requirement.objects.all()
    serializer = Appy_Job_RequirementSerializer(show_all_user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewAppyJobRequirement(request, pk):
    show_single_user_detail = appy_job_requirement.objects.get(id=pk)
    serializer = Appy_Job_RequirementSerializer(show_single_user_detail, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AddNewJobRequirement(request):
    serializer = Appy_Job_RequirementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Passport all views..............................
@api_view(['GET'])
def AllPassport(request):
    show_all_user = passport.objects.all()
    serializer = PassportSerializer(show_all_user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewSinglePassport(request, pk):
    show_single_user_detail = passport.objects.get(id=pk)
    serializer = PassportSerializer(show_single_user_detail, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AddNewPassport(request):
    serializer = PassportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




# Douryou Login all views..............................
@api_view(['GET'])
def AllDouryouLogin(request):
    show_all_user = douryou_login.objects.all()
    serializer = Douryou_LoginSerializer(show_all_user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewSingleDouryouLogin(request, pk):
    show_single_user_detail = douryou_login.objects.get(id=pk)
    serializer = Douryou_LoginSerializer(show_single_user_detail, many=False)
    return Response(serializer.data)

# @api_view(['POST'])
# def AddNewDouryouLogin(request):
#     serializer = Douryou_LoginSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

@api_view(['POST'])
def AddNewDouryouLogin(request):
    serializer = Douryou_LoginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    # except:
        # number = request.POST.get('number')
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # intrestedin = request.POST.get('intrestedin')
        # photo = request.POST.get('photo')
        # photo = request.FILES.get('photo')
        # whyjoin = request.POST.get('whyjoin')
        # user = douryou_login(number=number, name=name, email=email,intrestedin=intrestedin,
        # photo=photo,whyjoin=whyjoin)
        # user.save()
        # return Response('user data is save', status=status.HTTP_200_OK)


# Apply Luggage Adliodtmet all views..............................
@api_view(['GET'])
def AllApplyLuggageAdliodtmet(request):
    show_all_user = ApplyLuggageAdliodtmet.objects.all()
    serializer = ApplyLuggageAdliodtmetSerializer(show_all_user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewSingleApplyLuggageAdliodtmet(request, pk):
    show_single_user_detail = ApplyLuggageAdliodtmet.objects.get(id=pk)
    serializer = ApplyLuggageAdliodtmetSerializer(show_single_user_detail, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AddNewLuggageAdliodtmet(request):
    serializer = ApplyLuggageAdliodtmetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Apply Purchase Francbise all views..............................
@api_view(['GET'])
def AllApplyPurchaseFrancbise(request):
    show_all_user = ApplyPurchaseFrancbise.objects.all()
    serializer = ApplyPurchaseFrancbiseSerializer(show_all_user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewSingleApplyPurchaseFrancbise(request, pk): 
    show_single_user_detail = ApplyPurchaseFrancbise.objects.get(id=pk)
    serializer = ApplyPurchaseFrancbiseSerializer(show_single_user_detail, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AddNewPurchaseFrancbise(request):
    serializer = ApplyPurchaseFrancbiseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)










from douryou_seller.models import SellerTodaysDeals, SellerProfile
from douryou_user.serializers import SellerTodaysDealsSerializer
###################### strat new task about show ads to user........ ################3333

# @api_view(['GET'])
# def viewAllSellerTodaysDeals(request):
#     show_all_today_deals = SellerTodaysDeals.objects.all().filter(Approved=True)
#     serializer = SellerTodaysDealsSerializer(show_all_today_deals, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def viewAllSellerTodaysDeals(request):
    show_all_today_deals = SellerTodaysDeals.objects.all().filter(Approved=True)
    serializer = SellerTodaysDealsSerializer(show_all_today_deals, many=True)

    # show_all_today_deals = SellerProfile.objects.all()
    # serializer = SellerProfileSerializer(show_all_today_deals, many=True)
    
    return Response({"todaysdeals": serializer.data})





























# @api_view(['GET'])
# def ShowAll_number(request):
#     show_all_user = User_Registration_with_mobile_number.objects.all()
#     serializer = User_RegistrationSerializer_with_mobile_number(show_all_user, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def ViewUser_Registration_number(request, pk):
#     show_single_user_detail = User_Registration_with_mobile_number.objects.get(id=pk)
#     serializer = User_RegistrationSerializer_with_mobile_number(show_single_user_detail, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def CreateUser_Registration_number(request):
#     serializer = User_RegistrationSerializer_with_mobile_number(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['POST'])
# def updateUser_Registration_number(request, pk):
#     update_user = User_Registration_with_mobile_number.objects.get(id=pk)
#     serializer = User_RegistrationSerializer_with_mobile_number(instance=update_user, data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['GET'])
# def deleteUser_Registration_number(request, pk):
#     delete_user = User_Registration_with_mobile_number.objects.get(id=pk)
#     delete_user.delete()

#     return Response('Items delete successfully!')




# # Create your views for gmail registrations...


# @api_view(['GET'])
# def ShowAll_email(request):
#     show_all_user = User_Registration_with_email.objects.all()
#     serializer = User_RegistrationSerializer_with_Email_id(show_all_user, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def ViewUser_Registration_email(request, pk):
#     show_single_user_detail = User_Registration_with_email.objects.get(id=pk)
#     serializer = User_RegistrationSerializer_with_Email_id(show_single_user_detail, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def CreateUser_Registration_email(request):
#     serializer = User_RegistrationSerializer_with_Email_id(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)



# @api_view(['POST'])
# def updateUser_Registration_email(request, pk):
#     update_user = User_Registration_with_email.objects.get(id=pk)
#     serializer = User_RegistrationSerializer_with_Email_id(instance=update_user, data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['GET'])
# def deleteUser_Registration_email(request, pk):
#     delete_user = User_Registration_with_email.objects.get(id=pk)
#     delete_user.delete()

#     return Response('Items delete successfully!')




# # Create your views for facebook registration



# @api_view(['GET'])
# def ShowAll_facebook(request):
#     show_all_user = User_Registration_with_facebook.objects.all()
#     serializer = User_RegistrationSerializer_with_facebook_id(show_all_user, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def ViewUser_Registration_facebook(request, pk):
#     show_single_user_detail = User_Registration_with_facebook.objects.get(id=pk)
#     serializer = User_RegistrationSerializer_with_facebook_id(show_single_user_detail, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def CreateUser_Registration_facebook(request):
#     serializer = User_RegistrationSerializer_with_facebook_id(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)



# @api_view(['POST'])
# def updateUser_Registration_facebook(request, pk):
#     update_user = User_Registration_with_facebook.objects.get(id=pk)
#     serializer = User_RegistrationSerializer_with_facebook_id(instance=update_user, data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['GET'])
# def deleteUser_Registration_facebook(request, pk):
#     delete_user = User_Registration_with_facebook.objects.get(id=pk)
#     delete_user.delete()

#     return Response('Items delete successfully!')



# @api_view(['GET'])
# def apiOverview(request):
#     return HttpResponse('THIS is first page!')





# #############################################


# @api_view(['POST'])
# def Check_facebook_validation(request):
    
#     usrid = request.data["usrid"]
#     print(usrid)
#     valid_user = User_Registration_with_facebook.objects.filter(usrid=usrid)
#     x = User_RegistrationSerializer_with_facebook_id(valid_user, many=True)
#     userdetail = x.data
#     print("this is x",x.data)
        
#     if x.data == [] :
#         return Response({
#             "data":{"value": "facebook"}
#              } ,status=status.HTTP_403_FORBIDDEN)

#     return Response({"userdetail": userdetail ,
        
#         "message" : "User Found", 
     
#     })

# @api_view(['POST'])
# def Check_email_validation(request):
    
#     usrid = request.data["usrid"]
      
#     valid_user = User_Registration_with_email.objects.filter(usrid=usrid)
#     x = User_RegistrationSerializer_with_Email_id(valid_user, many=True)
#     userdetail = x.data
#     print("this is x",userdetail)
        
#     if x.data == [] :
#       return Response({
       
#             "data":{"value": "google"}
             
#     }, status=status.HTTP_403_FORBIDDEN)
    
#     return Response({"userdetail":userdetail,
        
#         "message" : "User Found", 
      
#     })


# ######################################3

# # Twilio otp... system...

# @api_view(['POST'])
# def send_otp(request):
    
#     usrid = request.data["usrid"]
#     print(usrid)
    
#     # account_sid = os.environ['TWILIO_ACCOUNT_SID']
#     # auth_token = os.environ['TWILIO_AUTH_TOKEN']
#     account_sid = settings.TWILIO_ACCOUNT_SID
#     auth_token = settings.TWILIO_AUTH_TOKEN
#     print(account_sid, auth_token)
#     print(settings.TWILIO_AUTH_URL)
#     client = Client(account_sid," + ", auth_token)
#     print("this is lintttrre", client)

#     verification = client.verify \
#                          .v2 \
#                          .services('VA8ef5b94e11faf0bdbd247b823f780a0c') \
#                          .verifications \
#                          .create(to=usrid, channel='sms')

#     print(verification.status)

#     return Response({
#         "message" : "Success"
#     })



# @api_view(['POST'])
# def varify_otp(request):
    
#     usrid = request.data["usrid"]
#     code = request.data["code"]
#     print(usrid)
    
#     account_sid = settings.TWILIO_ACCOUNT_SID
#     auth_token = settings.TWILIO_AUTH_TOKEN

#     client = Client(account_sid, auth_token)

#     verification_check = client.verify \
#                                .v2 \
#                                .services(settings.TWILIO_AUTH_URL) \
#                                .verification_checks \
#                                .create(to=usrid, code=code)

#     print(verification_check.status)
#     x=verification_check.status

#     if x== "approved":
#         # usrid = request.data["usrid"]
       
#         valid_user = User_Registration_with_mobile_number.objects.filter(usrid=usrid)
#         x = User_RegistrationSerializer_with_mobile_number(valid_user, many=True)
        
#         userdetail = x.data
            
#         if x.data == [] :
           
#            return Response({
#             "data":{"value": "User"}
#              },status=status.HTTP_403_FORBIDDEN)
        
#         return Response({"data":userdetail,
            
#             "message" : "Mobile number exist", 
#             "value": "message"
#         })

 
   


#     else:
#         return Response({
#             "message" : "OTP Incorrect"
#         },status=status.HTTP_400_BAD_REQUEST)




'''
facebook{
,https://eatmatekiapi.herokuapp.com/api/Check_facebook_validation/,
https://eatmatekiapi.herokuapp.com/api/Add_new_user_facebook/,}

phonenumber{
https://eatmatekiapi.herokuapp.com/api/send_otp/,
https://eatmatekiapi.herokuapp.com/api/varify_otp/,
https://eatmatekiapi.herokuapp.com/api/Add_new_user_nu/,

}

gmail{
,https://eatmatekiapi.herokuapp.com/api/Add_new_user_email/,
https://eatmatekiapi.herokuapp.com/api/Check_email_validation/,}
}
'''