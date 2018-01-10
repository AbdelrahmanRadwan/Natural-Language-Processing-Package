import operator
import math

def suggestions1(lines, search):
    clubs = {}
    search_club_name= search.split()[0]

    for club in lines:
        distance = calculate_minimum_edit_distance(club, search)
        for club_token in club.split():
            distance = min(distance, calculate_minimum_edit_distance(club_token, search_club_name))
        clubs[club] = distance

    clubs = sorted(clubs.items(), key=operator.itemgetter(1))

    for i in range(5):
        for j in range(i+1,5):
            if clubs[i][1] == clubs[j][1] and \
                            len(clubs[i][0]) >= len(clubs[j][0]):
                clubs[i], clubs[j] = clubs[j], clubs[i]

    for i in range(5):
        if clubs[i][1] == 0 and search == clubs[i][0]:
            print ("Perfect match! - %s" % (clubs[i][0]))
            return
    print('Suggestions1 >>', end='')
    for i in range(5):
        if clubs[i][1] < 3:
            print (clubs[i][0] + " (%s) - " %(clubs[i][1]), end= '' )
        elif i == 0 and clubs[i][1] <=5:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
            break
        elif i==0:
            print ("No such team!", end='')
        else:
            break
    print("")

def suggestions2(lines, search):
    clubs = {}
    search_tokens = search.split()
    for club_name in lines:
        club_name_tokens= club_name.split()
        distance = 0
        for i in range(0, min(len(search_tokens), len(club_name_tokens))):
            distance+=calculate_minimum_edit_distance(search_tokens[i], club_name_tokens[i])
        clubs[club_name] = distance

    clubs = sorted(clubs.items(), key=operator.itemgetter(1))

    for i in range(5):
        for j in range(i+1,5):
            if clubs[i][1] == clubs[j][1] and \
                            len(clubs[i][0]) >= len(clubs[j][0]):
                clubs[i], clubs[j] = clubs[j], clubs[i]

    for i in range(5):
        if clubs[i][1] == 0 and search == clubs[i][0]:
            print ("Perfect match! - %s" % (clubs[i][0]))
            return
    print('Suggestions2 >>', end='')
    for i in range(5):
        if clubs[i][1] < 3:
            print (clubs[i][0] + " (%s) - " %(clubs[i][1]), end= '' )
        elif i == 0 and clubs[i][1] <=5:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
            break
        elif i==0:
            print ("No such team!", end='')
        else:
            break
    print("")

def suggestions3(lines, search):
    clubs = {}
    search_tokens = search.split()
    for club in lines:
        distances = []
        club_tokens= club.split()
        for token1 in search_tokens:
            distance=10000
            for token2 in club_tokens:
                distance=min(distance, calculate_minimum_edit_distance(token1, token2))
            distances.append(distance)
        n = min(len(search_tokens), len(club_tokens))
        distances.sort()
        avg=abs(len(search_tokens) - len(club_tokens))
        for i in range(n):
            avg+=distances[i]
        avg/=n
        clubs[club]=avg

    clubs = sorted(clubs.items(), key=operator.itemgetter(1))

    for i in range(5):
        for j in range(i + 1, 5):
            if clubs[i][1] == clubs[j][1] and \
                            len(clubs[i][0]) >= len(clubs[j][0]):
                clubs[i], clubs[j] = clubs[j], clubs[i]

    for i in range(5):
        if clubs[i][1] == 0 and search == clubs[i][0]:
            print("Perfect match! - %s" % (clubs[i][0]))
            return
    print('Suggestions3 >>', end='')
    for i in range(5):
        if clubs[i][1] < 3:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
        elif i == 0 and clubs[i][1] <=5:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
            break
        elif i == 0:
            print("No such team!", end='')
        else:
            break
    print("")

