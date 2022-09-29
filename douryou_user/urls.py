from django.urls import path
from douryou_user import views

urlpatterns = [

    # Your Requirement all urls..............................
    path('all-your-requirement-list/', views.AllYourRequirement, name='all_your_requirement_list'),
    path('your-requirement-number/<int:pk>/', views.ViewSingleYourReqirement, name='your_requirement_single'),
    path('Add-new-your-requirement/', views.AddNewRequirement, name='Add_new_your_requirement'),


    # Education Lone all urls..............................
    path('all-education-lone-list/', views.AllEducationLoan, name='all_education_lone_list'),
    path('education-lone-number/<int:pk>/', views.ViewSingleEducationLoan, name='education_lone_single'),
    path('Add-new-education-lone/', views.AddNewEducationLone, name='Add_new_your_requirement'),

    # Travel Insurance all urls..............................
    path('all-travel-insurance-list/', views.AllTravelInsurance, name='all_travel_insurance_list'),
    path('travel-insurance-number/<int:pk>/', views.ViewSingleTravelInsurance, name='travel_insurance_single'),
    path('Add-new-travel-insurance/', views.AddNewTravelInsurance, name='Add_new_your_requirement'),

    # Appy Job Requirement all urls..............................
    path('all-job-requirement-list/', views.AllAppyJobRequirement, name='all_job_requirement_list'),
    path('job-requirement-number/<int:pk>/', views.ViewAppyJobRequirement, name='job_requirement_single'),
    path('Add-new-job-requirement/', views.AddNewJobRequirement, name='Add_new_your_requirement'),

    # Passport all urls..............................
    path('all-passport-list/', views.AllPassport, name='all_passport_list'),
    path('passport-number/<int:pk>/', views.ViewSinglePassport, name='your_passport_single'),
    path('Add-new-passport/', views.AddNewPassport, name='Add_new_passport'),

    # Douryou Login all urls..............................
    path('all-douryou-logins-list/', views.AllDouryouLogin, name='all_douryou_logins_list'),
    path('douryou-logins-number/<int:pk>/', views.ViewSingleDouryouLogin, name='douryou_logins_single'),
    path('Add-new-douryou-logins/', views.AddNewDouryouLogin, name='Add_new_douryou_logins'),

    # Apply Luggage Adliodtmet all urls..............................
    path('all-apply-luggage-adliodtmett-list/', views.AllApplyLuggageAdliodtmet, name='all_apply_luggage_adliodtmett_list'),
    path('apply-luggage-adliodtmett-number/<int:pk>/', views.ViewSingleApplyLuggageAdliodtmet, name='apply_luggage_adliodtmett_single'),
    path('Add-new-apply-luggage-adliodtmett/', views.AddNewLuggageAdliodtmet, name='Add_new_apply_luggage_adliodtmett'),

    # Apply Purchase Francbise all urls..............................
    path('all-apply-purchase-francbise-list/', views.AllApplyPurchaseFrancbise, name='all_apply_purchase_francbise_list'),
    path('apply-purchase-francbise-number/<int:pk>/', views.ViewSingleApplyPurchaseFrancbise, name='apply_purchase_francbise_single'),
    path('Add-new-apply-purchase-francbise/', views.AddNewPurchaseFrancbise, name='Add_new_apply_purchase_francbise'),

###################### strat new task about show ads to user........ ################3333
    path('all-seller-todays-deals-list/', views.viewAllSellerTodaysDeals, name='viewAllSellerTodaysDeals'),


]
