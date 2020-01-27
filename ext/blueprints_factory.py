def register_blueprints(app):

    # config test app blueprint remove it
    from app.resources.api_v1.endpoints import example
    app.register_blueprint(example, url_prefix="/example")

    return app
