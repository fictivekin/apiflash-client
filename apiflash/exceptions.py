
from apiclient.exceptions import (
    APIClientError,
    APIRequestError,
)


# Errors thrown by the client, except those for HTTP reasons

class NoAccessKeyError(APIClientError):
    """There is no API key defined for the connection"""


class InvalidCaptureOptionError(APIClientError):
    """There is no API key defined for the connection"""


# Errors specific to ApiFlash requests

class BadRequestError(APIRequestError):
    """Either the API call contains invalid parameters or the target URL cannot be captured."""


class UnauthorizedError(APIRequestError):
    """The access key used to make this API call has been revoked or is invalid."""


class QuotaExceededError(APIRequestError):
    """The monthly screenshot quota has been exceeded for the user's current plan."""


class ForbiddenError(APIRequestError):
    """The current plan does not support some of the features requested through API parameters."""


class RateLimitedError(APIRequestError):
    """Too many API calls have been made. The specific reason is included in the response body."""
