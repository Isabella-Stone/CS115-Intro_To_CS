'''
Isabella Stone
I pledge my honor that I have abided by the Stevens Honor System.
'''

PREF_FILE = 'musicrecplus.txt'

def loadUsers(fileName):
    '''Reads in a file of stored
    users' preferences stored
    in the file 'fileName'. It returns a dictionary containing a
    mapping of user names to a list of preffered artists.'''
    file = open(fileName, 'r')
    userDict = {}
    for line in file:
        # read and parse a single line
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict

###########################################################
# to help give recomendations

def findBestUser(currUser, prefs, userMap):
    '''returns the index of the stored user with the most matches to
    the current user, assuming userPrefs and allPrefs are lists'''
    bestUser = None
    bestScore = -1
    for user in userMap.keys():
        
        score = numMatches(prefs, userMap[user])
        #print('score', score)

        
        #if the list is the exact same dont use it
        if userMap[currUser]==userMap[user]:
            #print('1')
            pass
        
        #if user is private dont use them
        elif user[-1]=='$':
            #print('2')
            pass
        
        #if list is a sublist dont use it
        elif (len(userMap[user]) < len(userMap[currUser])) and score==len(userMap[user]):
            #print('3')
            #print(len(userMap[user]))
            pass
        else:
            if score > bestScore and currUser != user:
                #print('4', score)
                bestScore = score
                bestUser = user
        '''
        else: #if only one user in usermap
            bestUser = currUser
        '''
        
    #if didnt find a match
    #bestUser = currUser
    #print(bestUser)
    return bestUser

    '''
        else:
            if score > bestScore and currUser != user:
                print('4', score)
                bestScore = score
                bestUser = user
        '''

def drop(list1, list2):
    '''returns a new list that contains only the elements in list2 that
    were not in list1.'''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    #add the rest of the list2 if theres anything left
    while j < len(list2):
        list3.append(list2[j])
        j += 1

    return list3

def numMatches(list1, list2):
    '''returns the number of elements that match between 2 sorted lists'''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

###########################################################

def saveUserPreferences(userName, prefs, userMap, fileName):
    '''Writes all of the user preferences to the file. Returns nothing.'''
    userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + "\n"
        file.write(toSave)
    file.close()
    
################################################################################################################
    
######################################################################
#                        menu options:                               #
######################################################################
# e #
# enter preferences

def getPreferencesInitial(userName, userMap): #original prefs for new users
    '''asks userName for their preferences and saves them into the
    dictionary userMap'''
    newPref = ''
    if userName in userMap:
        prefs = userMap[userName]
    else:
        prefs = []
        
        newPref = input("Enter an artist that you like (Enter to finish):\n")
        while newPref != '':
            if newPref.strip().title() in prefs: #dont put repeats
                #print('1')
                newPref = input('Enter an artist that you like (Enter to finish):\n')
            else:
                #print('2')
                prefs.append(newPref.strip().title())
                newPref = input('Enter an artist that you like (Enter to finish):\n')
        #keep lists sorted for ease
        #comparison
        prefs.sort()

    #save new preferences to Dict
    userMap[userName] = prefs
    
    return prefs

def getPreferencesE(userName, userMap): #for menu (e)
    '''replaces old preferences for userName in userMap, assuming
    userMap is a dictionary and userName is one of its keys'''
    
    #clear artists user already has
    userMap[userName] = []
    #print(userMap)

    prefs = []

    #fills prefs w new artists
    newPref = input("Enter an artist that you like (Enter to finish):\n")
    while newPref != '':
            if newPref.strip().title() in prefs: #dont put repeats
                #print('1')
                newPref = input('Enter an artist that you like (Enter to finish):\n')
            else: #if not a repeat add to prefs
                #print('2')
                prefs.append(newPref.strip().title())
                newPref = input('Enter an artist that you like (Enter to finish):\n')
                
    #keep lists sorted for ease
    #comparison
    prefs.sort()
        
    #save new preferences to Dict
    #userMap[userName] = prefs
    #print(userMap)
    
    return prefs


######################################################################
# r #
# get recomendations
def getRecommendations(currUser, prefs, userMap):
    '''Gets recommendations for a user (currUser) based on the users
    in UserMap (a dictionary) and the user's prefs in a pref (list).
    Returns a list of recommended artists.'''
    bestUser = findBestUser(currUser, prefs, userMap)
    if bestUser!=None:
        recommendations = drop(prefs, userMap[bestUser])
    else:
        recommendations = []
    
    #print(recommendations)
    #print(prefs)
    
    recommendations.sort()
    
    if recommendations == [] or numMatches(userMap[bestUser], prefs)==0:
        print("No recommendations available at this time.")
    else:
        for rec in recommendations:
            print(rec)
    

