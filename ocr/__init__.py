from ocr.task_pool import TaskPool
from ocr.ocr_core import do_base64_ocr_task
from ocr.task import OCRTask

worker_count=1

def store_task_result(task):
  task.store_result()

result_queue = TaskPool(
  worker_count=worker_count, 
  do_task=store_task_result
)

task_queue = TaskPool(
  worker_count=worker_count, 
  do_task=do_base64_ocr_task, 
  result_queue=result_queue
)

# Start the result queue and task queue
result_queue.run()
task_queue.run()