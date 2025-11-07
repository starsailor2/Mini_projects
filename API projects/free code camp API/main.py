from fastapi import FastAPI  
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

#defining schema using pydantic
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

# this is called a path operation
@app.get("/")
def root(): # the name in the function doesn't matter  
    return {"messege": "Hello world"} # this output will be visible for the user(it will send in JSON format)

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_post(new_post: Post):
    print(new_post.title)
    print(new_post.published)
    return {"data": "new post"}

@app.post("/create")
def create(payload: dict = Body(...)): # extract all the fields from the body and stored inside a python dictionary
    print(payload)
    return {"new_post": f"title {payload['title']} content: {payload['content']}"}

