from json import dumps
from unittest import main, TestCase
from unittest.mock import Mock, patch

from python.trello.request import Request


class RequestTests(TestCase):

    _BASE_URL = "python.trello.request"

    @patch(f"{_BASE_URL}.getenv")
    def test_init(self, mock_getenv):
        # test base URL is not defined
        mock_getenv.side_effect = [None, None, None]
        with self.assertRaisesRegex(
            EnvironmentError,
            "the Trello base URL is not defined"
        ):
            Request()

        # test API key is not defined
        mock_getenv.side_effect = ["BASE_URL", None, None]
        with self.assertRaisesRegex(
            EnvironmentError,
            "the Trello API key is not defined"
        ):
            Request()

        # test token is not defined
        mock_getenv.side_effect = ["BASE_URL", "API_KEY", None]
        with self.assertRaisesRegex(
            EnvironmentError,
            "the Trello token is not defined"
        ):
            Request()

        # test valid call
        params = ["BASE_URL", "API_KEY", "TOKEN"]
        mock_getenv.side_effect = params
        req = Request()
        self.assertEqual(req._BASE_URL, params[0])
        self.assertEqual(req._API_KEY, params[1])
        self.assertEqual(req._TOKEN, params[2])

    @patch(f"{_BASE_URL}.Request.__init__")
    def test_get_params(self, mock_init):
        params = {
            "key": "API_KEY",
            "token": "TOKEN"
        }
        mock_self = Mock(_API_KEY=params["key"], _TOKEN=params["token"])

        mock_data = {"foo": "bar"}

        new_params = params.copy()
        new_params.update(mock_data)
        self.assertDictEqual(
            Request._get_params(mock_self, **mock_data),
            new_params
        )

    @patch(f"{_BASE_URL}.Request.__init__")
    def test_url_constructor(self, mock_init):
        base_url = "BASE_URL"
        mock_self = Mock(_BASE_URL=base_url)

        obj = "object"
        id = "id"
        return_object = "return_object"

        # test object URL
        self.assertEqual(
            Request._url_constructor(mock_self, obj, id),
            f"{base_url}/{obj}/{id}"
        )

        # test return object URL
        self.assertEqual(
            Request._url_constructor(mock_self, obj, id, return_object),
            f"{base_url}/{obj}/{id}/{return_object}"
        )

    @patch(f"{_BASE_URL}.request")
    @patch(f"{_BASE_URL}.Request.__init__")
    def test_get(self, mock_init, mock_request):
        url = "url"
        params = {"foo": "bar"}

        mock_self = Mock()
        mock_self._url_constructor.return_value = url
        mock_self._get_params.return_value = params

        response = {"a": "1", "b": "2", "c": "3"}
        mock_request.return_value = Mock(text=dumps(response))

        obj = "object"
        id = "id"
        return_object = "return_object"
        self.assertDictEqual(
            Request.get(mock_self, obj, id, return_object),
            response
        )

        mock_request.assert_called_once_with("GET", url, params=params)


if __name__ == "__main__":
    main()
