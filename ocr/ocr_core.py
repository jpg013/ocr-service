from .base64_image_helper import save_base64_image, remove_image
try:
  from PIL import Image
except ImportError:
  import Image
import pytesseract

def ocr_core(image):
  """This function will handle the core OCR processing of images."""
  image_object = Image.open(image)
  text = pytesseract.image_to_string(image_object)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
  image_object.close()

  return text

def do_base64_ocr_task(task):
  # Save the image to file
  file_name = save_base64_image(task.task_id, task.task_data)

  # Get text from image
  result = ocr_core(file_name)
  task.result = result
  
  # remove image
  remove_image(file_name)
  return task