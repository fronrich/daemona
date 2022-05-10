# sends a notification

import os
import time
import notify2
from src.utils.DirUtils import DirUtils

# only run in main
# starts d-bus connection


def notify_init():
    # initialise the d-bus connection
    notify2.init("Daemona Deamon")


def notify(title, content, icon, timeout):

    # create Notification object
    n = notify2.Notification(None, icon=icon)

    # set urgency level
    n.set_urgency(notify2.URGENCY_NORMAL)

    # set timeout for a notification
    n.set_timeout(timeout)

    # update notification data for Notification object
    n.update(title, content)

    # show notification on screen
    n.show()

# sends a generic notifcation
# generic becaise icon and timeout are constant


def notify_generic(title, content, timeout=1000):
    du = DirUtils()
    icon = os.path.join(du.get_media_dir(), 'icon.svg')
    notify(title, content, icon, timeout)

# spoof a virus


def notify_spoof(title, content, timeout=1000):
    du = DirUtils()
    icon = os.path.join(du.get_media_dir(), 'icon_spoof.svg')
    notify(title, content, icon, timeout)

# noify that daemona will remember something


def notify_remember():
    notify_generic('Interaction Saved to Hard Drive',
                   'Daemona will remember that.')

# notify that daemona has forgetten an interaction


def notify_forget():
    notify_generic('Interaction Forgotten',
                   'Memory lost.')


# notify that an action has been completed

def notify_file_create(file_type, path):
    notify_generic('File Created', 'The ' + str(file_type) +
                   ' has been saved to ' + str(path))


def notify_file_delete(path):
    file_type = path.split('.')[-1]
    notify_generic('File Deleted', 'The ' + str(file_type) +
                   'file in ' + str(path) + ' has been deleted.')


def notify_file_ransom(path):
    file_type = path.split('.')[-1]
    notify_spoof('File Held For Ransom', 'The ' + str(file_type) +
                 'file in ' + str(path) + ' has been encrypted.')


def notify_file_return(path):
    file_type = path.split('.')[-1]
    notify_spoof('File Recovered', 'The ' + str(file_type) +
                 'file in ' + str(path) + ' has been recovered.')
