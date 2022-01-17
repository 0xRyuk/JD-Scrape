from core.logger import *
import requests


class Requester:
    """
    Requester module to make web requests to website, and return respone data object.
    """
    # create session to make faster web requests.
    session = requests.Session()

    @classmethod
    def Request(self, url):
        # used user-agent because website was blocking request.
        User_Agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
        }
        try:
            response = self.session.get(url, headers=User_Agent)
            return response
        # error handling stuff is here.
        except (requests.ConnectionError, requests.Timeout):
            Logger.error('Please check your internet conectivity!')
            quit()
