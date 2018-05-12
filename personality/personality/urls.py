from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^about/$',include('about.urls')),
    url(r'^home/$',include('home.urls')),
    url(r'^services/$',include('services.urls')),
    url(r'^contact/$',include('contact.urls')),
    url(r'^damodar/data/$',include('data.urls')),


]