def suggestions4(lines, search):
    clubs = {}
    search_tokens = search.split()
    for club in lines:
        distances = []
        club_tokens= club.split()
        for token1 in search_tokens:
            distance=10000
            for token2 in club_tokens:
                distance=min(distance, calculate_minimum_edit_distance(token1, token2))
            distances.append(distance)
        n = min(len(search_tokens), len(club_tokens))
        distances.sort()
        avg=0
        for i in range(n):
            avg+=distances[i]
        avg/=n
        clubs[club]=avg

    clubs = sorted(clubs.items(), key=operator.itemgetter(1))

    for i in range(5):
        for j in range(i + 1, 5):
            if clubs[i][1] == clubs[j][1] and \
                            len(clubs[i][0]) >= len(clubs[j][0]):
                clubs[i], clubs[j] = clubs[j], clubs[i]

    for i in range(5):
        if clubs[i][1] == 0 and search == clubs[i][0]:
            print("Perfect match! - %s" % (clubs[i][0]))
            return
    print('Suggestions4 >>', end='')
    for i in range(5):
        if clubs[i][1] < 3:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
        elif i == 0 and clubs[i][1] <=5:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
            break
        elif i == 0:
            print("No such team!", end='')
            break
        else:
            break
    print("")

def suggestions5(lines_synonyms, search):
    clubs = {}
    search_tokens = search.split()

    for line in lines_synonyms:
        club_synonyms = line.split(',')
        for club in club_synonyms:
            distances = []
            club_tokens = club.split()
            if not club_tokens:
                continue
            for token1 in search_tokens:
                distance = 10000
                for token2 in club_tokens:
                    distance = min(distance, calculate_minimum_edit_distance(token1, token2))
                distances.append(distance)
            n = min(len(search_tokens), len(club_tokens))
            distances.sort()
            avg=0
            for i in range(n):
                avg+=distances[i]
            avg/=n
            if club_synonyms[0] in clubs:
                clubs[club_synonyms[0]]=min(avg, clubs[club_synonyms[0]])
            else:
                clubs[club_synonyms[0]] = avg
    clubs = sorted(clubs.items(), key=operator.itemgetter(1))

    for i in range(5):
        for j in range(i + 1, 5):
            if clubs[i][1] == clubs[j][1] and \
                            len(clubs[i][0]) >= len(clubs[j][0]):
                clubs[i], clubs[j] = clubs[j], clubs[i]

    for i in range(5):
        if clubs[i][1] == 0 and search == clubs[i][0]:
            print("Perfect match! - %s" % (clubs[i][0]))
            return
    print('Suggestions5 >>', end='')
    for i in range(5):
        if clubs[i][1] < 3:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
        elif i == 0 and clubs[i][1] <=5:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
            break
        elif i == 0:
            print("No such team!", end='')
            break
        else:
            break
    print("")

def suggestions6(lines_synonyms, search):
    clubs = {}
    search_tokens = search.split()

    for line in lines_synonyms:
        club_synonyms = line.split(',')
        for club in club_synonyms:
            distances = []
            club_tokens = club.split()
            if not club_tokens:
                continue
            for token1 in search_tokens:
                distance = 10000
                for token2 in club_tokens:
                    distance = min(distance, calculate_minimum_edit_distance(token1, token2))
                distances.append(distance)
            n = min(len(search_tokens), len(club_tokens))
            distances.sort()
            avg=0
            for i in range(n):
                avg+=distances[i]
            avg/=n
            if club_synonyms[0] in clubs:
                clubs[club_synonyms[0]]=min(avg, clubs[club_synonyms[0]])
            else:
                clubs[club_synonyms[0]] = avg
    clubs = sorted(clubs.items(), key=operator.itemgetter(1))

    for i in range(5):
        for j in range(i + 1, 5):
            if clubs[i][1] == clubs[j][1] and \
                            len(clubs[i][0]) >= len(clubs[j][0]):
                clubs[i], clubs[j] = clubs[j], clubs[i]

    for i in range(5):
        if clubs[i][1] == 0 and search == clubs[i][0]:
            print("Perfect match! - %s" % (clubs[i][0]))
            return
    print('Suggestions6 >>', end='')
    for i in range(5):
        if clubs[i][1] < 3:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
        elif i == 0 and clubs[i][1] <=5:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
            break
        elif i == 0:
            print("No such team!", end='')
            break
        else:
            break
    print("")

