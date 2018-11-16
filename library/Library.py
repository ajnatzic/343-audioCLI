import curses
import curses.textpad
import os
import sys
from exceptions.CLI_Exception import CLI_Audio_File_Exception
from exceptions.CLI_Exception import CLI_Audio_Screen_Size_Exception

#Creates a library class that allows searching multiple songs instead of having to
#type in each one individually

class Library:

	#Sets the working directory for the library to "/media"
        def _init_():
            self.files = os.listdir('./media')

	#shows all created playlists in the media library
        def showLibrary(self, parentView):

            changeWindow = curses.newwin(20, 50, 5, 5)
            changeWindow.addstr(2,10, "Available Playlists:")
            files = os.listdir('./media')
            x = 3
            for name in files:
                changeWindow.border()
                changeWindow.addstr(2+x,4, name)
                x = x + 1

            x = 1
            for name in files:
                changeWindow.border()
                changeWindow.addstr(4+x,2, str(x))
                x = x + 1



            parentView.stdscr.refresh()
            curses.echo()
            index = changeWindow.getstr(1,1, 1)

	#throws an exception if it cannot find the requested file
	#used "https://stackoverflow.com/questions/2817264/how-to-get-the-parent-dir-location" to figure out how to navigate directorys in python
            try:
                if (int(index) > len(files)):
                    parentView.stdscr.addstr(2,15, "Directory not Found!")
                    raise CLI_Audio_File_Exception("The song requested is not available in the playlist","CLI_AUDIO_FILE_EXCEPTION!")
                parentView.stdscr.addstr(2,15, "                            ")
            except CLI_Audio_File_Exception:
                index = 1
                # print("Song not available")

            except:
                parentView.stdscr.addstr(2,15, "Directory not Found!")
                index = 1



            parentView.setDirectory('./media/' + files[int(index)-1] + '/')
            parentView.setPlaylist()
            parentView.displayPlaylist()
            curses.noecho()
            del changeWindow
            parentView.stdscr.touchwin()
            parentView.stdscr.refresh()
