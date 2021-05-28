import os
import pytest
from flask import Flask, jsonify

import os


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/hello")
    def hello():
        return "Hi, {}".format(os.environ.get("NAME"))

    return app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_hello(client):
    """Start with a blank database."""
    rv = client.get('/hello')
    print(rv.data)
    assert b'Hi' in rv.data