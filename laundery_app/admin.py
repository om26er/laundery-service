from django.contrib import admin
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group

from laundery_app.models import (
    User,
    Category,
    SubCategory,
    Service,
    ServiceRequest,
    ServiceItem,
)


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
        return True


class RequestItemsInline(admin.TabularInline):
    model = ServiceItem
    readonly_fields = ('quantity', 'request', 'item', 'price', )


class ServiceRequestAdmin(admin.ModelAdmin):
    inlines = [RequestItemsInline]
    readonly_fields = ('address', 'laundry_type', 'user', 'drop_time')

    class Meta:
        model = ServiceRequest

    def get_queryset(self, request):
        return ServiceRequest.objects.filter(laundry_type='normal')

    def has_add_permission(self, request):
        return False


class ServiceRequestProxy(ServiceRequest):
    class Meta:
        verbose_name = 'Express Service Request'
        verbose_name_plural = 'Express Service Requests'
        proxy = True


class ExpressServiceRequestAdmin(admin.ModelAdmin):
    inlines = [RequestItemsInline]
    readonly_fields = ('address', 'laundry_type', 'user', 'drop_time')

    class Meta:
        model = ServiceRequestProxy

    def get_queryset(self, request):
        return ServiceRequest.objects.filter(laundry_type='express')

    def has_add_permission(self, request):
        return False


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceRequest, ServiceRequestAdmin)
admin.site.register(ServiceRequestProxy, ExpressServiceRequestAdmin)
admin.site.unregister(Token)
admin.site.unregister(Group)
