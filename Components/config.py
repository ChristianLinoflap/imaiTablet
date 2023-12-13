from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
db_server_name = os.getenv('DB_SERVER_NAME')
db_name = os.getenv('DB_NAME')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')

user_info = {
    'first_name': None,
    'last_name': None,
}