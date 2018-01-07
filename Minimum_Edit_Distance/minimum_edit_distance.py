import operator


def suggestions(lines, search_club_name):
    clubs = {}
    for club in lines:
        distance = calculate_minimum_edit_distance(club, search_club_name)
        clubs[club] = distance

    clubs = sorted(clubs.items(), key=operator.itemgetter(1))

    if clubs[0][1] == 0:
        print ("Perfect match! - %s" % (clubs[0][0]))
    #elif clubs[0][1] >= len(search_club_name) - 2:
     #   print ("Is this a club name!")
    else:
        print("Suggestions >> \'%s\' \'%s\' \'%s\'" %(clubs[0][0],
                                          clubs[1][0],
                                          clubs[2][0]))



def calculate_minimum_edit_distance (s1,s2):
    "Calculate Levenstein edit distance for strings s1 and s2."
    len1 = len (s1) # vertically
    len2 = len (s2) # horizontally
    # Allocate the table
    table = [None]*(len2+1)
    for i in range(len2+1):
        table[i] = [0]*(len1+1)
    # Initialize the table
    for i in range(1, len2+1):
        table[i][0] = i
    for i in range(1, len1+1):
        table[0][i] = i
    # Do dynamic programming
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if s1[j-1] == s2[i-1]:
                d = 0
            else:
                d = 4
            table[i][j] = min(table[i-1][j-1] + d,
                              table[i-1][j]+2,
                              table[i][j-1]+1)

    return table[len2][len1]

