from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('weather/', include('weather.urls')),
    url('admin/', admin.site.urls),
]