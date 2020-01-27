from flask import Blueprint
from flask_restx import Resource

from app.domains.facade import get_all_tasks, get_task, create_task, update_task, delete_task
from app.schemas.todo_serializers import crete_task, complete_task
from ext.restlib import api

example = Blueprint('api', __name__, url_prefix='/api/1') # This blueprint is not used
ns = api.namespace('example', description='TODO operations')


@ns.route('/<string:todo_id>')
@api.doc(responses={404: 'Todo not found'}, params={'todo_id': 'The Todo ID'})
class Todo(Resource):

    @api.doc(description='todo_id should be a interger number}')
    @api.marshal_with(complete_task)
    def get(self, todo_id):
        """Fetch a given resource"""
        return get_task(todo_id)

    @api.doc(responses={204: 'Todo deleted'})
    def delete(self, todo_id):
        """Delete a given resource"""
        return delete_task(todo_id)

    @api.marshal_with(complete_task)
    @api.expect(crete_task)
    def put(self, todo_id):
        """Update a given resource"""
        api_payload = api.payload
        return update_task(api_payload, todo_id)


@ns.route('/todo')
class TodoList(Resource):
    """Shows a list of all todos, and lets you POST to add new tasks"""

    @api.doc('Get all tasks actives')
    @api.marshal_list_with(complete_task)
    def get(self):
        """List all todos"""
        return get_all_tasks()

    @api.expect(crete_task)
    @api.marshal_with(complete_task, code=201)
    def post(self):
        """Create a todo"""
        api_payload = api.payload
        return create_task(api_payload)
