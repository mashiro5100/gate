from celery import Celery
from kombu import Exchange, Queue

app = Celery("demo", broker="amqp://guest:guest@localhost:5672//")


app.conf.task_default_exchange = "gate"
app.conf.task_default_exchange_type = "topic"

app.conf.task_queues = (
    Queue("gate1", routing_key="gate.#"),
    Queue("gate2", routing_key="gate.#"),
)


def route_task(name, args, kwargs, options, task=None, **kw):
    return {
        "queue": "gate1",
        "exchange": "gate",
        "exchange_type": "topic",
        "routing_key": "gate.#",
    }


app.conf.task_routes = (route_task,)

# app.conf.task_routes = {'gate1.add': {'queue': 'gate1'}}


@app.task(name="gate1.add")
def add(x, y):
    print(x + y)
