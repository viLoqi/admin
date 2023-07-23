import json

with open("./cse_courses.json", "r") as f:
    database = json.load(f)
    resDB = {}

    for k, v in database.items():
        no_space = "".join(k.split())
        resDB[no_space] = v

    with open("./cse_courses.json", "w") as wf:
        wf.write(json.dumps(resDB))