######################################################################
# p #
# show most popular artists

def getArtistDict(userMap):
    '''creates a new dictionary of artists and how many times they appear
    in userMap, assuming userMap is a dictionary'''
    newDict = {}
    #fill newDict w all artists and how many times they appear in userMap
    for user in userMap:
        for artist in userMap[user]:
            if user[-1]=='$': #don't include private users
                pass
            elif artist in newDict: #add 1 to artist's count
                newDict[artist] += 1
            else: #add artist to newDict if it's not already in it
                newDict[artist] = 1
    return newDict

def getMostPopArtists(userMap):
    '''finds the artist that appears the most in userMap,
    assuming userMap is a dictionary'''
    newDict = getArtistDict(userMap)
    #pick top 3 artists in newDict which already doesnt include private users
    if newDict != {}:
        #sortedDictList = sorted(newDict.items(), key = lambda x:(x[1], x[0]))
        sortedDictList = []
        for key in newDict:
            sortedDictList += [(newDict[key], key)]
        sortedDictList.sort()
        ##print(sortedDictList) ##
        print(sortedDictList[-1][1])
        if len(sortedDictList)>1:
            print(sortedDictList[len(sortedDictList)-2][1])
        if len(sortedDictList)>2:
            print(sortedDictList[len(sortedDictList)-3][1])
    else: #if newDict is empty / no artists can be found
        print("Sorry, no artists found.")

######################################################################
# h #
# how popular is the most popular

def howPopular(userMap):
    '''finds how many times the most popular artists appears in userMap,
    assuming userMap is a dictionary'''
    newDict = getArtistDict(userMap)
    #pick value at last/highest artist
    if newDict != {}:
        sortedDictList = []
        for key in newDict:
            sortedDictList += [(newDict[key], key)]
        sortedDictList.sort()
        return sortedDictList[-1][0]
    else: #if newDict is empty / no artists can be found
        print("Sorry, no artists found.")

######################################################################
# m #
# which user has the most likes (which user has most preferences)

def mostLikes(userMap):
    '''finds which user in userMap has the most artists entered,
    assuming userMap is a dictionary'''
    newDict = {}
    #fill newDict w all users and how many artists they have
    for user in userMap:
        if user[-1]=='$': #don't include private users
                pass
        else:
            newDict[user] = len(userMap[user])
    #get the name of the last user in the dict
    if newDict != {}:
        sortedDictList = []
        for key in newDict:
            sortedDictList += [(newDict[key], key)]
        sortedDictList.sort()
        return sortedDictList[-1][1]
    else: #if newDict is empty / no users can be found
        print("Sorry, no user found.")
    
######################################################################
# q #
# save and quit

# use --> saveUserPreferences(userName, prefs, userMap, PREF_FILE)

################################################################################################################


def main():
    '''main functions of program to run'''

    #userMap = loadUsers(PREF_FILE)
    try:
        userMap = loadUsers(PREF_FILE)
    except:
        file = open(PREF_FILE,'w')
        file.close()
        userMap = {}
    
    # 1.have user enter name:
    userName = input('Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n')

    # 2.if user not in file, enter as many artists as they like and save them
    
    prefs = getPreferencesInitial(userName, userMap) 
    #recs = getRecommendations(userName, prefs, userMap)
    
    # 3.give the menu and have the options work from there:
    while True:
        menuAnswer = input('Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit\n')
        if menuAnswer not in ['e','r','p','h','m','q']:
            pass
        elif menuAnswer=='q':
            saveUserPreferences(userName, prefs, userMap, PREF_FILE)
            break
        else: # perform function corresponding to letter user inputs
            if menuAnswer == 'e':
                prefs = getPreferencesE(userName, userMap)
                userMap[userName] = prefs
            elif menuAnswer == 'r':
                getRecommendations(userName, prefs, userMap)
            elif menuAnswer == 'p':
                getMostPopArtists(userMap)
            elif menuAnswer == 'h':
                print(howPopular(userMap))
            elif menuAnswer == 'm':
                print(mostLikes(userMap))
            
    
    saveUserPreferences(userName, prefs, userMap, PREF_FILE)

if __name__=='__main__':main()












            
