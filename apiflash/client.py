
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

    def __init__(self, access_key, *, image_format=None, response_type=None):
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
            if response_type == ResponseType.IMAGE:
                self.set_response_handler(RequestsResponseHandler)

    def capture(self, url, **kwargs):
        kwargs['url'] = url

        if 'response_type' not in kwargs:
            kwargs['response_type'] = self.response_type
        elif kwargs['response_type'] != self.response_type:
            # This is a one-off request, switch it up
            self.set_response_handler(
                RequestsResponseHandler if kwargs['response_type'] == ResponseType.IMAGE else JsonResponseHandler
            )
        if 'format' not in kwargs:
            kwargs['format'] = self.image_format

        resp = self.get(Endpoint.screenshot, kwargs)

        if kwargs['response_type'] != self.response_type:
            # This was a one-off request, switch it back
            self.set_response_handler(
                RequestsResponseHandler if self.response_type == ResponseType.IMAGE else JsonResponseHandler
            )

        return resp.content if kwargs['response_type'] == ResponseType.IMAGE else resp
