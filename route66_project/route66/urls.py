from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gogetthegood', views.goods, name='thegoods'),
    path('happyhappyjoyjoy', views.joy, name='emotions'),
    path('hey', views.response, name='callback'),
]