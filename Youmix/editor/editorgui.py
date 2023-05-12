import tkinter as tk
import os

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import filedialog as fd
from typing import Optional, List

class EditWindow(tk.Tk):
    def __init__(self, streams: Optional[List[str]] = None) -> None:
        super().__init__()

        #main window
        self.title("Editor")
        self.geometry("600x300")
        self.resizable(False,False)

        #Audio list
        self.edit_streams = streams
        self.edit_list = Listbox(self, selectmode=EXTENDED)
        for stream in self.edit_streams:
            self.edit_list.insert(END, stream)

        #Packing
        self.edit_list.pack(side=LEFT)

if __name__ == "__main__":
    app = EditWindow()
    app.mainloop()