from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message":"the world is alive!!!!"}

@app.get( "/posts")
def get_posts():
    return {"data": "this is your post"}

@app.post("/createpost")
def create_posts(payload: dict=Body(...)):
    print(payload)
    return {"new_post": f"title {payload['id']} content:{payload['type']}"}