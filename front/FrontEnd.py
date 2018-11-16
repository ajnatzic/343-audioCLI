import curses
import curses.textpad
import os
import sys
from exceptions.CLI_Exception import CLI_Audio_File_Exception
from exceptions.CLI_Exception import CLI_Audio_Screen_Size_Exception

#This class handles the front end of the CLI-audio player.
class FrontEnd:

    def __init__(self, player,library):
        self.player = player
        self.library = library
        self.directory = "./media"
        self.playlist = []
        self.player.play('./media/looperman.wav')
        curses.wrapper(self.menu)

    def menu(self, args):
        self.stdscr = curses.initscr()
        self.stdscr.border()
        height,width = self.stdscr.getmaxyx()

	#throws exception if screen size is not large enough
        if (height < 25):
            raise CLI_Audio_Screen_Size_Exception("ERROR: insufficient screen height","")
        if (width < 90):
            raise CLI_Audio_Screen_Size_Exception("ERROR: insufficient screen width","")

        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "l - Library")
        self.stdscr.addstr(9,10, "ESC - Quit")
        self.updateSong()
        self.stdscr.refresh()
        self.stdscr.addstr(14,10, "Available Songs: ")
        self.setPlaylist()
        self.displayPlaylist()
        while True:
            self.stdscr.addstr(13,10, "Current Directory: " + self.directory)
            c = self.stdscr.getch()
            if c == 27:
                self.quit()
            elif c == ord('p'):
                self.player.pause()
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord('l'):
                self.library.showLibrary(self)


    def updateSong(self):
        self.stdscr.addstr(15,10, "                                        ")
        self.stdscr.addstr(11,10, "Now playing: " + self.player.getCurrentSong())

    def changeSong(self):
        changeWindow = curses.newwin(5, 40, 5, 50)
        changeWindow.border()
        changeWindow.addstr(0,0, "Enter the index of the song: playlist length " + str(len(self.playlist)), curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        path = changeWindow.getstr(1,1, 1)
        curses.noecho()
        del changeWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        self.player.stop()

	#throws an exception if it can't find the song in the playlist
        try:
            if (int(path) > len(self.playlist)):
                self.stdscr.addstr(2,15, "Song not Found!")
                raise CLI_Audio_File_Exception("ERROR: can't find requested song in playlist","")

        except CLI_Audio_File_Exception:
            # print("Song not available")
            return
        except:
            return

        self.stdscr.addstr(2,15, "                            ")
        index = self.playlist[int(path)-1]
        songs = os.listdir(self.directory)
        song = self.directory + index
        self.player.play(song)

	#should display the playlist that the player is currently playing
    def displayPlaylist(self):

        x = 1
        for song in self.playlist:
            self.stdscr.addstr(15 + x,10, str(x) + ": "+ song)
            x = x + 1
	#sets the root directory
    def setDirectory(self,dir):
        self.directory = dir

	#puts all requested songs into a playlist
	#used "https://www.tutorialspoint.com/python/os_listdir.htm" to figure out how to use 'listdir()' in python
    def setPlaylist(self):
        self.playlist = []
        songs = os.listdir(self.directory)
        x = 0
        for song in songs:
            self.playlist.append(song)
            x = x + 1

    def quit(self):
        self.player.stop()
        exit()
