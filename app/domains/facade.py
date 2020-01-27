from app.domains.todo.constants import TaskStatusEnum
from app.models.todo import ToDo as _ToDo
from app.schemas.todo_schema import ToDoSchema
from ext.db import db
from ext.restlib import api

todos_schema = ToDoSchema(many=True)
todo_schema = ToDoSchema()

"""
It's not ideal facade pattern
Facade external examples:
https://github.com/pallets/flask/blob/master/flask/__init__.py
https://github.com/kennethreitz/requests/blob/master/requests/__init__.py

Use this pattern to helpers too!
"""


def get_all_tasks():
    """
    Get all tasks, no params
    :return JSON with all tasks
    :raise empty JSON
    """
    output = {}
    try:
        get_all_tasks = _ToDo.query.filter_by(activate=TaskStatusEnum.ACTIVATED.value).all()
    except Exception as e:
        return api.abort(404, 'Error to database {}'.format(e))
    if get_all_tasks:
        output = todos_schema.dump(get_all_tasks)
    return output, 201


def get_task(todo_id):
    """"
    Get task by ID
    :param todo_id: task id
    :return task's details in JSON
    :raise 404 Message
    """
    todo_task = None
    try:
        todo_task = _ToDo.query.filter_by(id=todo_id).first()
    except Exception as e:
        return api.abort(404, 'Error to database {}'.format(e))
    if not todo_task:
        return api.abort(404, "Todo {} doesn't exist".format(todo_id))
    return todo_schema.dump(todo_task)


def create_task(api_payload):
    """
    Create new tasks
    :param task: Task name
    :param description: Task Details
    :return 201 Success Message
    :raise 404 Error Message
    """
    output = None
    try:
        input_data = todo_schema.load(api_payload)
        db.session.add(input_data)
        db.session.commit()
        output = todo_schema.dump(input_data)
    except Exception as e:
        return api.abort(404, "Task include error {}".format(e))

    return output, 201


def update_task(api_payload, todo_id):
    """
    Update existing task
    :param dict with id, task, description and activate
    :return task JSON updated
    :raise 404 Error Message
    """
    task = None
    output = None
    try:
        task = _ToDo.query.filter_by(id=todo_id).first()
        if api_payload.get('task') is not None and api_payload.get('task') != '':
            task.task = api_payload.get('task')
        if api_payload.get('description') is not None and api_payload.get('description') != '':
            task.description = api_payload.get('description')
        if task:
            db.session.add(task)
            db.session.commit()
        output = todo_schema.dump(task)
    except Exception as e:
        return api.abort(404, "Error to update task {}".format(e))
    return output, 201


def delete_task(todo_id):
    """
    Deactivate task
    :param task id
    :return 201 Success Message
    :raise 404 Error Message
    """
    try:
        delete_todo = _ToDo.query.filter_by(id=todo_id).first()
        delete_todo.activate = TaskStatusEnum.DEACTIVATED.value
        db.session.add(delete_todo)
        db.session.commit()
        if delete_todo:
            return {'message': 'task deleted'}, 201
    except Exception as e:
        return api.abort(404, 'Error to delete task {}'.format(e))
    return api.abort(404, "Todo {} doesn't exist".format(todo_id))
