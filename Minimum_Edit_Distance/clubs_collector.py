# -*- coding: utf-8 -*-
# coding: utf-8
import json
from pprint import pprint

clubs_data = json.load(open('clubs.json'))

with open("clubs.txt", "a") as clubs_list:
    for club in clubs_data['entries']:
        clubs_list.write((club['value']+"\n").lower())


