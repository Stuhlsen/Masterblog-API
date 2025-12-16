# Posts API (Flask)

A lightweight RESTful API for managing blog posts.  
Built for learning CRUD + search + sorting using an in-memory data store (a Python list).

## Features

- **List posts**: `GET /api/posts`
- **Create posts**: `POST /api/posts` (auto-generates integer IDs)
- **Update posts**: `PUT /api/posts/<id>` (partial update: title/content optional)
- **Delete posts**: `DELETE /api/posts/<id>`
- **Search**: `GET /api/posts/search?title=...&content=...`
- **Optional sorting** on list endpoint: `GET /api/posts?sort=title|content&direction=asc|desc`
- **CORS enabled** (works with a separate frontend)

---

## Tech Stack

- Python 3
- Flask
- flask-cors

---

## Project Structure

```text
backend/
  backend_app.py
frontend/
  index.html
  static/
    main.js
    styles.css
  frontend_app.py
