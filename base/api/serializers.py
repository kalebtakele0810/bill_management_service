from base.models import Payment

from rest_framework import serializers


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['transactionId','bill', 'paymentChannel','remark']   
class PaymentSerializer(serializers.Serializer):
    RequestRefID = serializers.CharField()
    CommandID = serializers.CharField()
    Remark = serializers.CharField()
    SourceSystem = serializers.CharField()
    ResultUrl = serializers.CharField()
    Version = serializers.CharField()
    Timestamp = serializers.CharField()
    payload = ModelSerializer()
    