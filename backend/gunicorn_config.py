import os
from dotenv import load_dotenv
load_dotenv()
workers = 4
bind = os.getenv("BACKEND_ADDRESS")
timeout = 60
loglevel = 'info'
accesslog = './logs/access.log'
errorlog = './logs/error.log'