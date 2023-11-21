from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import PaymentSerializer



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

@api_view(['POST'])
@permission_classes(IsAuthenticated)
def savePayment(request):
    if request.method == 'POST':
        payment = PaymentSerializer(request.POST)
        if payment.is_valid():
            payment.save()
    return Response(payment)