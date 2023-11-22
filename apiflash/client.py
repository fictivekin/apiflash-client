
from apiclient import (
    APIClient,
    endpoint,
    JsonResponseHandler,
    QueryParameterAuthentication,
    RequestsResponseHandler,
)


# Define endpoints, using the provided decorator.
@endpoint(base_url="https://api.apiflash.com")
class Endpoint:
    screenshot = "v1/urltoimage"
    quota = "v1/urltoimage/quota"


class ImageFormat:
    WEPB = 'webp'
    PNG = 'png'
    JPEG = 'jpeg'


class ResponseType:
    JSON = 'json'
    IMAGE = 'image'


# Extend the client for your API integration.
class ApiFlashClient(APIClient):

    image_format = ImageFormat.PNG
    response_type = ResponseType.JSON
    fail_on_status = '400-599'

    def __init__(self, access_key, *, image_format=None, response_type=None, fail_on_status=None):
        super().__init__(
            authentication_method=QueryParameterAuthentication(
                'access_key',
                access_key,
            ),
            response_handler=JsonResponseHandler,
        )

        if image_format is not None:
            self.image_format = image_format
        if response_type is not None:
            self.response_type = response_type
        if fail_on_status is not None:
            self.fail_on_status = fail_on_status

    def _autoswitch_handler(self, response_type):
        self.set_response_handler(
            RequestsResponseHandler if response_type == ResponseType.IMAGE else JsonResponseHandler
        )

    def capture(self, url, **kwargs):
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
        self._autoswitch_handler(ResponseType.JSON)
        return self.get(Endpoint.quota)
