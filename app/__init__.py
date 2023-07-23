from fastapi import FastAPI
import json

#
# DUMMY IMPLEMENTATION FOR TESTING!!!
#
#

app = FastAPI()


@app.get("/about")
async def read_about():
    return {'message': "Welcome to Loqi's System API"}


@app.get("/all")
async def fetch_sections():
    with open("./cse_courses.json", "r") as f:
        return [k for k, v in json.load(f).items()]
    # Returns all the class of the school


@app.get("/sections")
async def fetch_sections(course_name: str):

    if not course_name:
        return []

    with open("./cse_courses.json", "r") as f:
        database = json.load(f)
        return [v for _, v in database[course_name].items()]

    # Returns an object with the sections as keys and their associated information


@app.get("/classChatRoomID")
async def fetch_chatroom_id(course_name: str, section_name: str):

    school_code = "002838"

    with open("./cse_courses.json", "r") as f:
        database = json.load(f)
        res = "".join(
            [school_code, database[course_name][section_name]["classNumber"]])
        return int(res)

    # Returns the school code concatenated with the class number for the chatroomID