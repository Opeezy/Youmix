import tkinter as tk
import os
import traceback
import math

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import filedialog as fd 
from threading import Thread, currentThread, active_count
from uuid import uuid4
from time import time

SRC_DIR = os.getcwd()
PROJECT_DIR = os.path.dirname(SRC_DIR)

class MainWindow(tk.Tk):
	def __init__(self, version, title):
		super().__init__()

		t = currentThread()
		print(f"Initializing thread {t} for MainWindow()")	

		#main window
		self.title(title)
		self.geometry("800x400+560+340")
		self.resizable(False,False)
		self.iconbitmap(f"{PROJECT_DIR}\\img\\icon.ico")
	
		#menubar
		self.menubar = Menu(self)
		self.config(menu=self.menubar)

		#file menu and cascades
		self.file_menu = Menu(self, tearoff=False)
		self.menubar.add_cascade(label="File", menu=self.file_menu, underline=0)

		#menu commands
		self.file_menu.add_command(label='Save Selected', command=lambda: self.execute_thread(self.save_selected, "save_selected()"))
		self.file_menu.add_command(label='Save All', command=lambda: self.execute_thread(self.save_all, "save_all()"))

		#converter field
		self.convert_frame = Frame(self, bg="#cccccc", relief=RIDGE, bd=2)
		self.url_text = Entry(self.convert_frame, relief=SUNKEN)
		self.convert_button = Button(self.convert_frame, text="Convert", width=15, relief=RAISED, command=lambda: self.execute_thread(self.load_video, "load_video()"))

		#video info and streams
		self.vid_frame = Frame(self)
		self.video_info_frame = Frame(self.vid_frame, bg="black")
		self.video_title = Label(self.video_info_frame, height=2)
		self.video_author = Label(self.video_info_frame, height=2)
		self.video_duration = Label(self.video_info_frame, height=2)
		self.video_streams = Listbox(self.vid_frame, selectmode=EXTENDED)

		#bottom frame
		self.sort_options = ['Descending Quality', 'Ascending Quality']
		self.sort_var = StringVar(self)
		self.sort_var.set(self.sort_options[0])
		self.bottom_frame = Frame(self, bg="#cccccc")
		self.sort_options_menu = OptionMenu(self.bottom_frame, self.sort_var, *self.sort_options, command=self.sort_streams)
		self.progress_indeterminate = Progressbar(self.bottom_frame, orient=HORIZONTAL, length=200, mode='indeterminate')
		self.progress_determinate_frame = Frame(self.bottom_frame, bg="#cccccc")
		self.progress_title = Label(self.progress_determinate_frame, text="Placeholder", bg="#cccccc")
		self.progress_determinate = Progressbar(self.progress_determinate_frame, orient=HORIZONTAL, length=300, mode='determinate')

		'''//PACKING-GRIDDING//'''

		#converter
		self.convert_frame.pack(side=TOP, fill=X)
		self.url_text.pack(side=LEFT, expand=TRUE, fill=X, padx=2, pady=2)
		self.convert_button.pack(side=LEFT, padx=2, pady=5)

		#video info and streams
		self.vid_frame.pack(side=TOP, expand=TRUE, fill=BOTH)
		self.video_info_frame.pack(side=TOP, fill=X)
		self.video_streams.pack(side=TOP, fill=BOTH)
		self.video_title.pack(side=TOP, expand=TRUE, fill=X)
		self.video_author.pack(side=TOP, expand=TRUE, fill=X)
		self.video_duration.pack(side=TOP, expand=TRUE, fill=X)

		#bottom frame
		self.bottom_frame.pack(side=TOP, expand=TRUE, fill=BOTH)
		self.sort_options_menu.pack(side=LEFT)

class MixerWindow(tk.Tk):
	def __init__(self):
		super().__init__()
		
		self.title(f"Mixer")
		self.geometry("800x400+560+340")
		self.resizable(False,False)
		self.iconbitmap(f"{PROJECT_DIR}\\img\\icon.ico")
	

if __name__ == '__main__':
	app = MixerWindow()
	app.mainloop()

