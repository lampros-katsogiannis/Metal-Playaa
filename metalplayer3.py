from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os

mixer.init()

player = Tk()
player.geometry('700x200')
player.resizable(0, 0)

def play_song(song_name, songs_list, status):
	song_name.set(songs_list.get(ACTIVE))
	mixer.music.load(songs_list.get(ACTIVE))
	mixer.music.play()
	status.set("Song Playing")

def stop_song(status):
	mixer.music.stop()
	status.set("Song Stopped")

def load(listbox):
	os.chdir(filedialog.askdirectory(title='Songs directory'))
	tracks = os.listdir()

	for track in tracks:
		listbox.insert(END, track)

def pause_song(status):
	mixer.music.pause()
	status.set("Song Paused")

def resume_song(status):
	mixer.music.unpause()
	status.set("Song Resumed")

song_frame = LabelFrame(player, text='Song playing', bg='#CD5C5C', width=400, height=80)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(player, text='Controls', bg='#6495ED', width=400, height=120)
button_frame.place(y=80)

listbox_frame = LabelFrame(player, text='Playlist', bg='green')
listbox_frame.place(x=400, y=0, height=200, width=300)

current_song = StringVar(player, value='')

song_status = StringVar(player, value='')

playlist = Listbox(listbox_frame, font=('Arial', 11), selectbackground='Green')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)


Label(song_frame, text='------------------->:', bg='#CCCCFF', fg='red', font=('Times', 10, 'bold')).place(x=5, y=20)

song_lbl = Label(song_frame, textvariable=current_song, bg='Yellow', font=("Times", 12), width=25)
song_lbl.place(x=150, y=20)

pause_btn = Button(button_frame, text='Pause', bg='blue', font=("Georgia", 11), width=7,
	command=lambda: pause_song(song_status))
pause_btn.place(x=15, y=10)

stop_btn = Button(button_frame, text='Stop', bg='blue', font=("Georgia", 11), width=7,
	command=lambda: stop_song(song_status))
stop_btn.place(x=105, y=10)

play_btn = Button(button_frame, text='Play', bg='blue', font=("Georgia", 11), width=7,
	command=lambda: play_song(current_song, playlist, song_status))
play_btn.place(x=195, y=10)

resume_btn = Button(button_frame, text='Resume', bg='blue', font=("Georgia", 11), width=7,
	command=lambda: resume_song(song_status))
resume_btn.place(x=285, y=10)

load_btn = Button(button_frame, text='Open', bg='blue', font=("Georgia", 10), width=35, command=lambda: load(playlist))
load_btn.place(x=10, y=55)

Label(player, textvariable=song_status, bg='#D07E35', fg='white', font=('Times', 10), justify=LEFT).pack(side=BOTTOM, fill=X)

player.update()
player.mainloop()
