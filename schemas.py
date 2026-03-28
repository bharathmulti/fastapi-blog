from pydantic import BaseModel, Field
from typing import List

class Blog(BaseModel):
    title: str 
    body: str
    user_id: int

class ShowBlog(Blog):
    model_config = {
        "from_attributes": True
    }

class ShowUser(BaseModel):
    name: str 
    email: str
    blogs: List[ShowBlog] = Field(default_factory =list)
    model_config = {
        "from_attributes": True
    }

class ShowBlogWithUser(ShowBlog):
    creator: ShowUser
    model_config = {
        "from_attributes": True
    }

class User(BaseModel):
    name: str
    email: str
    password: str = Field(min_length=4, max_length=72)

class Login(BaseModel):
    username: str 
    password: str = Field(min_length=4, max_length=72)

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


