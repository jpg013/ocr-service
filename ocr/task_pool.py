import sys
from queue import Queue
from threading import Thread
import uuid

# default exception handler.
def default_handler(name, exception, *args, **kwargs):
  print("%s raised %s with args %s and kwargs %s", name, str(exception), repr(args), repr(kwargs), file=sys.stderr)
  pass

class TaskWorker(Thread):
  """Thread executing tasks from a given tasks queue"""
  def __init__(self, task_queue, result_queue, result_handler, exception_handler):
    Thread.__init__(self)
    self.task_queue = task_queue
    self.result_handler = result_handler
    self.daemon = True
    self.start()

  def run(self):
    while True:
      func, args, kwargs = self.task_queue.get()
      #the function may raise
      try:
        task_result = func(*args, **kwargs)
        self.result_handler(task_result)
      except Exception as e:
        self.exception_handler(self.name, e, args, kwargs)
      finally:
        #task complete no matter what happened
        self.task_queue.task_done()

class TaskPool:
  """Pool of worker threads consuming tasks from a queue"""
  def __init__(self, worker_count, do_task, result_queue=None):
    self.worker_count = worker_count
    self.queue = Queue(self.worker_count)
    self.result_queue = result_queue
    self.workers = []
    self.do_task = do_task

  def is_alive(self):
    """Returns True if any worker threads are currently running"""
    return True in [t.is_alive() for t in self.workers]

  def run(self):
    if self.is_alive():
      return False
    
    for t in range(self.worker_count):
      worker = TaskWorker(
        self.queue, 
        self.result_queue, 
        self.result_handler, 
        default_handler
      )
      self.workers.append(worker)
    
    return True
  
    """Add a task to the queue"""
  def add_task(self, *args, **kargs):
    self.queue.put((self.do_task, args, kargs))

  def result_handler(self, task_result):
    if self.result_queue is None:
      return

    self.result_queue.add_task(task_result)
