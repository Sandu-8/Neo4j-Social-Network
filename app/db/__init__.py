from neomodel import config
from dotenv import load_dotenv
import os

load_dotenv()
config.DATABASE_URL = f"bolt://{os.getenv('NEO4J_USER')}:{os.getenv('NEO4J_PASSWORD')}@{os.getenv('NEO4J_URI').split('://')[1]}"
