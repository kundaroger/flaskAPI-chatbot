from fastapi import FastAPI


app = FastAPI()


@app.get('/') #this the path/route
def index():
    return "This is the front page"

@app.get('about')
def about():
    return "About Page"

#This is the backend