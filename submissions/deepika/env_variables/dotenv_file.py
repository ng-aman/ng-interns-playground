import os
from dotenv import load_dotenv


from config import CORES, NUMBER_OF_FILES

load_dotenv()
host = os.environ.get("host_name")
email = os.environ.get("user_email")
password = os.environ.get("user_password")


if __name__ == "__main__":
    print(f"host_name:{host}")
    print(f"email:{email}")
    print(f"password{password}")
    print(f"Cores:{CORES}")
    print(f"files:{NUMBER_OF_FILES}")

    