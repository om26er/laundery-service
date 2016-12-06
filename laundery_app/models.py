from django.db import models

from simple_login.models import BaseUser


class User(BaseUser):
    full_name = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=255, blank=False)
    account_activation_sms_otp = None
    password_reset_sms_otp = None
