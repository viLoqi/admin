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
    arr = []

    cls_no_space = "".join(cls.split())

    for sec in class_data:
        section_data = class_data[sec]
        
        # Additional Fields
        section_data['_created'] = firestore.SERVER_TIMESTAMP
        section_data['_lastWiped'] = firestore.SERVER_TIMESTAMP



        # Document with info about section and the instructor
        arr.append({"sec_id": sec, "sec_ins": section_data["instructor"]})


        db.collection(f'chats/{cls_no_space}/{sec}').document('meta').set(section_data)

        # members and messages will be found in the following paths
        #db.collection(f'chats/{cls}/{sec}/meta/members')
        #db.collection(f'chats/{cls}/{sec}/meta/messages')

    db.document(f'chats/{cls_no_space}').set({'sections': arr})
