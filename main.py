from src.utils.MoodUtils import MoodUtils
from src.utils.DialougeUtils import DialougeUtils
from src.utils.DirUtils import DirUtils
from src.utils.GUIUtils import GUIUtils
from src.utils.EventUtils import StateMachine
from src.utils.events.Notify import *
from src.utils.events.Draw import *
from src.utils.events.Quiet import *
from src.utils.events.Learn import *
import pyttsx3
import tkinter as tk

def main():
    # spawn window
    gu = GUIUtils()
    gu.init_interface()

    # init d-bus
    notif = notify_init()

    # create the root window here and pass it to all object that need a frontend
    mu = MoodUtils()
    mu.update_mood('neutral')

    sm = StateMachine()

    # init voice engine
    vox_engine = pyttsx3.init()
    vox_engine.setProperty('voice', 'mb-us1')
    vox_engine.setProperty('rate', 150)

    # begin dialouge
    du = DialougeUtils(sm, vox_engine, silent=True)
    # choose a root node in the dialogue network to begin on
    du.init_dialouge()

    gu.main_loop()
    # TODO: Remove this to test code below
    return 1



    # autotime = 0.1
    # while True:
    #     mu.update_mood('focused')
    #     time.sleep(autotime)
    #     mu.update_mood('confused')
    #     time.sleep(autotime)
    #     mu.update_mood('sad')
    #     time.sleep(autotime)
    #     mu.update_mood('surprised')
    #     time.sleep(autotime)
    #     mu.update_mood('smirk')
    #     time.sleep(autotime)
    #     mu.glitch_update_mood('crazy', 3, 10)
    #     time.sleep(autotime)
    #     mu.update_mood('regret')
    #     time.sleep(autotime)


main()
