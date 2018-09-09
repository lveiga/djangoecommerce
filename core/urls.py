from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contato', views.contact, name='contact'),
    path('produto', views.product, name='product'),
    url(r'^produtos/', include(('catalog.urls', 'catalog'), namespace='catalog')),
]