from pydantic import BaseModel


class UserInfo(BaseModel):
    name: str
    surname: str
    age: int
