# Visit pyGuru on youtube
# pip install pygame

import os
import pickle
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from pygame import mixer

class Player(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		mixer.init()

		if os.path.exists('songs.pickle'):
			with open('songs.pickle', 'rb') as 
				self.playlist = pickle.load(f)
		else:
			self.playlist=[]

		self.current = 0
		self.paused = True
		self.played = False

		self.create_frames()
		self.track_widgets()
		self.control_widgets()
		self.tracklist_widgets()

	def create_frames(self):
		self.track = tk.LabelFrame(self, text='
					font=("times new roman",15,
					bg="grey",fg="white",bd=5,r
		self.track.config(width=410,height=300)
		self.track.grid(row=0, column=0, padx=1

		self.tracklist = tk.LabelFrame(self, te
							font=("times new ro
							bg="grey",fg="white
		self.tracklist.config(width=190,height=
		self.tracklist.grid(row=0, column=1, ro

		self.controls = tk.LabelFrame(self,
							font=("times new ro
							bg="white",fg="whit
		self.controls.config(width=410,height=8
		self.controls.grid(row=2, column=0, pad

	def track_widgets(self):
		self.canvas = tk.Label(self.track, imag
		self.canvas.configure(width=400, height
		self.canvas.grid(row=0,column=0)

		self.songtrack = tk.Label(self.track, f
						bg="white",fg="dark blu
		self.songtrack['text'] = 'Musicxy MP3 P
		self.songtrack.config(width=30, height=
		self.songtrack.grid(row=1,column=0,padx

	def control_widgets(self):
		self.loadSongs = tk.Button(self.control
		self.loadSongs['text'] = 'Load Songs'
		self.loadSongs['command'] = self.retrie
		self.loadSongs.grid(row=0, column=0, pa

		self.prev = tk.Button(self.controls, im
		self.prev['command'] = self.prev_song
		self.prev.grid(row=0, column=1)

		self.pause = tk.Button(self.controls, i
		self.pause['command'] = self.pause_song
		self.pause.grid(row=0, column=2)

		self.next = tk.Button(self.controls, im
		self.next['command'] = self.next_song
		self.next.grid(row=0, column=3)

		self.volume = tk.DoubleVar(self)
		self.slider = tk.Scale(self.controls, f
		self.slider['variable'] = self.volume
		self.slider.set(8)
		mixer.music.set_volume(0.8)
		self.slider['command'] = self.change_vo
		self.slider.grid(row=0, column=4, padx=


	def tracklist_widgets(self):
		self.scrollbar = tk.Scrollbar(self.trac
		self.scrollbar.grid(row=0,column=1, row

		self.list = tk.Listbox(self.tracklist, 
					 yscrollcommand=self.scroll
		self.enumerate_songs()
		self.list.config(height=22)
		self.list.bind('<Double-1>', self.play_

		self.scrollbar.config(command=self.list
		self.list.grid(row=0, column=0, rowspan

	def retrieve_songs(self):
		self.songlist = []
		directory = filedialog.askdirectory()
		for root_, dirs, files in os.walk(direc
				for file in files:
					if os.path.splitext(file)[1
						path = (root_ + '/' + f
						self.songlist.append(pa

		with open('songs.pickle', 'wb') as f:
			pickle.dump(self.songlist, f)
		self.playlist = self.songlist
		self.tracklist['text'] = f'PlayList - {
		self.list.delete(0, tk.END)
		self.enumerate_songs()

	def enumerate_songs(self):
		for index, song in enumerate(self.playl
			self.list.insert(index, os.path.bas


	def play_song(self, event=None):
		if event is not None:
			self.current = self.list.curselecti
			for i in range(len(self.playlist)):
				self.list.itemconfigure(i, bg="

		print(self.playlist[self.current])
		mixer.music.load(self.playlist[self.cur
		self.songtrack['anchor'] = 'w' 
		self.songtrack['text'] = os.path.basena

		self.pause['image'] = play
		self.paused = False
		self.played = True
		self.list.activate(self.current) 
		self.list.itemconfigure(self.current, b

		mixer.music.play()

	def pause_song(self):
		if not self.paused:
			self.paused = True
			mixer.music.pause()
			self.pause['image'] = pause
		else:
			if self.played == False:
				self.play_song()
			self.paused = False
			mixer.music.unpause()
			self.pause['image'] = play

	def prev_song(self):
		if self.current > 0:
			self.current -= 1
		else:
			self.current = 0
		self.list.itemconfigure(self.current + 
		self.play_song()

	def next_song(self):
		if self.current < len(self.playlist) - 
			self.current += 1
		else:
			self.current = 0
		self.list.itemconfigure(self.current - 
		self.play_song()

	def change_volume(self, event=None):
		self.v = self.volume.get()
		mixer.music.set_volume(self.v / 10)

# ----------------------------- Main ----------

root = tk.Tk()
root.geometry('600x400')
root.wm_title('Musicxy')

img = PhotoImage(file='images/music.gif')
next_ = PhotoImage(file = 'images/next.gif')
prev = PhotoImage(file='images/previous.gif')
play = PhotoImage(file='images/play.gif')
pause = PhotoImage(file='images/pause.gif')

app = Player(master=root)
app.mainloop()
<a href="C:\Users\Karthik Rja S\OneDrive\Desktop ">
<a>