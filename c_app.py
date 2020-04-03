
from celery import Celery

app = Celery("demo", broker='amqp://guest:guest@localhost:5672//')

@app.task
def add(x, y):
    print(x + y)


app.worker_main()
