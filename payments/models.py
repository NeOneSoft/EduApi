# Django
from django.db import models


# Define Model Payment
class Payment(models.Model):
    protection_eligibility = models.CharField(max_length=200)
    address_status = models.CharField(max_length=200)
    payer_id = models.CharField(max_length=200)
    payment_date = models.CharField(max_length=200)
    payment_status = models.CharField(max_length=200)
    verify_sign = models.CharField(max_length=200)
    receiver_id = models.CharField(max_length=200)
    txn_type = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)
    mc_currency = models.CharField(max_length=200)
    payment_gross = models.DecimalField(max_digits=6, decimal_places=2)
    shipping = models.DecimalField(max_digits=6, decimal_places=2)

    # Setting display to show in the Django admin site
    def __str__(self):
        return "Payment id <{}>".format(self.id)
