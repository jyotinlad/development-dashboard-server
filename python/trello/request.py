from dotenv import load_dotenv
from json import loads
from os import getenv
from requests import request


class Request:

    def __init__(self):
        load_dotenv()
        self._BASE_URL = getenv("TRELLO_BASE_URL")
        self._API_KEY = getenv("TRELLO_API_KEY")
        self._TOKEN = getenv("TRELLO_TOKEN")

        if not self._TOKEN:
            raise EnvironmentError("the Trello TOKEN not defined")

        if not self._API_KEY:
            raise EnvironmentError("the Trello API key not defined")

    def _get_params(self, **kwargs):
        url_params = {
            "key": self._API_KEY,
            "token": self._TOKEN
        }
        url_params.update(kwargs)

        return url_params

    def _url_constructor(self, object, id, return_object=None):
        url = f"{self._BASE_URL}/{object}/{id}"
        if return_object:
            url = f"{url}/{return_object}"

        return url

    def get(self, object, id, return_object=None):
        response = request(
            "GET",
            self._url_constructor(object, id, return_object),
            params=self._get_params()
        )
        data = loads(response.text)
        return data
