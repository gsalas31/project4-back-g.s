#status contains all http status
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import RegistrationSerializer, LoginSerializer, UserListSerializer
from .models import User

class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        #by default is an empty object but info will be saved later on
        user = request.data.get('user', {})
        if not user:
            user = {
                'fullname': request.data.get('fullname'),
                'email': request.data.get('email'),
                'password': request.data.get('password')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)