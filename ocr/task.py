import uuid
from cache import client

class OCRTask:
  """Task  """
  def __init__(self, base64_str):
    self.task_id = str(uuid.uuid1())
    self.task_data = base64_str
    self.client = client
    self.result = None
    self.exp = 600 # 10 minutes
    
  def get_storage_key(self):
    return "ocr_" + self.task_id

  def store_result(self):
    key = self.get_storage_key()
    self.client.set(key, self.result, ex=self.exp) #lives for 10 minutes