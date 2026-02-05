from typing import List
from pydantic import BaseModel, EmailStr, Field

class BlogBase(BaseModel):
    title: str
    body: str
    
class Blog(BlogBase):    
    model_config = {
        "from_attributes": True
    }    

class User(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)
    
class ShowUser(BaseModel):
    name: str
    email : str    
    blogs : List[Blog]
    model_config = {
        "from_attributes": True
    }
#conifg should be Config Pydantic v1
# class config():
#     orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    model_config = {
        "from_attributes": True
    }
# class config():
#     orm_mode = True
        
        