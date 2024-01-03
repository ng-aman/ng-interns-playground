import os
from dotenv import load_dotenv
from configure import cores, user_name

load_dotenv()

password = os.getenv("PASSWORD")
host = os.getenv("DB_HOST")

# Use the variables in your application
print(f"Database Host: {host}")
print(f"Database User: {user_name}")
print(f"Database Password: {password}")
print(f"Cores: {cores}")