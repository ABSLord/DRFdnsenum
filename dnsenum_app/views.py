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

    def get(self, request):
        domain = request.query_params["domain"]
        result = subprocess.Popen(
            ["perl", os.path.join(os.getcwd(), "dnsenum_app", "dnsenum.pl"),
             domain], stdout=subprocess.PIPE).stdout.read()
        content = {'message': result}
        return Response(content)
