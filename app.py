from flask import Flask, render_template, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI"))
db = client['dashboard_db']
collection = db['content_scaling']

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/api/data')
def get_data():
    data = []
    for doc in collection.find():
        doc['_id'] = str(doc['_id']) 
        data.append(doc)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)