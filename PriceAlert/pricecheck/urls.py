from django.conf.urls import url, include
from . import views

app_name = 'pricecheck'

urlpatterns = [
    url(r'^$', views.index, name='index'),  
    url(r'^item/$', views.item, name='item'),
    url(r'^item/alert/$', views.setAlert, name='alert' )
]