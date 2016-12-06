from django.contrib import admin
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group

from laundery_app.models import User


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

admin.site.register(User, UserAdmin)
admin.site.unregister(Token)
admin.site.unregister(Group)
