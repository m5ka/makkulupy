class BadResponseException(Exception):
    """Raised when the API response returns an error."""

    pass


class MalformedResponseException(Exception):
    """Raised when the API response cannot be properly parsed."""

    pass
