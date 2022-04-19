import time
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import os


def move_gimbal(event):
    '''
    Get the event data and move the gimbal accordingly
    X -> -1 [Joystick left] to 1 [Joystick right]
    Y -> -1 [Joystick up] to 1 [Joystick down]
    '''
    try:
        x,y = event.data['x'], event.data['y'] if event.data.get('x') and event.data.get('y') else None
        if x and y:
            #TODO: @JASH - Add your code below

            ### I HAVE ADDED SOME HELPER CODE BELOW TO TRANSFORM VALUES OF X AND Y - INCASE YOU NEED THAT :) ###
            # # Convert X & Y from [-1,1] to [0,1]
            # x = (x + 1) / 2
            # y = (y + 1) / 2

            # # Convert X and Y to digital values
            # x = 0 if abs(x) < 0.5 else 1 # If X is less than 0.5, set it to 0 else set it to 1
            # y = 0 if abs(y) < 0.5 else 1 # If Y is less than 0.5, set it to 0 else set it to 1
            print(x,y)
    except KeyError as e:
        print(e)

if __name__ == "__main__":

    cred = credentials.Certificate("keys/touri-65f07-firebase-adminsdk-wuv71-3751c21aa8.json")
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://touri-65f07-default-rtdb.firebaseio.com/'})

    db.reference("gimbal").listen(move_gimbal)


