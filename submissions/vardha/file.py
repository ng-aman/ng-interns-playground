import os
from dotenv import load_dotenv
from config import CORES, NUMBER_OF_FILES

load_dotenv()
email = os.environ.get("USER_EMAIL_ID")
password = os.environ.get("USER_PASSWORD")


if __name__ == "__main__":
    print(f"email: {email}")
    print(f"password: {password}")
    print(f"Cores: {CORES}")
    print(f"files: {NUMBER_OF_FILES}")