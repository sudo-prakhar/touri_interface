from importlib.resources import path
import time
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import os

cred = credentials.Certificate("keys/touri-65f07-firebase-adminsdk-wuv71-3751c21aa8.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://touri-65f07-default-rtdb.firebaseio.com/'})

def save_lift(lift):
    assert lift <= 1.5, "Lift is too high"
    path = "temp/lift"
    db.reference(path).set(lift)

def get_lift():
    try:
        return db.reference("temp/lift").get()
    except Exception as e:
        print("Firebase error: ", e)


