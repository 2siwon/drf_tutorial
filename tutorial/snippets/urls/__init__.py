from django.conf.urls import include, url

from snippets.urls import cbv_mixins
from . import cbv, fbv

urlpatterns = [
    url(r'^fbv/', include(fbv, namespace='fbv')),
    url(r'^cbv/', include(cbv, namespace='cbv')),
    url(r'^cbv-mixins/', include(cbv_mixins, namespace='cbv_mixins'))
]