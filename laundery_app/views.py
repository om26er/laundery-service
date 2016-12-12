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

from laundery_app.models import User, Address, Category
from laundery_app.serializers import (
    UserSerializer,
    AddressSerializer,
    CategorySerializer,
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
