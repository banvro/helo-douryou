# Generated by Django 4.0.5 on 2022-09-05 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerJobOffer',
            fields=[
                ('JobOfferID', models.AutoField(primary_key=True, serialize=False)),
                ('JobTitle', models.CharField(blank=True, max_length=255, null=True)),
                ('TotalEmployRequrid', models.CharField(blank=True, max_length=255, null=True)),
                ('LastDateToApply', models.CharField(blank=True, max_length=255, null=True)),
                ('WhoApply', models.CharField(blank=True, max_length=255, null=True)),
                ('SalaryPeriod', models.CharField(blank=True, max_length=255, null=True)),
                ('SalaryFrom', models.CharField(blank=True, max_length=255, null=True)),
                ('SalaryTo', models.CharField(blank=True, max_length=255, null=True)),
                ('PostionType', models.CharField(blank=True, max_length=255, null=True)),
                ('MinimumQualificationRequired', models.CharField(blank=True, max_length=500, null=True)),
                ('MinimumExperience', models.CharField(blank=True, max_length=255, null=True)),
                ('JobDiscription', models.TextField(blank=True, max_length=255, null=True)),
                ('Location', models.CharField(blank=True, max_length=255, null=True)),
                ('Approved', models.BooleanField(default=False)),
                ('BannerPhoto', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
            ],
        ),
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('phone_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ContactPersonName', models.CharField(blank=True, max_length=130, null=True)),
                ('ContactPersonNumber', models.CharField(blank=True, max_length=210, null=True)),
                ('ContactPersonDesigation', models.CharField(blank=True, max_length=200, null=True)),
                ('ContactPersonPic', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyName', models.CharField(blank=True, max_length=140, null=True)),
                ('CompanyAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('CompanyDistrictName', models.CharField(blank=True, max_length=140, null=True)),
                ('CompanyStateName', models.CharField(blank=True, max_length=140, null=True)),
                ('CompanyEmailID', models.CharField(blank=True, max_length=140, null=True)),
                ('CompanyWebsiteLink', models.CharField(blank=True, max_length=140, null=True)),
                ('CompanyLoginPhoneNo', models.CharField(blank=True, max_length=140, null=True)),
                ('otp', models.CharField(default='1234', max_length=7)),
                ('CompanyLogo', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('AboutCompany', models.CharField(blank=True, max_length=255, null=True)),
                ('SpecializationOfCompany', models.CharField(blank=True, max_length=255, null=True)),
                ('WhyJoin', models.CharField(blank=True, max_length=240, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('OfficePic1', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('OfficePic2', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('OfficePic3', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('OfficePic4', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('OfficePic5', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('OfficePic6', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('OfficePic7', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('OfficePic8', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('OfficePic9', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('OfficePic10', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('OfficePic11', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('OfficePic12', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyCertificationPic1', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyCertificationPic2', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyCertificationPic3', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyCertificationPic4', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyCertificationPic5', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyCertificationPic6', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyCertificationPic7', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyCertificationPic8', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyCertificationPic9', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyCertificationPic10', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyCertificationPic11', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyCertificationPic12', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyPreviousResultsPic1', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyPreviousResultsPic2', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyPreviousResultsPic3', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyPreviousResultsPic4', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyPreviousResultsPic5', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyPreviousResultsPic6', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyPreviousResultsPic7', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyPreviousResultsPic8', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyPreviousResultsPic9', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyPreviousResultsPic10', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyPreviousResultsPic11', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CompanyPreviousResultsPic12', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CustomerReviewsPic1', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CustomerReviewsPic2', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CustomerReviewsPic3', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CustomerReviewsPic4', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CustomerReviewsPic5', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CustomerReviewsPic6', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CustomerReviewsPic7', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CustomerReviewsPic8', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CustomerReviewsPic9', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CustomerReviewsPic10', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CustomerReviewsPic11', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('CustomerReviewsPic12', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('PORFENSSIONAL_Plan', models.BooleanField(default=False)),
                ('BUSINESS_Plan', models.BooleanField(default=False)),
                ('ULTIMATE_Plan', models.BooleanField(default=False)),
                ('is_payment_done', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SellerSellFranchise',
            fields=[
                ('FranchiseID', models.AutoField(primary_key=True, serialize=False)),
                ('CompanyName', models.CharField(blank=True, max_length=255, null=True)),
                ('CompanyAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('ContactPerson', models.CharField(blank=True, max_length=255, null=True)),
                ('MobileNo', models.CharField(blank=True, max_length=255, null=True)),
                ('ContactPersonDesigation', models.CharField(blank=True, max_length=255, null=True)),
                ('YearOfStabilization', models.CharField(blank=True, max_length=255, null=True)),
                ('TotalNumberOfEmployees', models.CharField(blank=True, max_length=255, null=True)),
                ('DealIn', models.CharField(blank=True, max_length=255, null=True)),
                ('FranchiseOfferFor', models.CharField(blank=True, max_length=255, null=True)),
                ('AreaType', models.CharField(blank=True, max_length=255, null=True)),
                ('TotalAreaRequired', models.CharField(blank=True, max_length=255, null=True)),
                ('TotalInvestmentRequired', models.CharField(blank=True, max_length=255, null=True)),
                ('EstimatedReturnOfInvestment', models.CharField(blank=True, max_length=255, null=True)),
                ('TotalShareOfferOnSells', models.CharField(blank=True, max_length=255, null=True)),
                ('Approved', models.BooleanField(default=False)),
                ('UploadCompanyVisitingCard', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
            ],
        ),
        migrations.CreateModel(
            name='SellerTodaysDeals',
            fields=[
                ('TodaysDealID', models.AutoField(primary_key=True, serialize=False)),
                ('Catagery', models.CharField(blank=True, max_length=230, null=True)),
                ('DealTitle', models.CharField(blank=True, max_length=230, null=True)),
                ('DealPostDateandTime', models.DateTimeField(auto_now_add=True)),
                ('DealAddDiscription', models.TextField(blank=True, max_length=230, null=True)),
                ('Approved', models.BooleanField(default=False)),
                ('Panding', models.BooleanField(default=False)),
                ('UploadAdsPhoto', models.ImageField(blank=True, null=True, upload_to='douryouimages')),
                ('from_compny_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='douryou_seller.sellerprofile')),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-TodaysDealID',),
            },
        ),
    ]
