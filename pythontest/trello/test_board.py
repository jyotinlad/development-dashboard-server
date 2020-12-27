from datetime import datetime
from unittest import main, TestCase
from unittest.mock import Mock, patch

from python.trello.board import Board


class BoardTests(TestCase):

    _BASE_URL = "python.trello.board"

    @patch(f"{_BASE_URL}.Request")
    def test_init(self, mock_request):
        board_id = "abc"
        board_data = {"name": "BOARD"}

        mock_request.return_value.get.return_value = board_data

        board = Board(board_id)
        self.assertEqual(board.board_id, board_id)
        self.assertEqual(board.name, board_data["name"])

    @staticmethod
    def _request_data(object, id, return_object):
        if object == "boards":
            return [
                {"id": 1, "name": "To Do"},
                {"id": 2, "name": "In Progress"},
                {"id": 3, "name": "Done"}
            ]
        elif object == "lists":
            if id == 2:
                return [
                    {
                        "name": "CARD-A",
                        "due": "2020-12-31T12:30:45.000Z",
                        "dueComplete": "2020-12-31"
                    },
                    {
                        "name": "CARD-B",
                        "due": "2020-12-31T12:30:45.000Z",
                        "dueComplete": "2020-12-31"
                    },
                    {
                        "name": "CARD-C",
                        "due": "2020-12-31T12:30:45.000Z"
                    }
                ]
            elif id == 3:
                return [
                    {
                        "name": "CARD-D",
                        "due": "2020-12-31T12:30:45.000Z",
                        "dueComplete": "2020-12-31"
                    },
                    {
                        "name": "CARD-E",
                        "due": "2020-12-31T12:30:45.000Z",
                        "dueComplete": "2020-12-31"
                    },
                    {
                        "name": "CARD-F",
                        "due": "2020-12-31T12:30:45.000Z"
                    }
                ]

    @patch(f"{_BASE_URL}.Board.__init__")
    def test_completed(self, mock_init):
        mock_self = Mock(board_id=1)
        mock_self._request.get.side_effect = self._request_data

        self.assertListEqual(
            Board.completed(mock_self),
            [
                {
                    "title": "CARD-D",
                    "completed_date": datetime(2020, 12, 31, 12, 30, 45)
                },
                {
                    "title": "CARD-E",
                    "completed_date": datetime(2020, 12, 31, 12, 30, 45)
                }
            ]
        )


if __name__ == "__main__":
    main()
