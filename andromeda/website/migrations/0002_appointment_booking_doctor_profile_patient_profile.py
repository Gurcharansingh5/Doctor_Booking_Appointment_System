# Generated by Django 4.0.4 on 2022-05-17 10:50

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_time', models.TimeField(max_length=20)),
                ('to_time', models.TimeField(max_length=20)),
                ('date', models.DateField(max_length=10)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('Payment_card', models.BooleanField(default=True)),
                ('card_number', models.IntegerField()),
                ('expire_month', models.IntegerField()),
                ('expire_year', models.IntegerField()),
                ('Cvv', models.IntegerField()),
                ('amount_paid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='doctor_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/website/img/doctors/')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('Gender', models.BooleanField(default=True)),
                ('Date_of_Birth', models.DateField(max_length=20)),
                ('Biography', models.CharField(max_length=500)),
                ('clinic_name', models.CharField(max_length=40)),
                ('clinic_address', models.CharField(max_length=100)),
                ('clinic_images', models.ImageField(upload_to='static/website/img/doctors/')),
                ('Address_line1', models.CharField(max_length=200)),
                ('Address_line2', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=30)),
                ('State_Provice', models.CharField(max_length=30)),
                ('Country', models.CharField(max_length=30)),
                ('Postal_code', models.IntegerField()),
                ('Pricing', models.BooleanField(default=True)),
                ('Services', models.CharField(max_length=30)),
                ('Specialiazation', models.CharField(max_length=30)),
                ('Degree', models.CharField(max_length=30)),
                ('College_Institute', models.CharField(max_length=100)),
                ('Year_of_Completion', models.DateField(max_length=20)),
                ('Hospital_Name', models.CharField(max_length=50)),
                ('From', models.DateField(max_length=20)),
                ('To', models.DateField(max_length=20)),
                ('Designation', models.CharField(max_length=50)),
                ('Awards', models.CharField(max_length=30)),
                ('Year', models.DateField(max_length=20)),
                ('Memberships', models.CharField(max_length=50)),
                ('Registrations', models.CharField(max_length=50)),
                ('Year_of_Registeration', models.DateField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='patient_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/website/img/doctors/')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('Date_of_Birth', models.DateField(max_length=20)),
                ('Blood_Group', models.CharField(max_length=5)),
                ('email', models.EmailField(max_length=50)),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('Address', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=30)),
                ('zip_code', models.IntegerField()),
                ('Country', models.CharField(max_length=30)),
            ],
        ),
    ]
