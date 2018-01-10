import clubs_collector
from data_preprocessing import remove_endlines
from minimum_edit_distance import (suggestions1,
                                   suggestions2,
                                   suggestions3, suggestions4, suggestions5, suggestions6, suggestions7, suggestions8)

#Writing the clubs names into the memory
with open('clubs.txt', 'r') as clubs_file:
    lines = clubs_file.readlines()
with open('clubs_with_synonyms.txt', 'r') as clubs_file:
    lines_synonyms = clubs_file.readlines()
with open('clubs_with_synonyms_modefied.txt', 'r') as clubs_file:
    lines_synonyms_modefied = clubs_file.readlines()

#cleaning the data
lines = remove_endlines(lines=lines)
#interactive mode activation...
print("Suggestion1 => main-word try match\n"
      "Suggestion2 => Coressponding-words try match\n"
      "Suggestion3 => Complete-Graph Word Count Penalty\n"
      "Suggestion4 => Complete-Graph Word no Count Penalty\n"
      "Suggestion5 => Complete-Graph Word no Count Penalty - using synonyms\n"
      "Suggestion6 => Complete-Graph Word no Count Penalty - using modefied synonyms\n"
      "Suggestion7 => Complete-Graph Word Count Penalty - using synonyms\n"
      "Suggestion8 => Complete-Graph Word Count Penalty - using modefied synonyms")

while True:
    club_name_search = input("CLub name >> ")
    club_name_search = club_name_search.lower().rstrip()
    search=''
    for i in range(len(club_name_search)):
        if i+2< len(club_name_search) and club_name_search[i]==club_name_search[i+1] and club_name_search[i+1]==club_name_search[i+2]:
            continue
        else:
            search+=club_name_search[i]

    if club_name_search == "exit" or not club_name_search:
        break

    suggestions1(lines, search)
    suggestions2(lines, search)
    suggestions3(lines, search)
    suggestions4(lines, search)
    suggestions5(lines_synonyms, search)
    suggestions6(lines_synonyms_modefied, search)
    suggestions7(lines_synonyms, search)
    suggestions8(lines_synonyms_modefied, search)

    print("="*190)


