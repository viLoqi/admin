from fastapi import FastAPI

app = FastAPI()
b_name = "loqi-loqi.appspot.com"


@app.get("/about")
async def read_about():
    return {'message': "Welcome to Loqi's System API"}


@app.get("/")
async def fetch_meta_information():

    return "Successful :D"
