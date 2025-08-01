from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'jose',
            'password': '123456',
            'email': 'jose@jose.com',
        },
    )

    # Voltou o status correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic
    assert response.json() == {
        'username': 'jose',
        'email': 'jose@jose.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'jose',
                'email': 'jose@jose.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123456',
            'username': 'testusername2',
            'email': 'testusername@jose.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testusername2',
        'email': 'testusername@jose.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'password': '123456',
            'username': 'testusername2',
            'email': 'testusername@jose.com',
            'id': 1,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user_email(client):
    # Faz um GET para buscar o email do usuário com ID 1

    # Cria o usuario primeiro
    client.post(
        '/users/',
        json={
            'username': 'jose',
            'password': '123456',
            'email': 'jose@jose.com',
        },
    )

    # Acessa o endpoint que contem o usuario
    response = client.get('/users/1')

    # Verifica se a resposta está correta
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'email': 'jose@jose.com'}
