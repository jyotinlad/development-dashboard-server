from unittest import main, TestCase
from unittest.mock import patch

from python.listing import Listing


class ListingTests(TestCase):

    _BASE_URL = "python.listing"

    @patch(f"{_BASE_URL}.Sheets.fetch")
    def test_get(self, mock_fetch):
        data = ["foo", "bar", "baz"]

        spreadsheet_data = {
            "values": [
                [data[0]],
                [data[1]],
                [data[2]]
            ]
        }
        mock_fetch.return_value = spreadsheet_data

        self.assertListEqual(Listing.get("type"), data)


if __name__ == "__main__":
    main()
