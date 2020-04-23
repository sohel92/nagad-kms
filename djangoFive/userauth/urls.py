from django.conf.urls import url
from userauth import views
from django.contrib import admin

app_name='userauth'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^register/',views.register,name='register'),
    url(r'^user_login/',views.user_login,name='user_login'),
    url(r'^logout/',views.user_logout,name='logout'),


]
