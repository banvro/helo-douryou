from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 
from douryou_seller.models import SellerTodaysDeals, SellerProfile
from douryou_admin.models import  AddnewVideo
from douryou_seller import models
from douryou_user.models import douryou_login


# Create your views here.

def admin_login(request):            
    return render(request, 'admin_login.html') 

def admin_edit_plans(request):            
    return render(request, 'admin_edit_plans.html') 

def user_seler_request_aproval(request): 
    # profiledata = SellerProfile.objects.get() 
    sellerreq = SellerTodaysDeals.objects.all().filter(Approved=False)
    for z in sellerreq:
        print(z.TodaysDealID)
    print(sellerreq)
    whoreq = []
    for req in sellerreq:
        print(req.from_user)
        # get_data = SellerProfile.objects.get(phone_number=req.from_user)
        # print(get_data)
        try:
            get_from = SellerProfile.objects.get(phone_number=req.from_user)
            whoreq.append(get_from)
        except:
            pass
        
        # print(get_from)
        
        

    
    print(whoreq)
    # whoreq = SellerProfile.objects.get(phone_number=req.from_user)
    # print(whoreq)
    # for i in whoreq:
    # whoreq = 
    # deal_req=[]
    # request_by=[]
    # for req in sellerreq:
    #     what_req=User.objects.all().filter(id=req.id)
    #     req_by=SellerProfile.objects.all().filter(id = req.sellerprofile.id)
    #     deal_req.append(deal_req)
    #     request_by.append(request_by)
    
    # print(deal_req, request_by)
        

    # context = {'sellerreq' : sellerreq, 'whoreq' : whoreq}          
    context = {'data' : zip(whoreq, sellerreq)}          
    return render(request, 'user_seler_request_aproval.html', context)  


# def admin_view_seller_profile(request, TodaysDealID):
#     if request.method=='POST':
#         make_approve = SellerTodaysDeals.objects.get(TodaysDealID=TodaysDealID)
#     return render(request, 'admin_view_seller_profile.html') 

def admin_aprove_Seller_reqest(request, TodaysDealID):
    if request.method=='POST':
        make_approve = SellerTodaysDeals.objects.get(TodaysDealID=TodaysDealID)
        make_approve.Approved = True
        make_approve.save()
        return redirect('user_seler_request_aproval')
    return render(request, 'user_seler_request_aproval.html') 

def admin_reject_selller_request(request, TodaysDealID):
    if request.method=='POST':
        make_approve = SellerTodaysDeals.objects.get(TodaysDealID=TodaysDealID)
        make_approve.Panding = True
        make_approve.save()
        return redirect('user_seler_request_aproval')
    return render(request, 'user_seler_request_aproval.html')




##########################################################################3
def user_seler_holding_request_for_aproval(request):            
    return render(request, 'user_seler_holding_request_for_aproval.html') 
########################################################################################3333
def admin_hendle_user_request(request):            
    return render(request, 'admin_hendle_user_request.html') 

def admin_all_user(request):
    data=douryou_login.objects.all()
    return render(request, 'admin_all_user.html',{'data':data}) 

def admin_handle_all_seller(request):            
    return render(request, 'admin_handle_all_seller.html') 

def admin_handel_events(request):            
    return render(request, 'admin_handel_events.html') 

def admin_add_new_event(request):            
    return render(request, 'admin_add_new_event.html') 

def admin_videos(request):            
    return render(request, 'admin_videos.html') 


def admin_add_new_video(request): 
    if request.method=="POST":
        video_name=request.POST["video_name"]           
        category_name=request.POST["category_name"]
        video_title=request.POST["video_title"]
        select_seller=request.POST["select_seller"]
        video_link=request.POST["video_link"]
        thumbnail_link=request.POST["thumbnail_link"]
        data=AddnewVideo(video_name=video_name,category_name=category_name,video_title=video_title,select_seller=select_seller,video_link=video_link,thumbnail_link=thumbnail_link)
        data.save()
        messages.success(request,"Data added Sucessfully")
        return redirect('admin_add_new_video')
    return render(request, 'admin_add_new_video.html') 

def admin_send_notification(request):            
    return render(request, 'admin_send_notification.html') 

def admin_my_match(request):            
    return render(request, 'admin_my_match.html') 

def admin_add_new_my_match(request):            
    return render(request, 'admin_add_new_my_match.html') 

def admin_premium_user(request):            
    return render(request, 'admin_premium_user.html') 

def admin_staff(request):            
    return render(request, 'admin_staff.html') 