import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
base_url = "https://www.imoti.com/prodazhbi"

class Advertisement:
    def __init__(self, city="", neighborhood="", type="", size="", floor="", gas="", tpp="", price="", build_type=""):
        self.city = city
        self.neighborhood = neighborhood
        self.type = type
        self.size = size
        self.floor = floor
        self.gas = gas
        self.tpp = tpp
        self.price = price
        self.build_type = build_type

def get_links(soup, contains_href):
    all = soup.select("a[href*='" + contains_href + "']")
    cleared_links =  [el['href'].replace(base_url, "") for el in all]
    return unique(cleared_links)
    
def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def unique(list):
    npArray = np.array(list)
    uniqueNpArray = np.unique(npArray)
    return uniqueNpArray.tolist()

def get_ad_param(soup, param):
    try:
        return soup.find('i', string=param).find_next('span').get_text()
    except:
        return ""

def get_ad_data(soup):
    city = soup.select_one(".breadcrumbs .menuWrapper:nth-child(3)").text.strip()
    neighborhood = soup.select_one(".breadcrumbs .menuWrapper:nth-child(4)").text.strip()
    type = soup.select_one(".breadcrumbs .menuWrapper:nth-child(5)").text.strip()
    floor = get_ad_param(soup, "Етаж:")
    size = get_ad_param(soup, "Квадратура:")
    gas = get_ad_param(soup, "ГАЗ:")
    tpp = get_ad_param(soup, "ТЕЦ:")
    build_type = get_ad_param(soup, "Вид строителство:")
    price = soup.find('div', class_='price').find('span').text.strip()
    
    return Advertisement(city, neighborhood, type, size, floor, gas, tpp, price, build_type)
    
def save_as_xlsx(data):
    data = [{k: getattr(obj, k) for k in dir(obj) if not k.startswith('__')} for obj in data]
    properties_data = pd.DataFrame(data)
    properties_data.to_excel('properties.xlsx', index=False)
    
initial_soup = get_soup(base_url)
links = get_links(initial_soup, "prodazhbi")
data = []

for idx in range(len(links)):
    try:
        city_link = base_url + links[idx]
        initial_city_page_soup = get_soup(city_link)
        ad_links = get_links(initial_soup, "obiava")
        
        for page_number in range(100):
            page_link = city_link + "/page-" + str(page_number)
            page_soup = get_soup(page_link)
            ad_links.extend(get_links(page_soup, "obiava"))

        ad_links = unique(ad_links)
        
        for ad_link_idx in range(len(ad_links)):
            print(ad_links[ad_link_idx])
            ad_soup = get_soup(ad_links[ad_link_idx])
            record = get_ad_data(ad_soup)
            data.append(record)
    except:
        print("Error on: -" + base_url + links[idx])
        
save_as_xlsx(data)

