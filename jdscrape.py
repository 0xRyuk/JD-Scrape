from core import utils
from core.colors import *
from core.logger import Logger
from core.scrapper import Scrapper
import argparse
import time
import csv

"""
Main scrapper programme that takes input as arguments and start working.
"""
def main():
    start = time.perf_counter()
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     usage=f'{W}jdscrape.py -q \"service name\" -c <city> [options]', epilog=epilog, add_help=False)
    parser.add_argument_group('Options')
    parser.add_argument('-h ', '--help', action='store_true',
                        default=False, help='Show usage and help options')
    parser.add_argument('-q', '--query', dest='query',
                        metavar='', help='Search Query')
    parser.add_argument('-c', '--city', dest='city',
                        metavar='', help='City Location')
    parser.add_argument('-f', '--file', dest='file', metavar='',
                        help='Filename to save results. [Default: \'justdial.csv\']', default='justdial.csv')
    parser.add_argument('-p', '--page', dest='pages', type=int, default=3,
                        metavar="", help="Pages to fetch results from. [Default: 3]")
    parser.add_argument('--about', action='store_true',
                        help='Print about information')

    args = parser.parse_args()

    query = args.query
    city = args.city
    pages = args.pages
    if args.about:
        print(about)
        quit()
    if not query or not city:
        parser.print_help()
        quit()
    fields = ['Name', 'Contact', 'Rating',
              'Rating Count', 'Address', 'Location']

    csvfile = open(args.file, 'w')
    csvwriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fields)
    utils.csvwriter = csvwriter
    setHeader = True
    if setHeader:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        setHeader = False
    if ' ' in query:
        query = query.replace(' ', '-')
    Logger.info(query)
    Logger.info(city.title())
    Scrapper.start(city.title(), query, pages)
    if os.path.isfile(args.file):
        Logger.info(f'Results saved in \'{C}{args.file}{N}\'')
    csvfile.close()
    end = time.perf_counter()
    Logger.info(f'Scraping finished in {G}{round(end-start,3)}{N} second(s)')


if __name__ == '__main__':
    try:
        print(banner)
        main()
    except KeyboardInterrupt:
        Logger.warning(R+'Exiting..'+N)

    except Exception as e:
        Logger.error(e)
