from base.models import Bill, Payment

from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
    # class Meta:
    #     model = Payment
    #     fields = ['transactionId','bill', 'paymentChannel','remark']   

# class PaymentSerializer(serializers.Serializer):
#     payload = ModelSerializer()
#     RequestRefID = serializers.CharField(max_length=200)    
#     CommandID = serializers.CharField(max_length=200)
#     Remark = serializers.CharField(max_length=200)
#     SourceSystem = serializers.CharField(max_length=200)
#     Version = serializers.CharField(max_length=200)
#     Timestamp = serializers.CharField(max_length=200)
#     def save(self):
#         payload = self.validated_data.pop('payload')
#         print('ID============='+payload['bill'])
#         Payment.objects.create( transactionId=payload['transactionId'],
#                                bill=Bill.objects.get(pk = int(payload['bill'])),
#                                paymentChannel=payload['paymentChannel'],remark=payload['remark'])
#         return payload
    
    