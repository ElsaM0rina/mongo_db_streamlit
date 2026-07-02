import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri) #MongoClient("mongodb+srv://3jrmvsjsg777_db_user:t9bTGdgKGpJmpIdP@cluster0.bo1sggf.mongodb.net/?appName=Cluster0")

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


