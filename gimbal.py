import time
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import os


def move_gimbal(event):
    try:
        '''
        x -> -1 to 1
        y -> -1 to 1
        '''
        x,y = event.data['x'], event.data['y']
        print(x,y)
    except KeyError as e:
        print(e)

if __name__ == "__main__":

    cred = credentials.Certificate("keys/touri-65f07-firebase-adminsdk-wuv71-3751c21aa8.json")
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://touri-65f07-default-rtdb.firebaseio.com/'})

    db.reference("gimbal").listen(move_gimbal)


