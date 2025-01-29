import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://messattendance-11fc8-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "RA2211003011231":
        {
            "name": "Reetam Kole",
            "hostel": "Nelson",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "RA2211003011230":
        {
            "name": "Kartik Mittal",
            "hostel": "Kaari",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)