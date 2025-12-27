from fastapi import FastAPI


app = FastAPI() # instance 



@app.get('/') # decorater
def index(): # function
    return {'data': {'name': 'tushar'}}



@app.get('/about')
def about():
    return {'data': 'about page'}

