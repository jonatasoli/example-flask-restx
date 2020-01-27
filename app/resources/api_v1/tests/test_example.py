from app.models.todo import ToDo
from ext.db import db


def test_add_task(db_session):
    task = ToDo(task='one', description='my desc')
    db.session.add(task)
    db.session.commit()
    assert task.id == 1
    assert task.task == 'one'
    assert task.description == 'my desc'
    assert task.activate == True


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_get_all_todo_without_data(client, db_session):
    response = client.get('/example/todo')
    assert response.status_code == 201


def test_create_task(client, db_session):
    response = client.post('/example/todo', json={
        'task': 'Todo 1',
        'description': 'My first task'
    })
    assert response.status_code == 201
    assert response.json == {
        'id': 1,
        'task': 'Todo 1',
        'description': 'My first task',
        'activate': True
    }
