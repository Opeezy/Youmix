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
        self.edit_streams = streams

        #main window
        self.title("Editor")
        self.geometry("600x300")
        self.resizable(False,False)

        #Control bar
        self.control_frame = Frame(self, height=50, bg="black")

        #Audio list
        self.streams_frame = Frame(self, bg="blue")
        self.edit_list = Listbox(self.streams_frame, selectmode=EXTENDED)
        if streams is None:
            pass
        else:
            for stream in self.edit_streams:
                self.edit_list.insert(END, stream)

        #Packing
        self.control_frame.pack(side=TOP, fill=X)
        self.streams_frame.pack(side=TOP, expand=TRUE, fill=BOTH)
        self.edit_list.pack(side=LEFT, fill=Y)

if __name__ == "__main__":
    _dummy_list = ["dummy_stream" for i in range(10)]
    app = EditWindow(_dummy_list)
    app.mainloop()