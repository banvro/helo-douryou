# Generated by Django 4.0.5 on 2022-09-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyLuggageAdliodtmet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('fname', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('number', models.CharField(blank=True, max_length=50, null=True)),
                ('alt_number', models.CharField(blank=True, max_length=50, null=True)),
                ('passpost_no', models.CharField(blank=True, max_length=50, null=True)),
                ('adhr_no', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('flight_date', models.CharField(blank=True, max_length=50, null=True)),
                ('flight_name_num', models.CharField(blank=True, max_length=50, null=True)),
                ('desc', models.CharField(blank=True, max_length=50, null=True)),
                ('detail_lug', models.CharField(blank=True, max_length=50, null=True)),
                ('total_wight', models.CharField(blank=True, max_length=50, null=True)),
                ('amount_offer', models.CharField(blank=True, max_length=50, null=True)),
                ('Recv_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Recv_fname', models.CharField(blank=True, max_length=50, null=True)),
                ('Recv_address', models.CharField(blank=True, max_length=50, null=True)),
                ('Recv_mb_num', models.CharField(blank=True, max_length=50, null=True)),
                ('Recv_passpost_num', models.CharField(blank=True, max_length=50, null=True)),
                ('photo', models.CharField(blank=True, max_length=100000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplyPurchaseFrancbise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intrestede_in', models.CharField(blank=True, max_length=255, null=True)),
                ('Area_type', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.CharField(blank=True, max_length=50, null=True)),
                ('quli', models.CharField(blank=True, max_length=50, null=True)),
                ('total_o', models.CharField(blank=True, max_length=50, null=True)),
                ('flor_num', models.CharField(blank=True, max_length=50, null=True)),
                ('area', models.CharField(blank=True, max_length=50, null=True)),
                ('adhar_num', models.CharField(blank=True, max_length=50, null=True)),
                ('pan_num', models.CharField(blank=True, max_length=50, null=True)),
                ('invest', models.CharField(blank=True, max_length=50, null=True)),
                ('photo', models.CharField(blank=True, max_length=100000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='appy_job_requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('qualification', models.CharField(blank=True, max_length=150, null=True)),
                ('experiance', models.CharField(blank=True, max_length=20, null=True)),
                ('salary_expected', models.CharField(blank=True, max_length=25, null=True)),
                ('intersted_field', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('experiance_field', models.CharField(blank=True, max_length=120, null=True)),
                ('location', models.CharField(blank=True, max_length=120, null=True)),
                ('photo', models.CharField(blank=True, max_length=100000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='douryou_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('intrestedin', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.CharField(blank=True, max_length=100000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='education_loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=150, null=True)),
                ('fname', models.CharField(blank=True, max_length=150, null=True)),
                ('dob', models.CharField(blank=True, max_length=100000, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('physical', models.CharField(blank=True, max_length=255, null=True)),
                ('purpose', models.CharField(blank=True, max_length=120, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('dtravel', models.CharField(blank=True, max_length=120, null=True)),
                ('rtravel', models.CharField(blank=True, max_length=120, null=True)),
                ('trip', models.CharField(blank=True, max_length=70, null=True)),
                ('loantime', models.CharField(blank=True, max_length=70, null=True)),
                ('bankname', models.CharField(blank=True, max_length=120, null=True)),
                ('loanamount', models.CharField(blank=True, max_length=120, null=True)),
                ('itravlue', models.CharField(blank=True, max_length=255, null=True)),
                ('housetype', models.CharField(blank=True, max_length=120, null=True)),
                ('otherproperty', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.CharField(blank=True, max_length=100000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('fname', models.CharField(blank=True, max_length=150, null=True)),
                ('dob', models.CharField(blank=True, max_length=20, null=True)),
                ('city_name', models.CharField(blank=True, max_length=25, null=True)),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('type_of_passport', models.CharField(blank=True, max_length=120, null=True)),
                ('locatype_of_services', models.CharField(blank=True, max_length=120, null=True)),
                ('photo', models.CharField(blank=True, max_length=100000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='travel_insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=150, null=True)),
                ('fname', models.CharField(blank=True, max_length=150, null=True)),
                ('dob', models.CharField(blank=True, max_length=100000, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('physical', models.CharField(blank=True, max_length=255, null=True)),
                ('purpose', models.CharField(blank=True, max_length=120, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('dtravel', models.CharField(blank=True, max_length=120, null=True)),
                ('rtravel', models.CharField(blank=True, max_length=120, null=True)),
                ('trip', models.CharField(blank=True, max_length=70, null=True)),
                ('policytime', models.CharField(blank=True, max_length=70, null=True)),
                ('companyname', models.CharField(blank=True, max_length=120, null=True)),
                ('insuranceamount', models.CharField(blank=True, max_length=120, null=True)),
                ('itravlue', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.CharField(blank=True, max_length=100000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='your_requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_catgry', models.CharField(blank=True, max_length=20, null=True)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('quali', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('when_require', models.CharField(blank=True, max_length=40, null=True)),
                ('photo', models.CharField(blank=True, max_length=100000, null=True)),
            ],
        ),
    ]
