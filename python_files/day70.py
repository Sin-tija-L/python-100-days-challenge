import os
from dotenv import load_dotenv

# Load environment variables from the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '../python-dotenv/.env')
load_dotenv(dotenv_path=dotenv_path)

print("🌟Login System🌟")
print()

while True:
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username == os.getenv('adminUsername') and password == os.getenv('adminPassword'):
        print("Welcome Admin")
        break
    elif username == os.getenv('username') and password == os.getenv('password'):
        print("Welcome Normy")
        break
    else:
        print("Try again")
