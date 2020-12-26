from json import dumps
from unittest import main, TestCase
from unittest.mock import Mock, patch

from python.google.sheets import Sheets


class SheetsTests(TestCase):

    _BASE_URL = "python.google.sheets"

    @patch(f"{_BASE_URL}.getenv", side_effect=lambda x: x)
    @patch(f"{_BASE_URL}.get")
    def test_fetch(self, mock_get, mock_getenv):
        response = {"foo": "bar"}
        mock_get.return_value = Mock(text=dumps(response))

        sheet = "SHEET"
        self.assertDictEqual(Sheets.fetch(sheet), response)

        mock_get.assert_called_once_with(
            url=f"https://sheets.googleapis.com/v4/spreadsheets/"
                f"GOOGLE_SHEETS_FILE_ID/values/{sheet}?key=GOOGLE_API_KEY"
        )


if __name__ == "__main__":
    main()
