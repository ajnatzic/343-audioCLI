#This class handles exceptions for the program if it can't find the requested audio file from user

class CLI_Audio_File_Exception(CLI_Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors