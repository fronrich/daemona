from src.utils.DirUtils import DirUtils
from src.utils.MoodUtils import MoodUtils
import random

# Dialouge Engine


class DialougeUtils:
    def __init__(self, state_machine, vox_engine):
        dru = DirUtils()
        questions = dru.read_json(dru.get_schema_dir(), 'questions.json')
        responses = dru.read_json(dru.get_schema_dir(), 'responses.json')
        self.database = questions + responses
        DialougeUtils.sm = state_machine
        DialougeUtils.vox = vox_engine
        DialougeUtils.mu = MoodUtils()

    # processes a diagloue node, or the objects within the schema database
    # this process is performed recursivley until exit

    def process_node(self, id, seed=-1):

        # isolate speaker

        # get the target node by ID
        def get_node_by_id(id):
            for node in self.database:
                if node['id'] == id:
                    return node

        CURR_NODE = get_node_by_id(id)

        # Update Mood
        if 'sentiment' in CURR_NODE:
            DialougeUtils.mu.update_mood(CURR_NODE['sentiment'])

        # Display Dialouge
        SPEAKER = 'Daemona' if id.split(':')[0] == 'D' else 'Host'

        # get a random item from a list
        # returns the object and seed of the randomization
        def get_rand(list):
            seed = random.randint(0, len(list) - 1)
            return (list[seed], seed)

        # choose iteration of question
        (QUESTION_ITERATION, seed) = get_rand(
            CURR_NODE['iterations']) if seed == -1 else (CURR_NODE['iterations'][seed], seed)

        print(SPEAKER + ': ' + QUESTION_ITERATION)

        if 'events' in CURR_NODE:
            # Trigger any events which occur within this node
            for event in CURR_NODE['events']:
                DialougeUtils.sm.trigger_event(event)

        PATHS = CURR_NODE['paths']

        # path is determined by AI or Host
        path = ''
        # if host responds, show options by parsing paths and displaying iterations for each
        if SPEAKER == 'Daemona':
            # speak
            # speak question iteration
            DialougeUtils.vox.say(QUESTION_ITERATION)
            DialougeUtils.vox.runAndWait()
            i = 0
            seeds = []
            for x in PATHS:
                RES_NODE = get_node_by_id(x)
                (RES_ITERATION, seed) = get_rand(RES_NODE['iterations'])
                seeds.append(seed)
                print(str(i) + ': ' + RES_ITERATION)
                i += 1

            print()
            choice = int(input('What should I say: '))
            path = PATHS[choice]
            print()

            # trigger event on choice or question asked

            return self.process_node(path, seeds[choice])

        # if daemona responding, use sentiment analysis and speak
        else:

            (path, seed) = get_rand(PATHS)
            RES_NODE = get_node_by_id(path)
            (RES_ITERATION, seed) = get_rand(RES_NODE['iterations'])
            print()
            return self.process_node(path)

        # recurse into dialouge tree

    def init_dialouge(self):
        START_QUESTION = 'D:Q-N-0'
        self.process_node(START_QUESTION)
