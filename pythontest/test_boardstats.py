from datetime import date, datetime
from freezegun import freeze_time
from unittest import main, TestCase
from unittest.mock import patch

from python.boardstats import BoardStats


class BoardStatsTests(TestCase):

    _BASE_URL = "python.boardstats"

    def test_get_end_of_month(self):
        self.assertEqual(
            BoardStats._get_end_of_month(datetime(2020, 12, 1)),
            datetime(2020, 12, 31)
        )

    def test_get_quarter_from_month(self):
        # test quarter 1
        self.assertEqual(BoardStats._get_quarter_from_month(1), 1)
        self.assertEqual(BoardStats._get_quarter_from_month(3), 1)

        # test quarter 2
        self.assertEqual(BoardStats._get_quarter_from_month(4), 2)
        self.assertEqual(BoardStats._get_quarter_from_month(6), 2)

        # test quarter 3
        self.assertEqual(BoardStats._get_quarter_from_month(7), 3)
        self.assertEqual(BoardStats._get_quarter_from_month(9), 3)

        # test quarter 4
        self.assertEqual(BoardStats._get_quarter_from_month(10), 4)
        self.assertEqual(BoardStats._get_quarter_from_month(12), 4)

    def test_get_quarter_key(self):
        # test quarter 1
        self.assertEqual(
            BoardStats._get_quarter_key(datetime(2020, 1, 1)),
            datetime(2020, 3, 31)
        )
        self.assertEqual(
            BoardStats._get_quarter_key(datetime(2020, 2, 28)),
            datetime(2020, 3, 31)
        )

        # test quarter 2
        self.assertEqual(
            BoardStats._get_quarter_key(datetime(2020, 4, 1)),
            datetime(2020, 6, 30)
        )
        self.assertEqual(
            BoardStats._get_quarter_key(datetime(2020, 6, 29)),
            datetime(2020, 6, 30)
        )

        # test quarter 3
        self.assertEqual(
            BoardStats._get_quarter_key(datetime(2020, 7, 1)),
            datetime(2020, 9, 30)
        )
        self.assertEqual(
            BoardStats._get_quarter_key(datetime(2020, 9, 29)),
            datetime(2020, 9, 30)
        )

        # test quarter 4
        self.assertEqual(
            BoardStats._get_quarter_key(datetime(2020, 10, 1)),
            datetime(2020, 12, 31)
        )
        self.assertEqual(
            BoardStats._get_quarter_key(datetime(2020, 12, 31)),
            datetime(2020, 12, 31)
        )

    @freeze_time("2020-12-31")
    @patch(f"{_BASE_URL}.Board")
    def test_quarterly(self, mock_board):
        mock_board.return_value.name = "BOARD"
        mock_board.return_value.completed.return_value = [
            {"completed_date": datetime(2020, 1, 1, 0, 0)},
            {"completed_date": datetime(2020, 2, 1, 0, 0)},
            {"completed_date": datetime(2020, 3, 31, 0, 0)},
            {"completed_date": datetime(2020, 4, 1, 0, 0)},
            {"completed_date": datetime(2020, 4, 1, 0, 0)},
            {"completed_date": datetime(2020, 5, 1, 0, 0)},
            {"completed_date": datetime(2020, 6, 30, 0, 0)},
            {"completed_date": datetime(2020, 7, 1, 0, 0)},
            {"completed_date": datetime(2020, 7, 1, 0, 0)},
            {"completed_date": datetime(2020, 7, 1, 0, 0)},
            {"completed_date": datetime(2020, 8, 1, 0, 0)},
            {"completed_date": datetime(2020, 9, 30, 0, 0)},
            {"completed_date": datetime(2020, 10, 1, 0, 0)},
            {"completed_date": datetime(2020, 10, 1, 0, 0)},
            {"completed_date": datetime(2020, 10, 1, 0, 0)},
            {"completed_date": datetime(2020, 10, 1, 0, 0)},
            {"completed_date": datetime(2020, 11, 1, 0, 0)},
            {"completed_date": datetime(2020, 12, 31, 0, 0)}
        ]

        self.assertDictEqual(
            BoardStats.quarterly(1),
            {
                "name": "BOARD",
                "records": {
                    date(2020, 3, 31): 3,
                    date(2020, 6, 30): 4,
                    date(2020, 9, 30): 5,
                    date(2020, 12, 31): 6,
                }
            }
        )

    @freeze_time("2020-12-31")
    @patch(f"{_BASE_URL}.Board")
    def test_monthly(self, mock_board):
        mock_board.return_value.name = "BOARD"
        mock_board.return_value.completed.return_value = [
            {"completed_date": datetime(2020, 1, 1, 0, 0)},
            {"completed_date": datetime(2020, 2, 1, 0, 0)},
            {"completed_date": datetime(2020, 3, 31, 0, 0)},
            {"completed_date": datetime(2020, 4, 1, 0, 0)},
            {"completed_date": datetime(2020, 4, 1, 0, 0)},
            {"completed_date": datetime(2020, 5, 1, 0, 0)},
            {"completed_date": datetime(2020, 6, 30, 0, 0)},
            {"completed_date": datetime(2020, 7, 1, 0, 0)},
            {"completed_date": datetime(2020, 7, 1, 0, 0)},
            {"completed_date": datetime(2020, 7, 1, 0, 0)},
            {"completed_date": datetime(2020, 8, 1, 0, 0)},
            {"completed_date": datetime(2020, 9, 30, 0, 0)},
            {"completed_date": datetime(2020, 10, 1, 0, 0)},
            {"completed_date": datetime(2020, 10, 1, 0, 0)},
            {"completed_date": datetime(2020, 10, 1, 0, 0)},
            {"completed_date": datetime(2020, 10, 1, 0, 0)},
            {"completed_date": datetime(2020, 11, 1, 0, 0)},
            {"completed_date": datetime(2020, 12, 31, 0, 0)}
        ]

        self.assertDictEqual(
            BoardStats.monthly(1),
            {
                "name": "BOARD",
                "records": {
                    date(2020, 7, 31): 3,
                    date(2020, 8, 31): 1,
                    date(2020, 9, 30): 1,
                    date(2020, 10, 31): 4,
                    date(2020, 11, 30): 1,
                    date(2020, 12, 31): 1,
                }
            }
        )


if __name__ == "__main__":
    main()
