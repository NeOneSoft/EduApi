# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

"""
Serializers for a Payment Module
"""

from rest_framework import serializers
from payments.models import Payment


# Define Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    protection_eligibility = serializers.CharField(max_length=200)
    address_status = serializers.CharField(max_length=200)
    payer_id = serializers.CharField(max_length=200)
    payment_date = serializers.CharField(max_length=200)
    payment_status = serializers.CharField(max_length=200)
    verify_sign = serializers.CharField(max_length=200)
    receiver_id = serializers.CharField(max_length=200)
    txn_type = serializers.CharField(max_length=200)
    item_name = serializers.CharField(max_length=200)
    mc_currency = serializers.CharField(max_length=200)
    payment_gross = serializers.DecimalField(max_digits=6, decimal_places=2)
    shipping = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Payment
        fields = '__all__'
