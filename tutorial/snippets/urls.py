from django.conf.urls import url

from snippets import views

urlspatterns = [
    url(r'^snippet_list$', views.snippet_list, name='snippet_list'),

]
