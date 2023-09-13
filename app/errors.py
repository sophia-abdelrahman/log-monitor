# app/errors.py

class ValidationError(Exception):
    """Base validation exception."""
    pass

class KeywordError(ValidationError):
    """Exception raised for invalid keyword."""
    pass

class FileNameError(ValidationError):
    """Exception raised for invalid filename."""
    pass

class LastNError(ValidationError):
    """Exception raised for invalid last_n value."""
    pass
