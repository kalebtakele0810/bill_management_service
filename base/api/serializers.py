from base.models import Payment

from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['transactionId','bill','paymentChannel']