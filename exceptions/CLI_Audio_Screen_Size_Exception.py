#This class handles exceptions for the program if the screen size of the CLI audio player is not big enough

class CLI_Audio_Screen_Size_Exception(CLI_Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors