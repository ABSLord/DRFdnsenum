from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import subprocess
import os


class TestApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, _request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class DNSEnum(APIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self, _request):
        result = subprocess.Popen(["perl", "/home/anton/work/DRFTest/dnsenum_app/dnsenum.pl", "google.com"], stdout=subprocess.PIPE).stdout.read()
        content = {'message': result}
        return Response(content)
