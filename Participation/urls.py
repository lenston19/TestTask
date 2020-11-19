from django.conf.urls import url

from . import views

urlpatterns = [
    url('succes', views.succes, name='succes'),
    url('participation', views.participation.as_view(), name='participation'),
    url('lk', views.participationList.as_view(), name='lk'),
]
