import os
from dotenv import load_dotenv
from config import CORES, NUMBER_OF_FILES
load_dotenv()
email = os.environ.get('USER_EMAIL')
pasword = os.environ.get('PASWORD')

if __name__ == "__main__":
    print(f"email: {email}")
    print(f"pasword: {pasword}")
    print(f"number of cores: {CORES}")

    