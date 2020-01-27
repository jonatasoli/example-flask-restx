from flask_restx import fields
from ext.restlib import api


todo = api.model('Todo', {
    'task': fields.String(required=True, description='The task details')
})

listed_todo = api.model('ListedTodo', {
    'id': fields.String(required=True, description='The todo ID'),
    'todo': fields.Nested(todo, description='The Todo')
})

crete_task = api.model('Create', {
    'task': fields.String(required=True, description='ToDo Model task name'),
    'description': fields.String(required=True, description='Todo Task Description')
})

complete_task = api.model('Complete_Task', {
    'id': fields.Integer(required=True, description='Task ID'),
    'task': fields.String(required=True, description='ToDo Model task name'),
    'description': fields.String(required=True, description='Todo Task Description'),
    'activate': fields.Boolean(required=True, description='Task status True = actived False = deleted')
})