from ocr import task_queue, OCRTask
from flask import Flask, Blueprint, request, Response
import time
import json

app = Flask(__name__)

# health
@app.route('/health', methods=['GET'])
def health_handler():
  response = app.response_class(
    response=json.dumps({"status": "OK"}),
    status=200,
    mimetype='application/json'
  )
  return response

# base64_image_ocr
@app.route('/base64_image_ocr', methods=['POST'])
def base64_image_ocr_handler():
  try:
    req_data = request.get_json()
    base64_string = req_data['base64_string']
    # create a new ocr task
    task = OCRTask(base64_string)
    # add task to queue for processing
    task_queue.add_task(task)

    return app.response_class(
        response=json.dumps({"task_key": task.get_storage_key()}),
        status=200,
        mimetype='application/json'
      )
  except Exception as e:
    return app.response_class(
      response=json.dumps({"message": str(e)}),
      status=400,
      mimetype='application/json'
    )

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)