from mimetypes import init
from cairosvg import svg2png
from src.utils.DirUtils import DirUtils
from src.utils.GUIUtils import GUIUtils
import glitchart
import shutil
import time
import os


class MoodUtils:

    def __init__(self):
        Dir = DirUtils()
        self.mood_dir = Dir.get_mood_dir()
        self.render_path = os.path.join(self.mood_dir, 'mood.png')
        self.gu = GUIUtils()

    # returns the path to the rendered mood
    def get_mood(self):
        return self.render_path

    # rerender mood
    # return path to mood

    def update_mood(self, mood):
        NAME = 'deamona'
        mood_dir = self.mood_dir

        # updates the path to the svg which displays the mood
        # concat path to mood
        CURR_MOOD = os.path.join(mood_dir, (NAME + '_' + str(mood) + '.svg'))

        # read svg as string
        # open text file in read mode
        svg_file = open(CURR_MOOD, "r")

        # read whole file to a string
        svg_data = svg_file.read()

        # close file
        svg_file.close()

        # create a png from the svg
        # storing faces as svgs saves space
        svg2png(bytestring=svg_data, write_to=self.render_path)

        self.gu.update_mood_img()

        # return current mood path
        return self.render_path

    # create glitch effect on current mood

    def glitch_mood(self, duration=10, intensity=20, repeat=True):
        # save the original png
        temp_mood_render_path = self.render_path + '.old'
        shutil.copyfile(self.render_path, temp_mood_render_path)

        # glitch the current object
        rep = 0
        while rep < duration:
            glitchart.png(self.render_path, max_amount=intensity, inplace=True)
            self.gu.update_mood_img()
            time.sleep(0.1)
            rep += 1
        # reset image after delay

        shutil.copyfile(temp_mood_render_path, self.render_path)
        os.remove(temp_mood_render_path)

    def glitch_update_mood(self, new_mood, duration, intensity):
        self.update_mood(new_mood)
        self.glitch_mood(duration, intensity)
        self.update_mood(new_mood)
