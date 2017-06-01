#Author: JK
#Python script to grab pollen index from wunderground.com (because no API support for this)
#Requires beautiful soup
from bs4 import BeautifulSoup

import urllib
import re

try:

    zipcode=63033


    #out = "<html>%s%s%s%s</html>" % (head, prologue, query, tail)
    head='https://weather.com/forecast/allergy/l/'
    tail=zipcode
    page = urllib.urlopen('%s%s' % (head, tail))
    soup = BeautifulSoup(page, "lxml")
    for breathing in soup.select("[class~=breathing__wrapper__heading]"):
        print breathing.text
    
    #Find first allergen label
    lbl = soup.find_all("span", {"class":"allergy-outlook__content__graph__msg__label"})
    label = len(soup.find_all("span", {"class":"allergy-outlook__content__graph__msg__label"}))
    first_label = lbl[label -3 ]
    print first_label.get_text()

    #find first allergen level
    pollen_lvl = soup.find_all("div", {"class":"allergy-outlook__content__graph__msg__qual"})
    number_of_allergens = len(soup.find_all("div", {"class":"allergy-outlook__content__graph__msg__qual"}))
    first_allergen = pollen_lvl[number_of_allergens -3 ]
    print first_allergen.get_text()

    #Find second allergen label
    lbl = soup.find_all("span", {"class":"allergy-outlook__content__graph__msg__label"})
    label = len(soup.find_all("span", {"class":"allergy-outlook__content__graph__msg__label"}))
    second_label = lbl[label -2 ]
    print second_label.get_text()

    #Find second allergen level
    ragweed_lvl = soup.find_all("div", {"class":"allergy-outlook__content__graph__msg__qual"})
    number_of_allergens = len(soup.find_all("div", {"class":"allergy-outlook__content__graph__msg__qual"}))
    second_allergen = ragweed_lvl[number_of_allergens -2 ]
    print second_allergen.get_text()

    #Find third allergen label
    lbl = soup.find_all("span", {"class":"allergy-outlook__content__graph__msg__label"})
    label = len(soup.find_all("span", {"class":"allergy-outlook__content__graph__msg__label"}))
    last_label = lbl[label -1 ]
    print last_label.get_text()

    #Find third allergen level
    tree_lvl = soup.find_all("div", {"class":"allergy-outlook__content__graph__msg__qual"})
    number_of_allergens = len(soup.find_all("div", {"class":"allergy-outlook__content__graph__msg__qual"}))
    last_allergen = tree_lvl[number_of_allergens -1 ]
    print last_allergen.get_text()


    


except urllib:
    print(e.reason)
