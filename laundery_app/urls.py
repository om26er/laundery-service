from django.conf.urls import url

from laundery_app.views import (
    ActivationKeyRequest,
    ForgotPassword,
    ChangePassword,
    Register,
    Login,
    Activate,
    Profile,
    Status,
    ListCreateAddressAPIView,
    CategoryAPIView,
    SubCategoryAPIView,
    ServiceRequestAPIView,
    RetrieveUpdateDestroyAddressAPIView,
)


urlpatterns = [
    url(r'^api/user/register$', Register.as_view()),
    url(r'^api/user/request-activation-key$', ActivationKeyRequest.as_view()),
    url(r'^api/user/activate$', Activate.as_view()),
    url(r'^api/user/login$', Login.as_view()),
    url(r'^api/user/forgot-password$', ForgotPassword.as_view()),
    url(r'^api/user/change-password$', ChangePassword.as_view()),
    url(r'^api/user/status$', Status.as_view()),
    url(r'^api/user/me$', Profile.as_view()),
    url(r'^api/user/addresses$', ListCreateAddressAPIView.as_view()),
    url(r'^api/user/addresses/(?P<pk>[0-9]+)$',
        RetrieveUpdateDestroyAddressAPIView.as_view()),
    url(r'^api/laundry/categories$', CategoryAPIView.as_view()),
    url(r'^api/laundry/categories/(?P<pk>[0-9]+)$',
        SubCategoryAPIView.as_view()),
    url(r'^api/laundry/request$', ServiceRequestAPIView.as_view()),
]
