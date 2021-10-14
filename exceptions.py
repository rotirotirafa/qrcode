class DefaultException(Exception):
    """
        Exception que serve de base para qualquer outra excessão.

        Attributes:
            message -- Display the information 
    """

    def __init__(self, message, *args: object) -> None:
        self.message = message
        super().__init__(message, *args)

    def __str__(self) -> str:
        return f'Error {self.message}'

