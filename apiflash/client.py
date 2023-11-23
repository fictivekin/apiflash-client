
from apiclient import (
    APIClient,
    JsonResponseHandler,
    QueryParameterAuthentication,
    RequestsResponseHandler,
)

from .constants import (
    CaptureOptions,
    Endpoint,
    ImageFormat,
    ResponseType,
)
from .error_handler import ApiFlashErrorHandler
from .exceptions import (
    InvalidCaptureOptionError,
    NoAccessKeyError,
)


class ApiFlashClient(APIClient):
    """ApiFlash.com client"""

    image_format = ImageFormat.PNG
    response_type = ResponseType.JSON
    fail_on_status = '400-599'

    def __init__(self, access_key, *, image_format=None, response_type=None, fail_on_status=None):
        if not access_key:
            raise NoAccessKeyError()

        super().__init__(
            authentication_method=QueryParameterAuthentication(
                'access_key',
                access_key,
            ),
            error_handler=ApiFlashErrorHandler,
        )

        if image_format is not None:
            self.image_format = image_format
        if response_type is not None:
            self.response_type = response_type
        if fail_on_status is not None:
            self.fail_on_status = fail_on_status

    def _autoswitch_handler(self, response_type):
        """Based on the response type requested, set the request handler appropriately"""

        self.set_response_handler(
            RequestsResponseHandler if response_type == ResponseType.IMAGE else JsonResponseHandler
        )

    def capture(self, url, *, ignore_unknown_options=False, **kwargs):
        """Capture a screenshot of the given URL"""

        if not ignore_unknown_options:
            # pylint: disable=consider-iterating-dictionary
            for k in kwargs.keys():
                if k not in CaptureOptions:
                    raise InvalidCaptureOptionError(k)

        kwargs['url'] = url

        if 'response_type' not in kwargs:
            kwargs['response_type'] = self.response_type
        if 'format' not in kwargs:
            kwargs['format'] = self.image_format
        if 'fail_on_status' not in kwargs:
            kwargs['fail_on_status'] = self.fail_on_status

        self._autoswitch_handler(kwargs['response_type'])
        resp = self.get(Endpoint.screenshot, kwargs)
        return resp.content if kwargs['response_type'] == ResponseType.IMAGE else resp

    def quota(self):
        """Get the quota information for the current access key"""

        self._autoswitch_handler(ResponseType.JSON)
        return self.get(Endpoint.quota)
