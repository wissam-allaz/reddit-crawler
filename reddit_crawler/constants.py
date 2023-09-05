import os
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv("REDDIT_USER_NAME")
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
