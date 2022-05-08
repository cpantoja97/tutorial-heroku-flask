import celery
import os
import ffmpeg


app = celery.Celery('example')

app.conf.update(broker_url=os.environ['CLOUDAMQP_URL'])


@app.task
def add(x, y):
    return x + y