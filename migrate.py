import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('credentials.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

with open('cse_courses.json', "r") as f:
    class_offerings = json.loads(f.read())

for cls in class_offerings:
    class_data = class_offerings[cls]
    school_code = "002838"
    for sec in class_data:
        cNumber = class_data[sec]['classNumber']
        uid = int(school_code + cNumber)
        db.document(f'chats/{uid}').set({'class': f"{cls}_{sec}"})
