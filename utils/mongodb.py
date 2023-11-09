from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Retrieve the MongoDB URI from an environment variable
uri = os.environ.get("mongo_uri")
print("HERE",uri)
# Define connection options (if needed)
options = {}


# Create a MongoClient instance and establish a connection
clientPromise = MongoClient(uri, **options)
#clientPromise = client.connect()


def mongoclient():
    return clientPromise
