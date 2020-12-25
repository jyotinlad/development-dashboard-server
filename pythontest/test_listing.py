from unittest import main, TestCase
from unittest.mock import patch

# from python.google.sheets import Sheets


class ListingTests(TestCase):

    _BASE_URL = "python.google.listing"

    def setUp(self):
        pass


    # @patch(f"{_BASE_URL}.Sheets")
    def test_get(self):
        pass
        # data = Sheets.fetch(type)
        # return [v[0] for v in data.get("values")]


if __name__ == "__main__":
    main()
