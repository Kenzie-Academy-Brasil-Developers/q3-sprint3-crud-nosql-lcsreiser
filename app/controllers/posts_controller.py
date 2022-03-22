from flask import jsonify, request
from app.models.posts_model import Post
from http import HTTPStatus


def list_posts():
    list_post = Post.get_all()
    list_post = list(list_post)
    for post in list_post:
        post.update({"_id": str(post["_id"])})
    return jsonify(list_post), HTTPStatus.OK


def created_post():
    current_post = request.get_json()
    try:
        post = Post(**current_post)
        post.create_post()
        post._id = str(post._id)
        return jsonify(post.__dict__), HTTPStatus.CREATED
    except (TypeError, AttributeError):
        return "Ops, check request values", HTTPStatus.BAD_REQUEST


def deleted_post(id):
    try:
        current_del = Post.delete_post(id)
        current_del.update({"_id": str(current_del["_id"])})
        return jsonify(current_del), HTTPStatus.OK
    except (TypeError, AttributeError):
        return "ID Not Found", HTTPStatus.NOT_FOUND


def get_one_post(id):
    try:
        current_one = Post.filter_post(id)
        current_one.update({"_id": str(current_one["_id"])})
        return jsonify(current_one), HTTPStatus.OK
    except (TypeError, AttributeError):
        return "ID Not Found", HTTPStatus.NOT_FOUND


def get_one_post_update(id):
    try:
        current_update = Post.update_post(id)
        current_update.update({"_id": str(current_update["_id"])})
        return jsonify(current_update), HTTPStatus.OK
    except (TypeError, AttributeError):
        return "ID Not Found", HTTPStatus.NOT_FOUND
