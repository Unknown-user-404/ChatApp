from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
import os
from user import User
load_dotenv()
mongo_password = os.getenv('mongo_password')

client = MongoClient(f'mongodb+srv://admin:{mongo_password}@cluster0.y8pvuwe.mongodb.net/?retryWrites=true&w=majority')
chat_db = client.get_database("ChatDB")
users_collection = chat_db.get_collection('users')

def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    users_collection.insert_one({'_id': username, 'email': email, 'password': password_hash})

def get_user(username):
    user_data = users_collection.find_one({'_id': username})
    return User(user_data['_id'], user_data['email'], user_data['password']) if user_data else None