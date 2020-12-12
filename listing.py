from dotenv import load_dotenv
from google.sheets import Sheets


class Listing:

    @staticmethod
    def get(type):
        data = Sheets.fetch(type)
        return [v[0] for v in data.get("values")]
