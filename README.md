# NoSQL Manager — Content Scaling Dashboard

A comprehensive dashboard built with JavaScript, HTML and CSS for the frontend, and MongoDB and Python in the backend to manage non-relational data. Content is fetched dynamically from a MongoDB collection and rendered as interactive cards in real time — no page reloads required.

---

## How It Works

On page load, the JavaScript frontend fires an async request to the Flask `/api/data` endpoint. Python queries the MongoDB collection, serializes the documents to JSON, and returns them to the browser. The frontend then renders each document as a Bootstrap card in the dashboard grid dynamically.

---

## Built With

| Technology | Role |
|------------|------|
| Python | Backend language and API logic |
| Flask | Web server and REST endpoint |
| MongoDB | Non-relational database for dynamic content |
| PyMongo | MongoDB driver for Python |
| python-dotenv | Secure environment variable management |
| JavaScript | Async data fetching and dynamic card rendering |
| HTML5 | Dashboard layout and navbar structure |
| CSS3 | Card styling, hover transitions, and custom variables |
| Bootstrap 5 | Responsive grid and UI components |

---

## Project Structure

```
/
├── app.py                  # Flask app with / and /api/data routes
├── .env                    # MongoDB connection string (not committed)
├── templates/
│   └── index.html          # Dashboard layout and Bootstrap grid
└── static/
    ├── css/
    │   └── style.css       # Card styles, hover effects, and CSS variables
    └── js/
        └── main.js         # Async fetch, card rendering, and grid population
```

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/your-username/nosql-manager.git
cd nosql-manager
```

**2. Install dependencies**
```bash
pip pip install -r requirements.txt
```

**3. Configure the environment**

Create a `.env` file in the root directory:
```
MONGO_URI=mongodb+srv://your-user:your-password@your-cluster.mongodb.net/
```

**4. Start the server**
```bash
python app.py
```

Navigate to `http://127.0.0.1:5000` in your browser.

---

## API Reference

**`GET /api/data`**

Returns all documents from the `content_scaling` collection in the `dashboard_db` database.

Response:
```json
[
  {
    "_id": "64abc123...",
    "title": "Example Item",
    "description": "A sample description.",
    "scale_value": 3
  }
]
```

---

## Features

- Dynamic card grid rendered entirely from MongoDB documents
- Async JavaScript fetch with error handling via `try/catch`
- MongoDB `_id` serialized to string for safe JSON transport
- Environment variables via `.env` for secure credential management
- Smooth card hover animation with `translateY` and `box-shadow` transition
- Responsive layout with Bootstrap 5's grid system

---

Thank you for your attention!
