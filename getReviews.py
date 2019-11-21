from bs4 import BeautifulSoup
import requests
import re
import json
import csv
import mechanize
from readTx import readTx

def get_reviews(website):

    # reading from the text files
    content = readTx()
    cardio_dict = {}
    for phy in content:
        try:
            ph = requests.get(website + phy)
            p = ph.content
            soup = BeautifulSoup(p, 'html.parser')
            scripts = str(soup.find_all('script', type='text/javascript', string=re.compile('pageState.pes')))
            pes = scripts.splitlines()
            json_f = pes[6].strip('').strip('pageState.pes = ')[:-1]
            json_data = json.loads(json_f)

            # get the state and zipcode
            addr = soup.find('address', class_='location-row-address')
            addr = addr.text
            bit = addr.split()
            state = bit[-2]
            overall_ratings = soup.find('p', class_='score').getText()
            total_rev = soup.find('p', class_='survey-count').getText()
            total_rev = total_rev.strip('Based on reviews')
            print(total_rev, overall_ratings)

            # reviews
            reviews = [i['commentText'] for i in json_data['model']['comments']['results'] if (len(i) != 0)]
            if state in cardio_dict:
                cardio_dict[state] = cardio_dict[state] + reviews
            else:
                cardio_dict[state] = reviews
            # print(cardio_dict)
        except:
            pass

    with open('cardio.csv', 'w') as f:
        w = csv.DictWriter(f, cardio_dict.keys())
        w.writeheader()
        w.writerow(cardio_dict)


get_reviews('https://www.healthgrades.com')
