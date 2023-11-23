
ApiFlash.com Client
===================

The ApiFlash Client is a Python module for interacting with apiflash_. It requires Python 3.7+.

Installation
------------

In a Python virtual environment::

    $ pip install apiflash-client


Example usage
-------------

Setup a client::

    from apiflash import ApiFlashClient

    access_key = '<your-access-key>'

    client = ApiFlashClient(access_key)


Check the quota of your account::

    print(client.quota())


Capture a screenshot of a URL::

    resp = client.capture(
        'https://google.com',
    )
    print(resp['url'])


Capture a screenshot of a URL with some parameters::

    from apiflash import ImageFormat

    resp = client.capture(
        'https://google.com',
        width=400,
        height=600,
        format=ImageFormat.WEBP,
    )
    print(resp['url'])


Capture a screenshot of a URL, but return the image data, rather than a screentshot URL::

    from apiflash import ResponseType

    data = client.capture(
        'https://google.com',
        response_type=ResponseType.IMAGE,
    )

    with open('my-file.png', 'wb') as filehandle:
        filehandle.write(data)


All available capture options can be found here_.


Command line usage
------------------

Once installed in your virtual environment, you can use the command line interface. You will need to pass ``--access-key <your-access-key>`` or set ``APIFLASH_ACCESS_KEY`` in your environment for the command line to authenticate with apiflash.com::

    $ apiflash quota
    {'limit': 100, 'remaining': 91, 'reset': 1703265314}

    $ apiflash capture https://google.com
    https://api.apiflash.com/v1/urltoimage/cache/8jzv236knw.png?access_key=<your-access-key>

    $ apiflash capture https://google.com -o width 400 -o height 600
    https://api.apiflash.com/v1/urltoimage/cache/5asdf65asd.png?access_key=<your-access-key>

If you are using ngrok_ to expose a local development environment, you will need to pass ``-o headers ngrok-skip-browser-warning=yes`` to the command line utility. The same can be passed as a keyword argument to the ``capture()`` method, if retrieving the screenshot programmatically.


.. _apiflash: https://apiflash.com
.. _here: https://apiflash.com/documentation#parameters
.. _ngrok: https://ngrok.com
