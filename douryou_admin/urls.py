from django.contrib import admin
from django.urls import path, include
from douryou_admin import views



urlpatterns = [
    path("admin-login", views.admin_login, name='admin_login'),

    path("admin-edit-plans", views.admin_edit_plans, name='admin_edit_plans'),
    path("admin-seller-user-request-approval", views.user_seler_request_aproval, name='user_seler_request_aproval'),

    # path("admin-view-seller-profile", views.admin_view_seller_profile, name='admin_view_seller_profile'),
    path("admin-aprove-seller-request/<int:TodaysDealID>", views.admin_aprove_Seller_reqest, name='admin-aprove-seller-request'),
    path("admin-reject-seller-request/<int:TodaysDealID>", views.admin_reject_selller_request, name='admin_reject_selller_request'),
    ###############################################
    path("admin-seller-user-request-approval", views.user_seler_holding_request_for_aproval, name='user_seler_holding_request_for_aproval'),
    ###########################################
    path("admin-handle-user-request", views.admin_hendle_user_request, name='admin_hendle_user_request'),
    path("admin-handle-all-users", views.admin_all_user, name='admin_all_user'),
    path("admin-handle-all-seller", views.admin_handle_all_seller, name='admin_handle_all_seller'),
    path("admin-handle-events", views.admin_handel_events, name='admin_handel_events'),
    path("admin-add-new-events", views.admin_add_new_event, name='admin_add_new_event'),
    path("admin-handel-videos", views.admin_videos, name='admin_videos'),
    path("admin-add-new-video", views.admin_add_new_video, name='admin_add_new_video'),
    path("admin-send-notifications", views.admin_send_notification, name='admin_send_notification'),
    path("admin-my-match", views.admin_my_match, name='admin_my_match'),
    path("admin-add-new-my-match", views.admin_add_new_my_match, name='admin_add_new_my_match'),
    path("admin-premium-users", views.admin_premium_user, name='admin_premium_user'),
    path("admin-staff", views.admin_staff, name='admin_staff'),
]