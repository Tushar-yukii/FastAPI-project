from fastapi import FastAPI
from typing import Optional
app = FastAPI() # instance 


@app.get('/blog') # decorater
# default value of limit of 10
def index(limit=10, published: bool= True, sort: Optional[str] = None): # function

    if published:
        return {'data': f'{limit} published blog from the db'}
    else:
        return {'data': f'{limit} blog from the db'}
        

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blog'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
# comments 
def comments(id, limit=10):
    return {'data': {'1', '2', '3'}}



