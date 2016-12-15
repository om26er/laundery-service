from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
)
from rest_framework import permissions

from simple_login.views import (
    ActivationKeyRequestAPIView,
    RetrieveUpdateDestroyProfileAPIView,
    ActivationAPIView,
    LoginAPIView,
    PasswordResetRequestAPIView,
    PasswordChangeAPIView,
    StatusAPIView,
)

from laundery_app.models import User, Address, Category, SubCategory
from laundery_app.serializers import (
    UserSerializer,
    AddressSerializer,
    CategorySerializer,
    SubCategorySerializer,
)


class Register(CreateAPIView):
    serializer_class = UserSerializer


class Activate(ActivationAPIView):
    user_model = User
    serializer_class = UserSerializer


class ActivationKeyRequest(ActivationKeyRequestAPIView):
    user_model = User
    serializer_class = UserSerializer


class Login(LoginAPIView):
    user_model = User
    serializer_class = UserSerializer


class Profile(RetrieveUpdateDestroyProfileAPIView):
    user_model = User
    serializer_class = UserSerializer


class ForgotPassword(PasswordResetRequestAPIView):
    user_model = User
    serializer_class = UserSerializer


class ChangePassword(PasswordChangeAPIView):
    user_model = User
    serializer_class = UserSerializer


class Status(StatusAPIView):
    user_model = User
    serializer_class = UserSerializer


class AddAddressAPIView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SubCategoryAPIView(APIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        return SubCategory.objects.filter(category__id=int(self.kwargs['pk']))

    def get(self, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        for item in serializer.data:
            old_url = item.get('image')
            if old_url:
                item.update(
                    {
                        'image': '{}{}{}'.format(
                            'http://', settings.SERVER_IP, old_url
                        )
                    }
                )
        return Response(serializer.data, status=status.HTTP_200_OK)
