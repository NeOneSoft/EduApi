# -*- coding: utf-8 -*-
"""
Views for customerdataapi.
"""
from __future__ import absolute_import, unicode_literals

from rest_framework import viewsets, permissions, status

from customerdataapi.models import CustomerData
from customerdataapi.serializers import CustomerDataSerializer
from rest_framework.response import Response
import json
import ast


class CustomerDataViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving CustomerData.
    """

    queryset = CustomerData.objects.all()
    serializer_class = CustomerDataSerializer
    permission_classes = (permissions.AllowAny,)

    # Define an update data method to store it in our customer model
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request_to_json = json.dumps(request.data)
        request_to_dict = ast.literal_eval(request_to_json)
        request_to_dict['data'] = ast.literal_eval(request_to_dict['data'])
        instance.data = request_to_dict['data']

        serializer = CustomerDataSerializer(data=request_to_dict)

        # Valid data condition
        if serializer.is_valid():
            instance.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
