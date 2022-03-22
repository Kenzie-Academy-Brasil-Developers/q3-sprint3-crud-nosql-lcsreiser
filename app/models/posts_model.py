from datetime import datetime
from flask import request
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["kenzie"]


class Post:
    def __init__(self, title, author, tags: list, content):

        self.id = (
            list((db.posts.find().sort("_id", -1).limit(1)))[0]["id"] + 1
            if len(list((db.posts.find()))) > 0
            else 1
        )
        self.post_created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.post_updated = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content

    @staticmethod
    def get_all():
        devs_list = db.posts.find()

        return devs_list

    def create_post(self):

        db.posts.insert_one(self.__dict__)

    @staticmethod
    def delete_post(id):
        deleted_post = db.posts.find_one_and_delete({"id": id})

        return deleted_post

    @staticmethod
    def filter_post(id):
        filtred_post = db.posts.find_one({"id": id})
        return filtred_post

    @staticmethod
    def update_post(id):
        new_post = request.get_json()
        new_post["post_updated"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        return db.posts.find_one_and_update(
            {"id": id}, {"$set": new_post}, return_document=True
        )
