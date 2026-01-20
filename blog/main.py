from fastapi import FastAPI
from .import schemas, models
from .database import engine

app = FastAPI()

models.Base.metaData.create_all(engine)

@app.post('/blog')
def create(request:schemas.Blog):
    return request

