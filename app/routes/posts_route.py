from app.controllers import posts_controller


def posts_route(app):
    @app.get("/posts")
    def read_posts():
        return posts_controller.list_posts()

    @app.get("/posts/<int:id>")
    def read_post_by_id(id):
        return posts_controller.get_one_post(id)

    @app.post("/posts")
    def create_post():
        return posts_controller.created_post()

    @app.patch("/posts/<int:id>")
    def update_post(id):
        return posts_controller.get_one_post_update(id)

    @app.delete("/posts/<int:id>")
    def delete_post(id):
        return posts_controller.deleted_post(id)
