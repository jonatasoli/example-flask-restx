from ext.db import db


class ToDo(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    task = db.Column(db.String(16), nullable=False, unique=False)
    description = db.Column(db.String(20), nullable=True, unique=False)
    activate = db.Column(db.Boolean, nullable=False, unique=False, default=True, server_default="true")

    def __init__(self, task, description):
        super().__init__()
        self.task = task
        self.description = description
