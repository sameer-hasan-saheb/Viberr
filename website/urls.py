from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', RedirectView.as_view(url='accounts/login')),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
