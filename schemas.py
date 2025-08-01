from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDB(UserSchema):  # herda todas as caracteristicas de UserSchema + id
    id: int


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr

#Schema para retornar somente o email
class UserEmail(BaseModel):
    email: EmailStr


class UserList(BaseModel):
    users: list[UserPublic]
