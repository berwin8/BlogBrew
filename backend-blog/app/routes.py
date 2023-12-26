# backend/app/routes.py

from flask import Blueprint, request, jsonify
from . import db
from .models import Post

main = Blueprint('main', __name__)

@main.route('/posts', methods=['POST'])
def create_post():
    post_data = request.get_json()

    new_post = Post(title=post_data['title'], content=post_data['content'])
    db.session.add(new_post)
    db.session.commit()

    return jsonify(new_post.to_dict()), 201  # 使用 to_dict 方法


@main.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])