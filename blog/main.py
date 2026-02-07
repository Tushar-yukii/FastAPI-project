from fastapi import FastAPI
from .import modals
from .database import engine
from .routers import blog, user

app = FastAPI()
            
modals.Base.metadata.create_all(engine)

app.include_router(blog.router) 
app.include_router(user.router) #


     


