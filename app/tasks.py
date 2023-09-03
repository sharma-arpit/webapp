import time
from redis import Redis
import rq


def example(seconds):
    print('Starting task')
    for i in range(seconds):
        print(i)
        time.sleep(1)
    print('Task completed')


queue = rq.Queue('tasks', connection=Redis.from_url('redis://'))
job = queue.enqueue('app.tasks.example', 23)
print(job.get_id())
