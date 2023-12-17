import os
from dotenv import load_dotenv
from configure import cores, user_name

load_dotenv("sample.env")

PASSWORD = os.getenv("password")
HOST = os.getenv("db_host")

# Use the variables in your application
print(f"Database Host: {HOST}")
print(f"Database User: {user_name}")
print(f"Database Password: {PASSWORD}")
print(f"Cores: {cores}")