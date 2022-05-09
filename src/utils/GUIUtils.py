# Importing the tkinter library
import tkinter as tk
from tkinter import Canvas, PhotoImage, ttk
# import image libaries
from PIL import ImageTk, Image
from src.utils.DirUtils import DirUtils
import os


class GUIUtils():

    # the interface should only be initialized in main
    def init_interface(self):
        # set class vars
        GUIUtils.ROOT = tk.Tk()

        GUIUtils.du = DirUtils()
        GUIUtils.mood_path = os.path.join(
            GUIUtils.du.get_mood_dir(), 'mood.png')
        GUIUtils.ROOT.geometry("600x600")
        GUIUtils.ROOT.title("Deamona")
        # self.root.attributes('-alpha', 0)

        img = ImageTk.PhotoImage(Image.open(GUIUtils.mood_path))
        GUIUtils.image_label = tk.Label(GUIUtils.ROOT, image=img)

        # this attribute is garbage collected after __init__ is run, so save it to state
        GUIUtils.image_label.image = img
        GUIUtils.image_label.pack(fill="both", expand="yes")
        GUIUtils.ROOT.bind("<Return>", self.update_mood_img)

    def update_img(self, dir):
        img = ImageTk.PhotoImage(Image.open(dir))
        GUIUtils.image_label.configure(image=img)
        GUIUtils.image_label.image = img

    def test_img(self):
        self.update_img('test.png')

    def update_mood_img(self):
        self.update_img(self.mood_path)
        GUIUtils.ROOT.update_idletasks()

    def main_loop(self):
        return GUIUtils.ROOT.mainloop()
