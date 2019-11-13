import base64
import uuid 
import os

image_dir = os.path.dirname(os.path.abspath(__file__)) + "/tmp/"

def save_base64_image(img_id, base64_str):
  ext = get_base64_img_ext(base64_str)
  src = get_base64_img_src(base64_str)

  # convert img_data string to byte array
  byte_data = str.encode(src)
  
  # generate uuid for file name
  file_id = image_dir + img_id + "." + ext

  with open(file_id, "wb") as fh:
    fh.write(base64.decodebytes(byte_data))
    return file_id

def remove_image(file_id):
  if os.path.exists(file_id):
    os.remove(file_id)

def get_base64_img_ext(base64_str):
  cut_idx = base64_str.index(';charset=utf-8;base64,', 0)
  
  return base64_str[0:cut_idx].replace('data:image/', '', 1)

def get_base64_img_src(base64_str):
  return base64_str.split(";charset=utf-8;base64,", 1)[1]
