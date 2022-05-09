from src.utils.MoodUtils import MoodUtils
from src.utils.DialougeUtils import DialougeUtils
from src.utils.DirUtils import DirUtils
from src.utils.GUIUtils import GUIUtils
from src.utils.EventUtils import StateMachine
from src.utils.events.Notify import *
from src.utils.events.Draw import *
from src.utils.events.Quiet import *
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
    # voices = vox_engine.getProperty('voices')

    # for voice in voices:
    #     print(voice)

    vox_engine.setProperty('voice', 'mb-us1')
    vox_engine.setProperty('rate', 150)

    # test quiet
    quiet_run('encrypt', ['test.txt'])

    # begin dialouge
    du = DialougeUtils(sm, vox_engine)
    # choose a root node in the dialogue network to begin on
    du.init_dialouge()

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
    gu.main_loop()


main()
