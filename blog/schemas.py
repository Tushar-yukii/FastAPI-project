from pydantic import BaseModel, EmailStr, Field

class Blog(BaseModel):
    title: str
    body: str

class ShowBlog(BaseModel):
    title: str
    body: str
    model_config = {
        "from_attributes": True
    }

class User(BaseModel):
    name: str
    email: EmailStr
    password : str
    password: str = Field(min_length=6, max_length=72)
    
class ShowUser(BaseModel):
    name: str
    email : str    
    model_config = {
        "from_attributes": True
    }
    #conifg should be Config Pydantic v1
    # class config():
    #     orm_mode = True
        