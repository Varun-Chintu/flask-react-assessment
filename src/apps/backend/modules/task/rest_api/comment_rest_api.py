from flask import Blueprint, request, jsonify

# 1️⃣ Create the blueprint first
comment_blueprint = Blueprint("comment_blueprint", __name__)

# 2️⃣ In-memory storage
comments = []

# 3️⃣ Add a new comment
@comment_blueprint.route("/comments", methods=["POST"])
def add_comment():
    data = request.get_json()
    if not data or "task_id" not in data or "text" not in data:
        return jsonify({"error": "task_id and text are required"}), 400

    comment_id = len(comments) + 1
    new_comment = {
        "id": comment_id,
        "task_id": data["task_id"],
        "text": data["text"]
    }
    comments.append(new_comment)
    return jsonify(new_comment), 201

# 4️⃣ Update a comment
@comment_blueprint.route("/comments/<int:comment_id>", methods=["PUT"])
def update_comment(comment_id):
    data = request.get_json()
    for comment in comments:
        if comment["id"] == comment_id:
            comment["text"] = data.get("text", comment["text"])
            return jsonify(comment), 200
    return jsonify({"error": "Comment not found"}), 404

# 5️⃣ Get all comments
@comment_blueprint.route("/comments", methods=["GET"])
def get_comments():
    return jsonify(comments), 200

# 6️⃣ Delete a comment
@comment_blueprint.route("/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    global comments
    comments = [c for c in comments if c["id"] != comment_id]
    return jsonify({"message": "Comment deleted"}), 200
