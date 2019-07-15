import requests
import pytest

initial_users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

def test_load_users():
    for user in initial_users:
        requests.post(f'http://localhost:5000/user/{user["name"]}', data = user)
    r = requests.get('http://localhost:5000/user')
    assert sorted(user['name'] for user in r.json()) == sorted(user['name'] for user in initial_users)

def test_get():
    r = requests.get('http://localhost:5000/user/Jass')
    assert r.json() == {
        "name": "Jass",
        "age": "22",
        "occupation": "Web Developer"
    }

def test_insert():
    r = requests.post('http://localhost:5000/user/Howard', data = {'age':20, 'occupation':'climber'})
    assert r.json() == {
        "name": "Howard",
        "age": "20",
        "occupation": "climber"
    }

# this will fail because it already exists
def test_insert_duplicate():
    r = requests.post('http://localhost:5000/user/Howard', data = {'age':20, 'occupation':'climber'})
    assert r.status_code == 400

def test_delete():
    r = requests.delete('http://localhost:5000/user/Howard')
    assert r.status_code == 200

