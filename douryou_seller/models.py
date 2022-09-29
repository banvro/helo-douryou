from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# from douryou.models import User
# Create your models here.
# Genrate and verify otp

# class UserLogin(models.Model):
#     phone_number = models.CharField(max_length=120, primary_key=True)
#     Code = models.CharField(max_length=20, null=True, blank=True)

#     def __str__(self):
#         return str(self.phone_number)


class SellerProfile(models.Model):
    phone_number = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    # CompanyHelpID = models.AutoField()
    ContactPersonName = models.CharField(max_length=130, null=True, blank=True)
    ContactPersonNumber = models.CharField(max_length=210, null=True, blank=True)
    ContactPersonDesigation = models.CharField(max_length=200, null=True, blank=True)
    ContactPersonPic = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    
    CompanyName = models.CharField(max_length=140, null=True, blank=True)
    CompanyAddress = models.CharField(max_length=255, null=True, blank=True)
    CompanyDistrictName = models.CharField(max_length=140, null=True, blank=True)
    CompanyStateName = models.CharField(max_length=140, null=True, blank=True)
    CompanyEmailID = models.CharField(max_length=140, null=True, blank=True)
    CompanyWebsiteLink = models.CharField(max_length=140, null=True, blank=True)
    CompanyLoginPhoneNo = models.CharField(max_length=140, null=True, blank=True)
    otp = models.CharField(max_length=7, default="1234")
    CompanyLogo = models.ImageField(upload_to='douryouimages', null=True, blank=True)

    AboutCompany = models.CharField(max_length=255, null=True, blank=True)
    SpecializationOfCompany = models.CharField(max_length=255, null=True, blank=True)

    WhyJoin = models.CharField(max_length=240, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True, null=True)

 
    # images hendal in database 
    OfficePic1 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    OfficePic2 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    OfficePic3 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    OfficePic4 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    OfficePic5 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    OfficePic6 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    OfficePic7 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    OfficePic8 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    OfficePic9 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    OfficePic10 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    OfficePic11 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    OfficePic12 = models.ImageField(upload_to='douryouimages', null=True, blank=True)

    CompanyCertificationPic1 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyCertificationPic2 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyCertificationPic3 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyCertificationPic4 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyCertificationPic5 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyCertificationPic6 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyCertificationPic7 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyCertificationPic8 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyCertificationPic9 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyCertificationPic10 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyCertificationPic11 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyCertificationPic12 = models.ImageField(upload_to='douryouimages', null=True, blank=True)

    CompanyPreviousResultsPic1 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyPreviousResultsPic2 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyPreviousResultsPic3 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyPreviousResultsPic4 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyPreviousResultsPic5 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyPreviousResultsPic6 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyPreviousResultsPic7 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyPreviousResultsPic8 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyPreviousResultsPic9 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyPreviousResultsPic10 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyPreviousResultsPic11 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CompanyPreviousResultsPic12 = models.ImageField(upload_to='douryouimages', null=True, blank=True)

    CustomerReviewsPic1 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CustomerReviewsPic2 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CustomerReviewsPic3 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CustomerReviewsPic4 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CustomerReviewsPic5 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CustomerReviewsPic6 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CustomerReviewsPic7 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CustomerReviewsPic8 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CustomerReviewsPic9 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CustomerReviewsPic10 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CustomerReviewsPic11 = models.ImageField(upload_to='douryouimages', null=True, blank=True)
    CustomerReviewsPic12 = models.ImageField(upload_to='douryouimages', null=True, blank=True)

    PORFENSSIONAL_Plan = models.BooleanField(default=False)
    BUSINESS_Plan = models.BooleanField(default=False)
    ULTIMATE_Plan = models.BooleanField(default=False)

    is_payment_done = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.phone_number.ContactPersonName
        # +" "+self.user.last_name
    @property
    def get_instance(self):
        return self 

    def __str__(self):
        return str(self.CompanyName)





# Post Your Offer section

class SellerTodaysDeals(models.Model):
    from_user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    from_compny_profile = models.ForeignKey(SellerProfile, on_delete = models.CASCADE, null=True)
    TodaysDealID = models.AutoField(primary_key=True)
    Catagery = models.CharField(max_length=230, null=True, blank=True)
    DealTitle = models.CharField(max_length=230, null=True, blank=True)
    DealPostDateandTime = models.DateTimeField(auto_now_add=True)
    DealAddDiscription = models.TextField(max_length=230, null=True, blank=True)
    Approved = models.BooleanField(default=False)
    Panding = models.BooleanField(default=False)
    UploadAdsPhoto = models.ImageField(upload_to='douryouimages', null=True, blank=True)

    class Meta:
        ordering = ('-TodaysDealID',)


    def __str__(self):
        return str(self.DealTitle)

class SellerJobOffer(models.Model):
    JobOfferID = models.AutoField(primary_key=True)
    JobTitle = models.CharField(max_length=255, null=True, blank=True)
    TotalEmployRequrid = models.CharField(max_length=255, null=True, blank=True)
    LastDateToApply = models.CharField(max_length=255, null=True, blank=True)
    WhoApply = models.CharField(max_length=255, null=True, blank=True)
    SalaryPeriod = models.CharField(max_length=255, null=True, blank=True)
    SalaryFrom = models.CharField(max_length=255, null=True, blank=True)
    SalaryTo = models.CharField(max_length=255, null=True, blank=True)
    PostionType = models.CharField(max_length=255, null=True, blank=True)
    MinimumQualificationRequired = models.CharField(max_length=500, null=True, blank=True)
    MinimumExperience = models.CharField(max_length=255, null=True, blank=True)
    JobDiscription = models.TextField(max_length=255, null=True, blank=True)
    Location = models.CharField(max_length=255, null=True, blank=True)
    Approved = models.BooleanField(default=False)
    BannerPhoto = models.ImageField(upload_to='douryouimages', null=True, blank=True)

    def __str__(self):
        return str(self.JobTitle)


class SellerSellFranchise(models.Model):
    FranchiseID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=255, null=True, blank=True)
    CompanyAddress = models.CharField(max_length=255, null=True, blank=True)
    ContactPerson = models.CharField(max_length=255, null=True, blank=True)
    MobileNo = models.CharField(max_length=255, null=True, blank=True)
    ContactPersonDesigation = models.CharField(max_length=255, null=True, blank=True)
    YearOfStabilization = models.CharField(max_length=255, null=True, blank=True)
    TotalNumberOfEmployees = models.CharField(max_length=255, null=True, blank=True)
    DealIn = models.CharField(max_length=255, null=True, blank=True)
    FranchiseOfferFor = models.CharField(max_length=255, null=True, blank=True)
    AreaType = models.CharField(max_length=255, null=True, blank=True)
    TotalAreaRequired = models.CharField(max_length=255, null=True, blank=True)
    TotalInvestmentRequired = models.CharField(max_length=255, null=True, blank=True)
    EstimatedReturnOfInvestment = models.CharField(max_length=255, null=True, blank=True)
    TotalShareOfferOnSells = models.CharField(max_length=255, null=True, blank=True)
    Approved = models.BooleanField(default=False)
    UploadCompanyVisitingCard = models.ImageField(upload_to='douryouimages', null=True, blank=True)

    def __str__(self):
        return str(self.CompanyName)


