from django.conf.urls import url,include

from views import (
    UserCreateAPIView, UserLoginAPIView
)

urlpatterns = [
    url(r'^$', UserLoginAPIView.as_view(), name='login'),
    url(r'^login', UserLoginAPIView.as_view(), name='login'),
    url(r'^register', UserCreateAPIView.as_view(), name='register'),

]