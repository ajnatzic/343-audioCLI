#This main exception class serves as an interface for all exceptions in the CLI audio player.

class CLI_Exception(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class CLI_Audio_File_Exception(CLI_Exception):
    def __init__(self, message, errors):
        super().__init__(message,errors)
        self.errors = errors

class CLI_Audio_Screen_Size_Exception(CLI_Exception):
    def __init__(self, message, errors):
        super().__init__(message,errors)
        self.errors = errors