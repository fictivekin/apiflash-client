# pylint: disable=too-few-public-methods

from apiclient import endpoint


# Define endpoints, using the provided decorator.
@endpoint(base_url="https://api.apiflash.com")
class Endpoint:
    """All the available endpoints of the API"""

    screenshot = "v1/urltoimage"
    quota = "v1/urltoimage/quota"


class ImageFormat:
    """Supported image formats"""

    WEPB = 'webp'
    PNG = 'png'
    JPEG = 'jpeg'


class ResponseType:
    """Allowed response types"""

    JSON = 'json'
    IMAGE = 'image'


# All possible options for `capture()`: https://apiflash.com/documentation#parameters
CaptureOptions = [  # pylint: disable=invalid-name
    'format',            # jpeg
    'width',             # in pixels: 1920
    'height',            # in pixels: 1080
    'fresh',             # false
    'full_page',         # false
    'quality',           # in percent: 80
    'delay',             # in secs: 0
    'scroll_page',       # false
    'ttl',               # in secs: 86400
    'response_type',     # image
    'thumbnail_width',   #
    'crop',              #
    'no_cookie_banners', # false
    'no_ads',            # false
    'no_tracking',       # false
    'scale_factor',      # 1
    'element',           #
    'element_overlap',   # false
    'user_agent',        #
    'extract_html',      # false
    'extract_text',      # false
    'transparent',       # false
    'wait_for',          #
    'wait_until',        # network_idle
    'fail_on_status',    #
    'accept_language',   #
    'css',               #
    'cookies',           #
    'proxy',             #
    'latitude',          #
    'longitude',         #
    'accuracy',          # in secs: 0
    'js',                #
    'headers',           #
    'time_zone',         #
    'ip_location',       #
    's3_access_key_id',  #
    's3_secret_key',     #
    's3_bucket',         #
    's3_key',            #
    's3_endpoint',       #
    's3_region',         #
]
