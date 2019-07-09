import requests
import pytest
#from flask import Flask
#
#@pytest.fixture
#def bringup_server():
#    app = Flask(__name__)
#    app.run(debug=True)


# this presumes initial state
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


#if __name__ == '__main__':
#    print(test_insert())

