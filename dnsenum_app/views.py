from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import subprocess
import os


def find_index_in_list(lst, pattern):
    indexes = [i for i, s in enumerate(lst) if pattern in s]
    if not indexes:
        return -1
    else:
        return indexes[-1]


def parse_dnsenum_output(output):
    result = dict()
    lst = output.split("\n\n")

    index = find_index_in_list(lst, "Host\'s addresses:")
    result["Host\'s addresses:"] = lst[index + 1].split("\n") if index != -1 else [""]

    index = find_index_in_list(lst, "Name Servers")
    result["Name Servers"] = lst[index + 1].split("\n") if index != -1 else [""]

    index = find_index_in_list(lst, "Mail (MX) Servers")
    result["Mail (MX) Servers"] = lst[index + 1].split("\n") if index != -1 else [""]

    return result


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
