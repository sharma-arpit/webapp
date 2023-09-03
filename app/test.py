from redis import Redis
import rq


queue = rq.Queue('tasks', connection=Redis.from_url('redis://'))
job = queue.enqueue('app.tasks.example', 23)
print(job.get_id())
