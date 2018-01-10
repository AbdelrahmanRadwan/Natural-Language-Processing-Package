# -*- coding: utf-8 -*-
# coding: utf-8
import json
from pprint import pprint

clubs_data = json.load(open('clubs.json'))

with open("clubs.txt", "w") as clubs_list:
    for club in clubs_data['entries']:
        clubs_list.write((club['value']+"\n").lower())


with open('clubs_with_synonyms.txt', 'w') as clubs_list:
    for club in clubs_data['entries']:
        string = club['value']+','
        for synonym in club['synonyms']:
            string+=(synonym+',')
        clubs_list.write((string+"\n").lower())


with open('clubs_with_synonyms_modefied.txt', 'w') as clubs_list:
    for club in clubs_data['entries']:
        string = club['value']+ ","+"".join(club['value'].split())+","
        for synonym in club['synonyms']:
            string+=(synonym+',')
            string+="".join(synonym.split())+','
        clubs_list.write((string+"\n").lower())

