import time
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import os


def run_terminal_cmd(cmd, delay_in_sec=0):
    '''
    cmd -> command to run in a new terminal
    delay_in_sec -> delay in seconds [OPTIONAL] [DEFAULT = 0]
    '''
    time.sleep(delay_in_sec)
    os.system("gnome-terminal -- {}".format(cmd))


def nav_room_listner(event):
    '''
    event.data -> {'nav_room': 'nav_room_name'}
    '''
    room_num = None if event.data == 0 else event.data
    room_to_coords = {
        'room 3108': (0, 0),
        'room 3109': (0, 1),
    }
    if room_num:
        #TODO: @Shruti - Add your ROS terminal commands here
        run_terminal_cmd("YOUR COMMAND GOES HERE", delay_in_sec = 1)


def mani_object_listener(event):
    ''' 
    event.data -> {'mani_object': 'mani_object_name'}
    '''
    selected_obj = None if event.data.upper() == 'NONE' else event.data
    if selected_obj:
    #TODO: @Shivani - Add your ROS terminal commands here
        run_terminal_cmd("YOUR COMMAND GOES HERE", delay_in_sec = 1)


def upload_list_of_objects(list_of_objects):
    '''
    list_of_objects -> list of objects
    '''
    #Upload the list to firebase
    db.reference('objects').child('detected_objs').set(list_of_objects)


if __name__ == "__main__":

    cred = credentials.Certificate("keys/touri-65f07-firebase-adminsdk-wuv71-3751c21aa8.json")
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://touri-65f07-default-rtdb.firebaseio.com/'})

    db.reference("/nav/room_num").listen(nav_room_listner)
    db.reference("/mani/object").listen(mani_object_listener)


