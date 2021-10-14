class BaseException(Exception):
    
    
    def __init__(self, message, code = None, *args: object) -> None:
        super().__init__(*args)
        self.message = message
        self.code = code

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self) -> str:
        return super().__str__()

class DirectoryExists(BaseException):
    pass