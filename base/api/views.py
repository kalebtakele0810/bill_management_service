from rest_framework.decorators import api_view
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import PaymentSerializer, ResponseSerializer
from loguru import logger
from base.models import Payment
from rest_framework import status,serializers
from rest_framework.response import Response

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['username'] = user.username
#         return token
# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
    
@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token',
        '/api/refresh'
    ]
    return Response(routes)

# @permission_classes(IsAuthenticated)
@api_view(['POST'])
def savePayment(request):
    try:
        if request.method == 'POST':
            payment = PaymentSerializer(data=request.data)
            if payment.is_valid():
                payment.save()
                # responseObj = ResponseSerializer(payment)
                return Response(payment.data)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    except Payment.DoesNotExist:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
   