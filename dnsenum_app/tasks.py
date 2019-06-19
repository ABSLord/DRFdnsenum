from DRFTest.celery import app


@app.task
def hello_task():
    # TODO: add task here
    print("hello")
