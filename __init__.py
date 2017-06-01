# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from bs4 import BeautifulSoup

import urllib
import re


__author__ = 'eclarity'

LOGGER = getLogger(__name__)


class PollenSkill(MycroftSkill):
    def __init__(self):
        super(PollenSkill, self).__init__(name="PollenSkill")
	self.zipcode=self.config['zipcode']

    def initialize(self):
        comfort_intent = IntentBuilder("ComfortIntent"). \
            require("ComfortKeyword").build()
        self.register_intent(comfort_intent, self.handle_comfort_intent)

        allergen_intent = IntentBuilder("AllergenIntent"). \
            require("AllergenKeyword").build()
        self.register_intent(allergen_intent, self.handle_allergen_intent)


    def handle_comfort_intent(self, message):
	self.speak("The current breathing comfort level for your area is ")
	head='https://weather.com/forecast/allergy/l/'
        tail=self.zipcode
        page = urllib.urlopen('%s%s' % (head, tail))
        soup = BeautifulSoup(page, "lxml")
        for breathing in soup.select("[class~=breathing__wrapper__heading]"):
	    response = breathing.text
	    self.speak(response)

    def handle_allergen_intent(self, message):
	head='https://weather.com/forecast/allergy/l/'
        tail=self.zipcode
        page = urllib.urlopen('%s%s' % (head, tail))
        soup = BeautifulSoup(page, "lxml")

        #Find first allergen label
        lbl = soup.find_all("span", {"class":"allergy-outlook__content__graph__msg__label"})
        label = len(soup.find_all("span", {"class":"allergy-outlook__content__graph__msg__label"}))
        first_label = lbl[label -3 ]
        f_label = first_label.get_text()
	self.speak(f_label)

        #find first allergen level
        pollen_lvl = soup.find_all("div", {"class":"allergy-outlook__content__graph__msg__qual"})
        number_of_allergens = len(soup.find_all("div", {"class":"allergy-outlook__content__graph__msg__qual"}))
        first_allergen = pollen_lvl[number_of_allergens -3 ]
        f_allergen = first_allergen.get_text()
	self.speak(f_allergen)

        #Find second allergen label
        lbl = soup.find_all("span", {"class":"allergy-outlook__content__graph__msg__label"})
        label = len(soup.find_all("span", {"class":"allergy-outlook__content__graph__msg__label"}))
        second_label = lbl[label -2 ]
        s_label = second_label.get_text()
	self.speak(s_label)

        #Find second allergen level
        ragweed_lvl = soup.find_all("div", {"class":"allergy-outlook__content__graph__msg__qual"})
        number_of_allergens = len(soup.find_all("div", {"class":"allergy-outlook__content__graph__msg__qual"}))
        second_allergen = ragweed_lvl[number_of_allergens -2 ]
        s_allergen = second_allergen.get_text()
	self.speak(s_allergen)

        #Find third allergen label
        lbl = soup.find_all("span", {"class":"allergy-outlook__content__graph__msg__label"})
        label = len(soup.find_all("span", {"class":"allergy-outlook__content__graph__msg__label"}))
        last_label = lbl[label -1 ]
        l_label = last_label.get_text()
	self.speak(l_label)

        #Find third allergen level
        tree_lvl = soup.find_all("div", {"class":"allergy-outlook__content__graph__msg__qual"})
        number_of_allergens = len(soup.find_all("div", {"class":"allergy-outlook__content__graph__msg__qual"}))
        last_allergen = tree_lvl[number_of_allergens -1 ]
        l_allergen = last_allergen.get_text()
	self.speak(l_allergen)



    def stop(self):
        pass


def create_skill():
    return PollenSkill()
