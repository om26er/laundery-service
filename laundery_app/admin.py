from django.contrib import admin
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group

from laundery_app.models import User, Category, SubCategory, Service


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


class SubCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = SubCategory


class ServiceAdmin(admin.ModelAdmin):
    class Meta:
        model = Service

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.unregister(Token)
admin.site.unregister(Group)
