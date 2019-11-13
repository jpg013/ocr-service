import os
from dotenv import load_dotenv

# load env file
load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_DB   = os.getenv("REDIS_DB")