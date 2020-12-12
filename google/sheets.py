from dotenv import load_dotenv
from json import loads
from os import getenv
from requests import get


class Sheets:

    @staticmethod
    def fetch(sheet):
        load_dotenv()
        file_id = getenv("FILE_ID")
        api_key = getenv("GOOGLE_API_KEY")

        res = get(url=f"https://sheets.googleapis.com/v4/spreadsheets/{file_id}/values/{sheet}?key={api_key}")
        return loads(res.text)
