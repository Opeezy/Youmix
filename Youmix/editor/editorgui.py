import tkinter as tk
import os

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import filedialog as fd
from threading import Thread, currentThread, active_count

class EditWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Editor")
        self.geometry("1200x600")
        self.resizable(False,False)

if __name__ == "__main__":
    app = EditWindow()
    app.mainloop()