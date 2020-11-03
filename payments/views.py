# Serializers
from payments.serializers import PaymentSerializer

# Djangorestframework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

# Date and requests
from datetime import datetime
import requests


URL_API_CUSTOMER_DATA = "http://127.0.0.1:8000/api/v1/customerdata/"


class PaymentView(APIView):
    # Modify customer's data
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        ipn_data = dict(request.data.lists())
        # Modify current customer data
        if serializer.is_valid():
            customer = URL_API_CUSTOMER_DATA + ipn_data.get('payer_id')[0] + '/'
            instance = requests.get(customer)
            instance_json = instance.json()
            # Completed payment status condition
            if ipn_data.get('payment_status')[0] == "Completed":
                plan = ipn_data.get('item_name')[0]
            else:
                plan = "free"
            plan_update(instance_json['data'], instance_json['data']['SUBSCRIPTION'], plan)
            string_data = str(instance_json['data'])
            dict_json = {'id': instance_json['id'], 'data': string_data}
            requests.put(customer, dict_json)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define plan update method
def plan_update(customer, current_plan, new_plan):
    now = datetime.now()
    customer['LAST_PAYMENT_DATE'] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    # Define setting's plan condition
    if current_plan == new_plan:
        pass
    else:
        # Define settings for free plan
        if new_plan == "free":
            customer['SUBSCRIPTION'] = new_plan
            customer['ENABLED_FEATURES']['CERTIFICATES_INSTRUCTOR_GENERATION'] = False
            customer['ENABLED_FEATURES']['ENABLE_COURSEWARE_SEARCH'] = False
            customer['ENABLED_FEATURES']['ENABLE_EDXNOTES'] = False
            customer['ENABLED_FEATURES']['ENABLE_DASHBOARD_SEARCH'] = False
            customer['ENABLED_FEATURES']['INSTRUCTOR_BACKGROUND_TASKS'] = False
            customer['ENABLED_FEATURES']['ENABLE_COURSE_DISCOVERY'] = False
            if 'UPGRADE_DATE' in customer:
                del customer['UPGRADE_DATE']
            customer['DOWNGRADE_DATE'] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        # Define settings for basic plan
        elif new_plan == "basic":
            if current_plan == "premium":
                customer['SUBSCRIPTION'] = new_plan
                if 'UPGRADE_DATE' in customer:
                    del customer['UPGRADE_DATE']
                customer['DOWNGRADE_DATE'] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
            else:
                customer['SUBSCRIPTION'] = new_plan
                if 'DOWNGRADE_DATE' in customer:
                    del customer['DOWNGRADE_DATE']
                customer['UPGRADE_DATE'] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        # Define settings for premium plan
        elif new_plan == "premium":
            customer['SUBSCRIPTION'] = new_plan
            if 'DOWNGRADE_DATE' in customer:
                del customer['DOWNGRADE_DATE']
            customer['UPGRADE_DATE'] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
