from django.urls import path
from . import views
urlpatterns = [
    path('admin.html', views.admine ,name ="admine"),
    path('appointment-list.html', views.appointment_list ,name ="appointment_list"),
    path('blank-pagew.html', views.blank_pagew ,name ="blank_pagew"),
    path('componentsw.html', views.componentsw ,name ="componentsw"),
    path('data-tables.html', views.data_tables ,name ="data_tables"),
    path('doctor-list.html', views.doctor_list ,name ="doctor_list"),
    path('error-404.html', views.error_404 ,name ="error_404"),
    path('error-500.html', views.error_500 ,name ="error_500"),
    path('forgot-passwordw.html', views.forgot_passwordw ,name ="forgot_passwordw"),
    path('form-basic-inputs.html', views.form_basic_inputs ,name ="form_basic_inputs"),
    path('form-horizontal.html', views.form_horizontal ,name ="form_horizontal"),
    path('form-input-groups.html', views.form_input_groups ,name ="form_input_groups"),
    path('form-mask.html', views.form_mask ,name ="form_mask"),
    path('form-validation.html', views.form_validation ,name ="form_validation"),
    path('form-vertical.html', views.form_vertical ,name ="form_vertical"),
    path('invoice-report.html', views.invoice_report ,name ="invoice_report"),
    path('invoice.html', views.invoice ,name ="invoice"),
    path('lock-screen.html', views.lock_screen ,name ="lock_screen"),
    path('loginw.html', views.loginw ,name ="loginw"),
    path('patient-list.html', views.patient_list ,name ="patient_list"),
    path('profilew.html', views.profilew ,name ="profilew"),
    path('registerw.html', views.registerw ,name ="registerw"),
    path('reviewsw.html', views.reviewsw ,name ="reviewsw"),
    path('settings.html', views.settings ,name ="settings"),
    path('specialities.html', views.specialities ,name ="specialities"),
    path('table-basic.html', views.table_basic ,name ="table_basic"),
    path('transactions-list.html', views.transactions_list ,name ="transactions_list"),

    # path('logins',views.logins,name="logins"),
    # path('signup',views.signup,name="signup"),
    path('logout',views.logout,name="logout"),
]