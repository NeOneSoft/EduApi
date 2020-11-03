# Payment's admin module register
from django.contrib import admin
from payments.models import Payment

admin.site.register(Payment)
