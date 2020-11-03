# Django
from django.db import models


# Payment Model
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

    def __str__(self):
        return "Payment with id <{}>".format(self.id)
