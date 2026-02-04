from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
# import uvicorn

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
    # return limit
    return {'data': {'1', '2', '3'}}

class Blog(BaseModel):
    title: str
    body: str
    published : Optional[bool]
    
@app.post('/blog')

def Create_blog(request: Blog):
    # return request
    return {'data': f"blog is created with title {request.title}"}

# for debugging 
# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1", port=9000) 

