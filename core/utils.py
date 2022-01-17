from bs4 import BeautifulSoup

"""
Utility module of utility functions for scrapper, that helps in importent jobs.
"""
# get names from span element.
def get_name(body):
    return body.find('span', {'class': 'jcn'}).a.string

# checks for digits of phone numbers in website.
def which_digit(html):
    mappingDict = {'icon-ji': 9,
                   'icon-dc': '+',
                   'icon-fe': '(',
                   'icon-hg': ')',
                   'icon-ba': '-',
                   'icon-lk': 8,
                   'icon-nm': 7,
                   'icon-po': 6,
                   'icon-rq': 5,
                   'icon-ts': 4,
                   'icon-vu': 3,
                   'icon-wx': 2,
                   'icon-yz': 1,
                   'icon-acb': 0,
                   }
    return mappingDict.get(html, '')

# get phone numbers from scrapped data.
def get_phone_number(body):
    i = 0
    phoneNo = "No Number!"
    try:

        for item in body.find('p', {'class': 'contact-info'}):
            i += 1
            if(i == 2):
                phoneNo = ''
                try:
                    for element in item.find_all(class_=True):
                        classes = []
                        classes.extend(element["class"])
                        phoneNo += str((which_digit(classes[1])))
                except:
                    pass
    except:
        pass
    body = body['data-href']
    soup = BeautifulSoup(body, 'html.parser')
    for a in soup.find_all('a', {"id": "whatsapptriggeer"}):
        phoneNo = str(a['href'][-10:])

    return phoneNo


csvwriter = None

# data writer that writes rows


def write_data(data):
    csvwriter.writerow(data)

# get ratings from scrapped data
def get_rating(body):
    rating = 0.0
    text = body.find('span', {'class': 'star_m'})
    if text is not None:
        for item in text:
            rating += float(item['class'][0][1:])/10

    return rating

# get rating counts
def get_rating_count(body):
    text = body.find('span', {'class': 'rt_count'}).string
    # Get only digits
    rating_count = ''.join(i for i in text if i.isdigit())
    return rating_count

# get addresses from span element
def get_address(body):
    return body.find('span', {'class': 'mrehover'}).text.strip()

# get location of the shops
def get_location(body):
    text = body.find('a', {'class': 'rsmap'})
    if text == None:
        return
    text_list = text['onclick'].split(",")

    latitutde = text_list[3].strip().replace("'", "")
    longitude = text_list[4].strip().replace("'", "")

    return latitutde + ", " + longitude
