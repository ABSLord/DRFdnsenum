from DRFTest.celery import app
import os
import subprocess

from dnsenum_app.utils import *


@app.task
def hello_task():
    print("hello")


@app.task
def call_dns_enum(domain):
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
        return {
            'status': 'error',
            'message': result
        }
    else:
        return {
            'status': 'success',
            'data': result
        }
