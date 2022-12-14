# Generated by Django 4.0.5 on 2022-09-26 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('douryou', '0002_alter_user_whyjoin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='IELTS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='Passport',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='accomodation_at_abroad',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='air_ticket',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='education_loan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='international_couruer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='international_matamorial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='jobs_at_abroad',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='legal_advisor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='luaggage_adjustment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='money_exchange',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='online_ielts_classes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='pr',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='study_visa',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='tour_travel_package',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='tourist_business_visa',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='transport_for_airport',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='travel_insurence',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='work_permit',
            field=models.BooleanField(default=False),
        ),
    ]
