from django.conf.urls import url
from appSix import views

app_name = 'appSix'

urlpatterns=[
    url(r'^register/$', views.register, name='register'),
    url(r'^UserLogin/$', views.UserLogin, name='UserLogin')
]
