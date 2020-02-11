from bs4 import BeautifulSoup
import requests

def get_speciality(website):

    try:
        # list of specialties
        speciality_arr = ['/spa-medicine-directory']
        # cat = requests.get(website + '/specialty-directory')
        # ca = cat.content
        # soup = BeautifulSoup(ca, 'html.parser')
        # catogories = soup.find_all('li', class_='listArray__name')
        # for catogory in catogories:
        #     speciality_arr.append(catogory.a['href'])
        # collecting the state directory
        for spec in speciality_arr:
            name = spec.split('/')
            urlf = open(name[-1]+'.txt', 'w+')
            print(spec)
            st = requests.get(website + spec)
            t = st.content
            soup1 = BeautifulSoup(t, 'html.parser')
            st_dir = soup1.find_all('li', class_='listArray__name')
            states_arr = []
            for states in st_dir:
                states_arr.append(states.a['href'])
            print(states_arr)
            # collecting the cities
            city_arr = []
            for city in states_arr:
                ct = requests.get(website + city)
                c = ct.content
                soup2 = BeautifulSoup(c, 'html.parser')
                ct_dir = soup2.find_all('li', class_='link-column__list')
                for cit in ct_dir:
                    city_arr.append(cit.a['href'])
            print(city_arr)

            # prarsing the doctors to get doctor information
            doc_arr = []
            for doc in city_arr:
                dc = requests.get(website + doc)
                d = dc.content
                soup3 = BeautifulSoup(d, 'html.parser')
                doc_dir = soup3.find_all('a', class_= 'provider-name__lnk')
                for doctor in doc_dir:
                    doc_arr.append(doctor['href'])
            print(doc_arr)

            # writing the doctor URL's to a text file
            for doc in doc_arr:
                urlf.write(doc + '\n')

    except:
        pass


get_speciality('https://www.healthgrades.com')
