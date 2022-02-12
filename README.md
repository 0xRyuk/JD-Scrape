# JD-Scrape
A python based data scrapper for website justdial[.]com

## Options

```usage
usage: jdscrape.py -q "service name" -c <city> [options]

optional arguments:
  -h , --help    Show usage and help options
  -q , --query   Search Query
  -c , --city    City Location
  -f , --file    Filename to save results. [Default: 'justdial.csv']
  -p , --page    Pages to fetch results from. [Default: 3]
  --about        Print about information

Github: https://www.github.com/0xRyuk
Version: 1.0
```

## Info

It scrapes data from justdial[.]com according to user query.

>url = f'hxxps://www[.]justdial.com/<span style="color: red;">{city.title()}/{query}</span>/nct-11216691/page<span style="color: red;">-{page}</span>'

## Requirements
```modules
beautifulsoup4==4.9.3
rich==10.12.0
requests==2.21.0
lxml==4.6.3
```

>pyhton3 -m pip install -r requirements.txt

## Usage
Basic usage

>python3 jdscrape.py -q "mobile shops" -c delhi

Extend search results and save results in a file

>python3 jdscrape.py -q "mobile shops" -c delhi -p 4 -f mobile-shops-delhi.csv

## Screenshots

<img src="https://i.ibb.co/Q6hV6H1/jdscrape.png" alt="jdscrape" border="0">
<img src="https://i.ibb.co/ynBY5cQ/about.png" alt="about" border="0">


# Twitter - [0xRyuk](https://twitter.com/0xRyuk)
