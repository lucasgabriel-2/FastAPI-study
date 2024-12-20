from http import HTTPStatus

from fastapi.testclient import TestClient

from exercicio_aula02.app import app


def test_should_return_an_html_with_hello_world():
    client = TestClient(app)

    response = client.get('/HTMLRequest')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text
