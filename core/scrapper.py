from bs4 import BeautifulSoup
from core.requester import Requester
from core.logger import Logger
from core.colors import *
import warnings
from rich.console import Console
from core.utils import *

# to prevent console stdout of warnings from bs4 module
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


class Scrapper:
    """
    Scrapper module to scrape data from web response.
    """

    def __init__(self, city, query, pages):
        self.city = city
        self.query = query
        self.pages = pages

    service_count = 0

    @classmethod
    def scrape(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        services = soup.find_all('li', {'class': 'cntanr'})

        console = Console()
        with console.status("[bold green]Scrapping data...") as status:
            for service_html in services:
                dict_data = {}
                name = get_name(service_html)
                phone = get_phone_number(service_html)
                rating = get_rating(service_html)
                count = get_rating_count(service_html)
                address = get_address(service_html)
                location = get_location(service_html)
                if name:
                    dict_data['Name'] = name
                if phone:
                    dict_data['Contact'] = phone
                if rating:
                    dict_data['Rating'] = rating
                if count:
                    dict_data['Rating Count'] = count
                if address:
                    dict_data['Address'] = address
                if location:
                    dict_data['Address'] = location
                write_data(dict_data)
                console.log(f"{str(self.service_count+1)}{dict_data}")
                self.service_count += 1
        return self.service_count

    @classmethod
    def start(self, city, query, pages):
        for page in range(pages+1):
            url = f'https://www.justdial.com/{city.title()}/{query}/nct-11216691/page-{page}'
            response = Requester.Request(url)
            self.scrape(response)

        Logger.info(f'Total {R}{self.service_count}{N} Services found.')
