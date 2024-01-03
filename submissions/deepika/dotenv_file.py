import os
from dotenv import load_dotenv
from configure import CORES, NUMBER_OF_FILES

load_dotenv()
host = os.environ.get("HOST_NAME")
email = os.environ.get("USER_EMAIL_ID")
password = os.environ.get("USER_PASSWORD")


if __name__ == "__main__":
    print(f"host_name: {host}")
    print(f"email: {email}")
    print(f"password: {password}")
    print(f"Cores: {CORES}")
    print(f"files: {NUMBER_OF_FILES}")

    