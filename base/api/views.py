from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import PaymentSerializer
from loguru import logger
from rest_framework import status,serializers
from rest_framework.response import Response

from base.api import serializers

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
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
    if request.method == 'POST':
        if request.user.roles.filter(name='Customer').exists():
            payment = PaymentSerializer(data=request.data)
            if payment.is_valid():
                logger.info('Save payment request:'+ str(payment.validated_data.RequestRefID))
                payment.validated_data.payload.save()
                return Response(payment)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)