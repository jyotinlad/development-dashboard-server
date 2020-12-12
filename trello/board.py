from datetime import datetime

from .request import Request


class Board:

    def __init__(self, board_id):
        self._request = Request()
        board = self._request.get("boards", board_id)

        self.board_id = board_id
        self.name = board.get("name", "Undefined Board")

    def completed(self):
        lists = self._request.get("boards", self.board_id, "lists")

        data = []
        for list_object in lists:
            if list_object.get("name") == "Done":
                list_id = list_object.get("id")

                cards = self._request.get("lists", list_id, "cards")
                for card in cards:
                    if not card.get("dueComplete"):
                        continue

                    data.append({
                        "title": card.get("name"),
                        "completed_date": datetime.strptime(card.get("due"), "%Y-%m-%dT%H:%M:%S.%fZ")
                    })

        return data
