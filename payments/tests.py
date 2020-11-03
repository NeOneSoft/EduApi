# Django
from django.test import TestCase

HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded',
}


class TestViews(TestCase):
    def test_payment_status(self):
        data = {
            'protection_eligibility': 'Eligible',
            'address_status': 'confirmed',
            'payer_id': '903d7ebd-68f0-4574-ac31-4e5f80a41a98',
            'payment_date': '20:12:59 Jan 13, 2009 PST',
            'payment_status': 'Failed',
            'notify_version': '2.6',
            'verify_sign': 'AtkOfCXbDm2hu0ZELryHFjY-Vb7PAUvS6nMXgysbElEn9v-1XcmSoGtf',
            'receiver_id': 'S8XGHLYDW9T3S',
            'txn_type': 'express_checkout',
            'item_name': 'basic',
            'mc_currency': 'USD',
            'payment_gross': '19.90',
            'shipping': '0.0'
        }
        response = self.client.post('http://localhost:8000/payments/paypal/', headers=HEADERS, data=data)
        self.assertEquals(response.status_code, 202)

    def test_premium_plan(self):
        data = {
            'protection_eligibility': 'Eligible',
            'address_status': 'confirmed',
            'payer_id': '5b5eb8cd-9a4b-41f8-ad62-e7937c1789b3',
            'payment_date': '20:12:59 Jan 13, 2009 PST',
            'payment_status': 'Completed',
            'notify_version': '2.6',
            'verify_sign': 'AtkOfCXbDm2hu0ZELryHFjY-Vb7PAUvS6nMXgysbElEn9v-1XcmSoGtf',
            'receiver_id': 'S8XGHLYDW9T3S',
            'txn_type': 'express_checkout',
            'item_name': 'premium',
            'mc_currency': 'USD',
            'payment_gross': '17.00',
            'shipping': '5.80'
        }
        response = self.client.post('http://localhost:8000/payments/paypal/', headers=HEADERS, data=data)
        self.assertEquals(response.status_code, 202)

    def test_last_payment(self):
        data = {
            'protection_eligibility': 'Eligible',
            'address_status': 'confirmed',
            'payer_id': '5b5eb8cd-9a4b-41f8-ad62-e7937c1789b3',
            'payment_date': '20:12:59 Jan 13, 2009 PST',
            'payment_status': 'Completed',
            'notify_version': '2.6',
            'verify_sign': 'AtkOfCXbDm2hu0ZELryHFjY-Vb7PAUvS6nMXgysbElEn9v-1XcmSoGtf',
            'receiver_id': 'S8XGHLYDW9T3S',
            'txn_type': 'express_checkout',
            'item_name': 'premium',
            'mc_currency': 'USD',
            'payment_gross': '17.00',
            'shipping': '5.80'
        }
        response = self.client.post('http://localhost:8000/payments/paypal/', headers=HEADERS, data=data)
        self.assertEquals(response.status_code, 202)

    def test_bad_request(self):
        data = {
            'protection_eligibility': 'Eligible',
            'address_status': 'confirmed',
            'payer_id': 'a237ed14-88fb-45f3-b9b1-471877dbdc60',
            'payment_date': '20:12:59 Jan 13, 2009 PST',
            'payment_status': 'Completed',
            'notify_version': '2.6',
            'verify_sign': 'AtkOfCXbDm2hu0ZELryHFjY-Vb7PAUvS6nMXgysbElEn9v-1XcmSoGtf',
            'receiver_id': 'S8XGHLYDW9T3S',
            'txn_type': 'express_checkout',
            'item_name': 'basic',
            'mc_currency': 'USD',
            'payment_gross': '9.56',
        }
        response = self.client.post('http://localhost:8000/payments/paypal/', headers=HEADERS, data=data)
        self.assertEquals(response.status_code, 400)

    def test_basic_plan(self):
        data = {
            'protection_eligibility': 'Eligible',
            'address_status': 'confirmed',
            'payer_id': 'b18143b8-cc15-4e56-93cc-4b7008f5bf13',
            'payment_date': '20:12:59 Jan 13, 2009 PST',
            'payment_status': 'Completed',
            'notify_version': '2.6',
            'verify_sign': 'AtkOfCXbDm2hu0ZELryHFjY-Vb7PAUvS6nMXgysbElEn9v-1XcmSoGtf',
            'receiver_id': 'S8XGHLYDW9T3S',
            'txn_type': 'express_checkout',
            'item_name': 'basic',
            'mc_currency': 'USD',
            'payment_gross': '8.70',
            'shipping': '3.15'
        }
        response = self.client.post('http://localhost:8000/payments/paypal/', headers=HEADERS, data=data)
        self.assertEquals(response.status_code, 202)
