from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import subprocess
import os

from dnsenum_app.utils import *
from dnsenum_app.tasks import hello_task


class TestApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, _request):
        content = {'message': 'Hello, World!'}
        hello_task.delay()
        return Response(content)


class DNSEnum(APIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self, request):
        domain = request.query_params["domain"]
        process = subprocess.Popen(
            [
                "perl",
                os.path.join(os.getcwd(), "dnsenum_app", "dnsenum.pl"),
                domain,
                "--nocolor"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        process.wait()
        result = parse_dnsenum_output(process.communicate()[0].decode('UTF-8'))
        if process.returncode:
            # if exit code is not 0
            return Response({
                'status': 'error',
                'message': result
            }, status=400)
        else:
            return Response({
                'status': 'success',
                'data': result
            })
