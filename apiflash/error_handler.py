
from apiclient.error_handlers import ErrorHandler
from apiclient.exceptions import APIRequestError
from apiclient.response import Response

from .exceptions import (
    BadRequestError,
    ForbiddenError,
    QuotaExceededError,
    RateLimitedError,
    UnauthorizedError,
)


ApiExceptions = {  # pylint: disable=invalid-name
    '400': BadRequestError,
    '401': UnauthorizedError,
    '402': QuotaExceededError,
    '403': ForbiddenError,
    '429': RateLimitedError,
}


# pylint: disable=too-few-public-methods
class ApiFlashErrorHandler(ErrorHandler):
    """An error handler for ApiFlash specific error codes"""

    @staticmethod
    def get_exception(response: Response) -> APIRequestError:
        status_code = response.get_status_code()

        # Need these to be as strings, because a dict can't have an int key
        if str(status_code) in ApiExceptions:
            return ApiExceptions[str(status_code)](
                status_code=status_code,
                info=response.get_raw_data(),
            )

        return ErrorHandler.get_exception(response)
