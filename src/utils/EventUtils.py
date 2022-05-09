from multiprocessing import Event
from src.utils.events.Draw import *
from src.utils.events.Notify import *
from src.utils.events.Quote import *
from src.utils.events.Quiet import *
from src.utils.DirUtils import DirUtils
import pprint
from asyncio import run as async_run


class Events:
    def __init__(self):
        self.du = DirUtils()
        Events.props = self.du.read_properties(
            self.du.get_cache_dir(), 'life.properties')
        print(Events.props)

    def print_props(self):
        pprint.pprint(Events.props)

    def draw_picture(self):
        async def draw():
            picture_dir = self.du.get_user_pictures_dir()
            draw_dog(picture_dir, 'mona_doggo')
            notify_file_create('Drawing', picture_dir)
        async_run(draw())
        print('afterdraw')

    def fortune(self):
        quote = get_quote_from_rand_word()
        print_quote(quote)

    def inc_prop(self, prop, inc):
        Events.props[prop] += inc
        self.print_props()
        notify_remember()

# state machine


class StateMachine:
    def __init__(self):
        StateMachine.e = Events()

    # trigger an event based on which event enum was given
    def trigger_event(self, event_enum):
        e = StateMachine.e

        # if statement
        if event_enum == 'DRAW_PICTURE':
            return e.draw_picture()
        elif event_enum == 'FORTUNE':
            return e.fortune()
        elif event_enum == 'INC_SENTIMENT':
            return e.inc_prop('SENTIMENT', 1)
        elif event_enum == 'DEC_SENTIMENT':
            return e.inc_prop('SENTIMENT', -1)
        elif event_enum == 'INC_TEMPERMENT':
            return e.inc_prop('TEMPERMENT', 1)
        elif event_enum == 'DEC_TEMPERMENT':
            return e.inc_prop('TEMPERMENT', -1)
        elif event_enum == 'INC_SANITY':
            return e.inc_prop('SANITY', 1)
        elif event_enum == 'DEC_SANITY':
            return e.inc_prop('SANITY', -1)
        else:
            return
