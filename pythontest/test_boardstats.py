from unittest import main, TestCase


class BoardStatsTests(TestCase):

    def test_get_end_of_month(self):
        # return dt.replace(day=monthrange(dt.year, dt.month)[1])
        pass

    def test_get_quarter_from_month(self):
        # return (month - 1) // 3 + 1
        pass

    def test_get_quarter_key(self):
        # quarter = cls._get_quarter_from_month(dt.month)
        # return cls._get_end_of_month(dt.replace(month=quarter*3, day=1))
        pass

    def test_quarterly(self):
        pass

    def test_monthly(self):
        pass


if __name__ == "__main__":
    main()
