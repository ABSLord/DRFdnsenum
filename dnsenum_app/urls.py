from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from dnsenum_app.views import TestApi, DNSEnum

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('test/', TestApi.as_view(), name='test'),
    path('dnsenum/', DNSEnum.as_view(), name='dnsenum'),
]
