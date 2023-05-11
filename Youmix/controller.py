#https://www.youtube.com/watch?v=F7bKe_Zgk4o&list=PLS--x9YkaRc74mf2yNQb6s2GMLSZjsPd9&index=57 <---GOOD SONG
import traceback
import os
import sys
import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from pytube import YouTube
from threading import Thread, currentThread
from duration import format_length
from gui import MainWindow
from editor import EditWindow

class Controller(MainWindow):
	def __init__(self, version, title):
		super().__init__(version, title)

		self.process_in_progress = True
		self.audio_loaded = False
		self.current_streams = []

	def progress_func(self, stream, chunk, bytes_left):
		print(f"{bytes_left}/{self.filesize}")
		scaled_one = self.filesize/100
		bytes_downloaded = self.filesize-bytes_left
		update_amount = bytes_downloaded/scaled_one
		self.progress_title.config(text=f"{self.file_name} - {int(update_amount)}%")
		self.update_determinate_bar(update_amount)

	def complete_func(self, stream, path):
		file = os.path.basename(path)
		self.progress_title.config(text=f"{file} downloaded!")

	def pack_determinate_bar(self):
		self.progress_determinate_frame.pack(side=RIGHT)
		self.progress_title.pack(side=TOP)
		self.progress_determinate.pack(side=BOTTOM)

	def unpack_determinate_bar(self):
		self.progress_determinate_frame.pack_forget()
		self.progress_title.pack_forget()
		self.progress_determinate.pack_forget()

	def update_determinate_bar(self, amount):
		self.progress_determinate['value'] = amount

	def run_indeterminate_bar(self):
		self.process_in_progress = True
		self.progress_indeterminate.pack(side=RIGHT)
		self.progress_indeterminate.start()
		while self.process_in_progress:
			self.update()
		self.progress_indeterminate.stop()
		self.progress_indeterminate.pack_forget()

	def load_video(self):
		_url = self.url_text.get()
		if _url.lower().startswith("http"):
			self.button_states(False)
			self.unpack_determinate_bar()
			self.execute_thread(self.run_indeterminate_bar, "run_indeterminate_bar()")

			self.video_title.config(text="Converting video...")
			self.video_author.config(text="")
			self.video_duration.config(text="")
			self.video_streams.delete(0, (self.video_streams.size()-1))

			self.yt = YouTube(_url, use_oauth=True, on_progress_callback=self.progress_func, on_complete_callback=self.complete_func)
			self.yt.bypass_age_gate()

			self.video_duration.config(text=format_length(self.yt.length))
			self.video_title.config(text=self.yt.title)
			self.video_author.config(text=self.yt.author)
			self.audio_asc = self.yt.streams.filter(only_audio=True).order_by('abr')
			self.audio_desc = self.yt.streams.filter(only_audio=True).order_by('abr')[::-1]
			self.audio_loaded = True
			self.sort_streams()

			self.process_in_progress = False
			self.button_states(True)

		else:
			self.video_title.config(text="Enter a valid url")

	def execute_thread(self, func, name):
		t = currentThread()
		print(f"Initializing thread {t} for {name}")

		thread = Thread(target=func)
		thread.start()

	def sort_streams(self, *args):	
		if self.audio_loaded:
			self.video_streams.delete(0, (self.video_streams.size()-1))
			sort = self.sort_var.get()
			if sort == "Ascending Quality":
					self.current_streams = self.audio_asc
			elif sort == "Descending Quality":
				self.current_streams = self.audio_desc
	
			for stream in self.current_streams:
					self.video_streams.insert(END, stream)
		else:
			pass

	def button_states(self, state: bool):
		if state:
			self.convert_button['state'] = NORMAL
			self.menubar.entryconfig("File", state="normal")
		elif not state:
			self.convert_button['state'] = DISABLED
			self.menubar.entryconfig("File", state="disabled")
		else:
			pass
	
	def save_selected(self):
		self.button_states(False)

		selected_indices = [i for i in self.video_streams.curselection()]
		if len(selected_indices) is 0:
			print("Select streams")
		else:
			files = [('Mp3 Files', '*.mp3'),
					 ('Webm Files', '*.webm')]
			
			save_path = fd.asksaveasfilename(parent=self, filetypes=files, defaultextension=".mp3")
			path = os.path.dirname(save_path)
			self.pack_determinate_bar()
			itags = [self.current_streams[t].itag for t in selected_indices]
			for tag in itags:
				self.progress_determinate['value'] = 0
				stream = self.yt.streams.get_by_itag(tag)
				self.progress_title.config(text=stream.title)
				quality = stream.abr
				self.filesize = stream.filesize
				self.file_name = f"{quality}--{os.path.basename(save_path)}"
				self.progress_title.config(text=f"{self.file_name} - 0%")
				stream.download(output_path=path, filename=self.file_name, timeout=5, max_retries=5)

		self.button_states(True)

	def save_all(self):
		self.button_states(False)	
		self.pack_determinate_bar()

		files = [('Mp3 Files', '*.mp3'),
				 ('Webm Files', '*.webm')]
		save_path = fd.asksaveasfilename(parent=self, filetypes=files, defaultextension=".mp3")
		path = os.path.dirname(save_path)

		for item in range(self.video_streams.size()):
			self.progress_determinate['value'] = 0
			itag = self.current_streams[item].itag
			stream = self.yt.streams.get_by_itag(itag)
			self.filesize = stream.filesize
			quality = stream.abr
			self.file_name = f"{quality}--{os.path.basename(save_path)}"
			self.progress_title.config(text=f"{self.file_name} - 0%")
			stream.download(output_path=path, filename=self.file_name)

		self.button_states(True)

	def edit_selected(self):
		app = EditWindow()
		app.mainloop()


if __name__ == '__main__':
	pass
	
