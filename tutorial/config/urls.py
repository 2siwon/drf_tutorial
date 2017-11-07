
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^snippets/', include('snippets.urls', namespace='snippets')),
    url(r'^admin/', admin.site.urls),
]
