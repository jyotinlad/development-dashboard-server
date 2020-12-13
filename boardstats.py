from calendar import monthrange
from collections import Counter
from datetime import date, timedelta

from trello.board import Board


class BoardStats:

    @staticmethod
    def _get_end_of_month(dt):
        return dt.replace(day=monthrange(dt.year, dt.month)[1])

    @classmethod
    def _get_quarter_key(cls, dt):
        quarter = (dt.month - 1) // 3 + 1
        return cls._get_end_of_month(dt.replace(month=quarter*3, day=1))

    @classmethod
    def quarterly(cls, board_id):
        data = Counter()
        start_date = date.today() - timedelta(months=9)
        for i in range(4):
            dt = start_date + timedelta(months=i*3)
            quarter = cls._get_quarter_key(dt)
            print(quarter)
            data[quarter] = 0

        board = Board(board_id)
        records = board.completed()
        for record in records:
            completed_date = record.get("completed_date")
            quarter = cls._get_quarter_key(completed_date)
            if quarter not in data.keys():
                continue

            data[quarter] += 1

        return {"name": board.name, "records": dict(data)}

    @classmethod
    def monthly(cls, board_id):
        start_date = date.today()
        start_date = start_date.replace(day=1) - relativedelta(months=5)

        months = Counter()
        for i in range(6):
            month = start_date + relativedelta(months=i)
            months[month.replace(day=monthrange(month.year, month.month)[1])] += 0

        board = Board(board_id)
        records = board.completed()
        for record in records:
            completed_date = record.get("completed_date")
            completed_date = completed_date.replace(day=1).date()

            if completed_date < start_date:
                continue

            months[completed_date.replace(day=monthrange(completed_date.year, completed_date.month)[1])] += 1

        return {"name": board.name, "records": dict(months)}
