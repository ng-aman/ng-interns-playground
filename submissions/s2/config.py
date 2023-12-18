import os 
from dotenv import load_dotenv

load_dotenv()
email = os.getenv("EMAIL")
key = os.getenv("MY_SECRET_KEY")
host = os.getenv("HOST")

print(email)
print(key)
print(host)
