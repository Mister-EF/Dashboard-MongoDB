from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client['dashboard_db']
collection = db['content_scaling']

test_data = [
    {"title": "Server Health", "description": "Monitoring CPU and RAM usage across clusters.", "scale_value": 92},
    {"title": "User Traffic", "description": "Tracking active sessions in the South America region.", "scale_value": 45},
    {"title": "Database Latency", "description": "Measuring response time for NoSQL queries.", "scale_value": 12}
]

collection.insert_many(test_data)
print("Data injected successfully! Go refresh your browser.")
