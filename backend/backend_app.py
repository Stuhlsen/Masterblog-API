from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


def get_next_post_id() -> int:
    """Return the next unique post ID."""
    if not POSTS:
        return 1
    return max(post["id"] for post in POSTS) + 1


@app.route("/api/posts", methods=["GET", "POST"])
def posts():
    """List posts (GET) or create a new post (POST)."""
    if request.method == "GET":
        return jsonify(POSTS)

    data = request.get_json(silent=True) or {}

    title = str(data.get("title", "")).strip()
    content = str(data.get("content", "")).strip()

    missing_fields = []
    if not title:
        missing_fields.append("title")
    if not content:
        missing_fields.append("content")

    if missing_fields:
        return jsonify({
            "error": "Missing required fields",
            "missing": missing_fields,
        }), 400

    new_post = {
        "id": get_next_post_id(),
        "title": title,
        "content": content,
    }

    POSTS.append(new_post)
    return jsonify(new_post), 201

@app.route("/api/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id: int):
    """Delete a post by its ID."""
    for index, post in enumerate(POSTS):
        if post["id"] == post_id:
            POSTS.pop(index)
            return jsonify({
                "message": f"Post with id {post_id} has been deleted successfully."
            }), 200

    return jsonify({
        "error": f"Post with id {post_id} not found."
    }), 404


@app.route("/api/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id: int):
    """Update a post by its ID."""
    post = next((p for p in POSTS if p["id"] == post_id), None)
    if post is None:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    data = request.get_json(silent=True) or {}

    if "title" in data:
        title = str(data.get("title", "")).strip()
        if title:
            post["title"] = title

    if "content" in data:
        content = str(data.get("content", "")).strip()
        if content:
            post["content"] = content

    return jsonify(post), 200




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
