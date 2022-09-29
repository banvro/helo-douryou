# import email
from django.db import models

# Create your models here.


class your_requirement(models.Model):
    select_catgry = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    quali = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    when_require = models.CharField(max_length=40, null=True, blank=True)
    photo = models.ImageField(upload_to='douryouimages/userimages', null=True, blank=True)

    def _str_(self):
        return self.title

class education_loan(models.Model):
    text = models.CharField(max_length=150, null=True, blank=True)
    fname = models.CharField(max_length=150, null=True, blank=True)
    dob = models.CharField(max_length=100000, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    physical = models.CharField(max_length=255, null=True, blank=True)
    purpose = models.CharField(max_length=120, null=True, blank=True)
    country  = models.CharField(max_length=50, null=True, blank=True)
    dtravel = models.CharField(max_length=120, null=True, blank=True)
    rtravel = models.CharField(max_length=120, null=True, blank=True)
    trip  = models.CharField(max_length=70, null=True, blank=True)
    loantime  = models.CharField(max_length=70, null=True, blank=True)
    bankname = models.CharField(max_length=120, null=True, blank=True)
    loanamount = models.CharField(max_length=120, null=True, blank=True)
    itravlue = models.CharField(max_length=255, null=True, blank=True)
    housetype = models.CharField(max_length=120, null=True, blank=True)
    otherproperty = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='douryouimages/userimages', null=True, blank=True)

    def _str_(self):
        return self.text


class travel_insurance(models.Model):
    text = models.CharField(max_length=150, null=True, blank=True)
    fname = models.CharField(max_length=150, null=True, blank=True)
    dob = models.CharField(max_length=100000, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    physical = models.CharField(max_length=255, null=True, blank=True)
    purpose = models.CharField(max_length=120, null=True, blank=True)
    country  = models.CharField(max_length=50, null=True, blank=True)
    dtravel = models.CharField(max_length=120, null=True, blank=True)
    rtravel = models.CharField(max_length=120, null=True, blank=True)
    trip  = models.CharField(max_length=70, null=True, blank=True)
    policytime  = models.CharField(max_length=70, null=True, blank=True)
    companyname = models.CharField(max_length=120, null=True, blank=True)
    insuranceamount = models.CharField(max_length=120, null=True, blank=True)
    itravlue = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='douryouimages/userimages', null=True, blank=True)

    def _str_(self):
        return self.text

class appy_job_requirement(models.Model):
    email = models.CharField(max_length=20, null=True, blank=True)
    qualification = models.CharField(max_length=150, null=True, blank=True)
    experiance = models.CharField(max_length=20, null=True, blank=True)
    salary_expected = models.CharField(max_length=25, null=True, blank=True)
    intersted_field = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    experiance_field = models.CharField(max_length=120, null=True, blank=True)
    location = models.CharField(max_length=120, null=True, blank=True)
    photo = models.ImageField(upload_to='douryouimages/userimages', null=True, blank=True)

    def _str_(self):
        return self.email

class passport(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    fname = models.CharField(max_length=150, null=True, blank=True)
    dob = models.CharField(max_length=20, null=True, blank=True)
    city_name = models.CharField(max_length=25, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    type_of_passport = models.CharField(max_length=120, null=True, blank=True)
    locatype_of_services = models.CharField(max_length=120, null=True, blank=True)
    photo = models.ImageField(upload_to='douryouimages/userimages', null=True, blank=True)

    def _str_(self):                 
        return self.name

class douryou_login(models.Model): 
    number = models.CharField(max_length=255, null=True, blank=True)
    name= models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    intrestedin = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='douryouimages/userimages', null=True, blank=True)
    whyjoin = models.CharField(max_length=255, null=True, blank=True)

    def _str_(self):
        return self.number


class ApplyLuggageAdliodtmet(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    fname= models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    number = models.CharField(max_length=50, null=True, blank=True)
    alt_number = models.CharField(max_length=50, null=True, blank=True)
    passpost_no = models.CharField(max_length=50, null=True, blank=True)
    adhr_no = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    flight_date = models.CharField(max_length=50, null=True, blank=True)
    flight_name_num = models.CharField(max_length=50, null=True, blank=True)
    desc = models.CharField(max_length=50, null=True, blank=True)
    detail_lug = models.CharField(max_length=50, null=True, blank=True)
    total_wight = models.CharField(max_length=50, null=True, blank=True)
    amount_offer = models.CharField(max_length=50, null=True, blank=True)
    Recv_name = models.CharField(max_length=50, null=True, blank=True)
    Recv_fname = models.CharField(max_length=50, null=True, blank=True)
    Recv_address = models.CharField(max_length=50, null=True, blank=True)
    Recv_mb_num = models.CharField(max_length=50, null=True, blank=True)
    Recv_passpost_num = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='douryouimages/userimages', null=True, blank=True)

    def _str_(self):
        return self.name


class ApplyPurchaseFrancbise(models.Model):
    intrestede_in = models.CharField(max_length=255, null=True, blank=True)
    Area_type= models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=50, null=True, blank=True)
    quli = models.CharField(max_length=50, null=True, blank=True)
    total_o = models.CharField(max_length=50, null=True, blank=True)
    flor_num = models.CharField(max_length=50, null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)
    adhar_num = models.CharField(max_length=50, null=True, blank=True)
    pan_num = models.CharField(max_length=50, null=True, blank=True)
    invest = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='douryouimages/userimages', null=True, blank=True)

    def _str_(self):
        return self.intrestede_in