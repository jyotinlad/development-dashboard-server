from dotenv import load_dotenv
from json import loads
from os import getenv
from requests import get


class Sheets:

    @staticmethod
    def fetch(sheet):
        base_url = "https://sheets.googleapis.com/v4/spreadsheets"

        load_dotenv()
        file_id = getenv("GOOGLE_SHEETS_FILE_ID")
        api_key = getenv("GOOGLE_API_KEY")

        res = get(url=f"{base_url}/{file_id}/values/{sheet}?key={api_key}")
        return loads(res.text)
