from django.conf.urls import include, url
from django.contrib import admin

from laundery_app import urls as exp_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(exp_urls)),
]