def suggestions7(lines_synonyms, search):
    clubs = {}
    search_tokens = search.split()

    for line in lines_synonyms:
        club_synonyms = line.split(',')
        for club in club_synonyms:
            distances = []
            club_tokens = club.split()
            if not club_tokens:
                continue
            for token1 in search_tokens:
                distance = 10000
                for token2 in club_tokens:
                    distance = min(distance, calculate_minimum_edit_distance(token1, token2))
                distances.append(distance)
            n = min(len(search_tokens), len(club_tokens))
            distances.sort()
            avg = abs(len(search_tokens) - len(club_tokens))
            for i in range(n):
                avg+=distances[i]

            avg/=n
            if club_synonyms[0] in clubs:
                clubs[club_synonyms[0]]=min(avg, clubs[club_synonyms[0]])
            else:
                clubs[club_synonyms[0]] = avg
    clubs = sorted(clubs.items(), key=operator.itemgetter(1))

    for i in range(5):
        for j in range(i + 1, 5):
            if clubs[i][1] == clubs[j][1] and \
                            len(clubs[i][0]) >= len(clubs[j][0]):
                clubs[i], clubs[j] = clubs[j], clubs[i]

    for i in range(5):
        if clubs[i][1] == 0 and search == clubs[i][0]:
            print("Perfect match! - %s" % (clubs[i][0]))
            return
    print('Suggestions7 >>', end='')
    for i in range(5):
        if clubs[i][1] < 3:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
        elif i == 0 and clubs[i][1] <=5:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
            break
        elif i == 0:
            print("No such team!", end='')
            break
        else:
            break
    print("")

def suggestions8(lines_synonyms, search):
    clubs = {}
    search_tokens = search.split()

    for line in lines_synonyms:
        club_synonyms = line.split(',')
        for club in club_synonyms:
            distances = []
            club_tokens = club.split()
            if not club_tokens:
                continue
            for token1 in search_tokens:
                distance = 10000
                for token2 in club_tokens:
                    distance = min(distance, calculate_minimum_edit_distance(token1, token2))
                distances.append(distance)
            n = min(len(search_tokens), len(club_tokens))
            distances.sort()
            avg = abs(len(search_tokens) - len(club_tokens))
            for i in range(n):
                avg+=distances[i]

            avg/=n
            if club_synonyms[0] in clubs:
                clubs[club_synonyms[0]]=min(avg, clubs[club_synonyms[0]])
            else:
                clubs[club_synonyms[0]] = avg
    clubs = sorted(clubs.items(), key=operator.itemgetter(1))

    for i in range(5):
        for j in range(i + 1, 5):
            if clubs[i][1] == clubs[j][1] and \
                            len(clubs[i][0]) >= len(clubs[j][0]):
                clubs[i], clubs[j] = clubs[j], clubs[i]

    for i in range(5):
        if clubs[i][1] == 0 and search == clubs[i][0]:
            print("Perfect match! - %s" % (clubs[i][0]))
            return
    print('Suggestions8 >>', end='')
    for i in range(5):
        if clubs[i][1] < 3:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
        elif i == 0 and clubs[i][1] <=5:
            print(clubs[i][0] + " (%s) - " % (clubs[i][1]), end='')
            break
        elif i == 0:
            print("No such team!", end='')
            break
        else:
            break
    print("")


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
                d = 1
            table[i][j] = min(table[i-1][j-1] + d,
                              table[i-1][j]+1,
                              table[i][j-1]+1)

    return table[len2][len1]




