from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from schemas import (
    Message,
    UserDB,
    UserEmail,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


# Criando usuario
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        id=len(database) + 1,
        **user.model_dump(),  # transforma o objeto do userschema em um dict
    )

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    else:
        user_with_id = UserDB(**user.model_dump(), id=user_id)

        database[user_id - 1] = user_with_id

        return user_with_id


@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')
    else:
        del database[user_id - 1]

        return {'message': 'User deleted'}


@app.get('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserEmail)
def get_email_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')
    else:
        user = database[user_id - 1]
        email = user.email
        return {'email': email}
