from django.contrib import admin
from django.urls import path, include
from douryou_seller import views



urlpatterns = [
    path("seller-login", views.seller_login, name='seller_login'),
    # path("seller-verify-otp", views.seller_signup, name='seller_signup'),
    path("seller-otp-verify", views.seller_otp, name='seller_otp'),

    path("seller-create-profile1", views.seller_createprofile1, name='seller_createprofile1'),
    path("seller-create-profile-company-images", views.seller_images, name='seller_images'),
    path("seller-create-profile-buy-Your-plan", views.buy_your_plan, name='buy_your_plan'),
    path("payment-getway-buy-plan", views.payment_getway, name='payment_getway'),
# seller profile ............
    path("seller-profile", views.seller_profile, name='seller_profile'),
    path("seller-update-profile", views.seller_updateprofile, name='seller_updateprofile'),
    path("seller-edit-profile", views.seller_editprofile, name='seller_editprofile'),

# Your Coustmor...
    path("seller-dashbord-view-ads", views.seller_view_ads, name='seller_view_ads'),
    path("seller-dashbord-like-ads", views.seller_like_ads, name='seller_like_ads'),
    path("seller-dashbord-share-ads", views.seller_share_ads, name='seller_share_ads'),
    path("seller-dashbord-share-interview", views.seller_share_interview, name='seller_share_interview'),
    path("seller-dashbord-like-interview", views.seller_like_interview, name='seller_like_interview'),
    path("seller-dashbord-view-interview", views.seller_view_interview, name='seller_view_interview'),
    path("seller-dashbord-view-profiles", views.seller_view_profile, name='seller_view_profile'),
    path("seller-dashbord-like-profiles", views.seller_like_profile, name='seller_like_profile'),
    path("seller-dashbord-share-profiles", views.seller_share_profile, name='seller_share_profile'),

    path("seller-dashbord-add-todays-deals", views.seller_todays_deals, name='seller_todays_deals'),
    path("seller-dashbord-add-offer-jobs", views.seller_offer_jobs, name='seller_offer_jobs'),
    path("seller-dashbord-add-sell-franchise", views.seller_sell_franchise, name='seller_sell_franchise'),

    path("seller-dashbord-favorite-Customer", views.seller_favorite_Customer, name='seller_favorite_Customer'),

    path("seller-dashbord-Intersted-Visitor", views.seller_intrested_visitor, name='seller_intrested_visitor'),
    ##########################################################################################################################################################
    path("seller-dashbord-Intersted-Visitor-IELTS", views.ilets_intrested_user, name='ilets_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Study-Visa", views.study_visa_intrested_user, name='study_visa_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Passport", views.passport_intrested_user, name='passport_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Education-Loan", views.education_lone_intrested_user, name='education_lone_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Trevel-Insurance", views.travel_insureance_intrested_user, name='travel_insureance_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Money-Exchange", views.money_exchange_intrested_user, name='money_exchange_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Air-Ticket", views.air_ticket_intrested_user, name='air_ticket_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Transport-for-Airport", views.transport_for_airport_intrested_user, name='transport_for_airport_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Tourist-or-Business-visa", views.tourest_bus_visa_intrested_user, name='tourest_bus_visa_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Work-Permit", views.work_permit_intrested_user, name='work_permit_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Jobs at-Abroad", views.job_at_abroad_intrested_user, name='job_at_abroad_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Accommodation-at-Abroad", views.accomodation_intrested_user, name='accomodation_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Permanent-Resident", views.permant_resident_intrested_user, name='permant_resident_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Tour-or-Travel-Package", views.tour_and_travel_pacakage_intrested_user, name='tour_and_travel_pacakage_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-International-Courier", views.international_couruer_intrested_user, name='international_couruer_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Legal-Advisor", views.Legal_Advisor_intrested_user, name='Legal_Advisor_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Onliine-IELTS-Class", views.online_ilet_classes_intrested_user, name='online_ilet_classes_intrested_user'),
    path("seller-dashbord-Intersted-Visitor-Online-Weekly-IELTS-Test", views.onlune_wekkly_test_intrested_user, name='onlune_wekkly_test_intrested_user'),
    ##########################################################################################################################################################
    path("seller-dashbord-user-requrienment", views.seller_user_requrienment, name='seller_user_requrienment'),

    path("seller-dashbord-PR-Enquiry-Form", views.seller_pr_enquiry_form, name='seller_pr_enquiry_form'),

    path("seller-dashbord-post-online-IELTS-weekly-test", views.seller_add_online_ielts_weeklytest, name='seller_add_online_ielts_weeklytest'),
    path("seller-dashbord-my-match", views.seller_dashboard_my_match, name='seller_dashboard_my_match'),

    path("seller-dashbord-list-of-students", views.seller_list_of_students, name='seller_list_of_students'),

    path("seller-dashbord-book-event", views.seller_book_event, name='seller_book_event'),
    path("seller-dashbord-my-event", views.seller_my_event, name='seller_my_event'),
    path("seller-dashbord-my-event-stall-payment-getway", views.seller_stall_payment_getway, name='seller_stall_payment_getway'),
    path("seller-dashbord-my-event-stall-pass", views.seller_event_congratulation, name='seller_event_congratulation'),




    # comming soon

    path("seller-dashbord-Home-Cunsultancy", views.seller_home_consultancy, name='seller_home_consultancy'),
    path("seller-dashbord-hot-area-to-target", views.seller_hot_area_to_target, name='seller_hot_area_to_target'),
    path("seller-dashbord-A-I-customers", views.seller_a_i_coustmor, name='seller_a_i_coustmor'),

    path("seller-dashbord-demo-classes", views.seller_demo_classes, name='seller_demo_classes'),
    path("seller-dashbord-class-timing", views.seller_class_timing, name='seller_class_timing'),
    path("seller-dashbord-students-fee", views.seller_student_fee, name='seller_student_fee'),
    path("seller-dashbord-my-classroom", views.seller_my_classroom, name='seller_my_classroom'),
]