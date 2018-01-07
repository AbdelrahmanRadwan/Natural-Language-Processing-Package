import clubs_collector
from data_preprocessing import remove_endlines
from minimum_edit_distance import (
    suggestions,
    calculate_minimum_edit_distance)

#Writing the clubs names into the memory
with open('clubs.txt') as clubs_file:
    lines = clubs_file.readlines()
#cleaning the data
lines = remove_endlines(lines=lines)
#interactive mode activation...

while True:
    club_name_search = input("CLub name >> ")
    club_name_search.lower().rstrip()
    if club_name_search == "exit":
        break
    suggestions(lines, club_name_search)


