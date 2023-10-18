
import requests #allows attachment of internet file
constitution = requests.get('https://www.usconstitution.net/const.txt') #attaches consititution text to program
string = constitution.text 
stringlist = string.split('\n') #splits constitution text into lines, creating a list
search = input('Enter Search Term: ') #prompts for search term
s = 0
e = 1
while search != '': #while input for search term is not blank
    for i in range(len(stringlist)): #defines range according to number lines in the list
        if stringlist[i].find(search) != -1: #if the search term is found in a line
            for c in range (i, 0, -1): #program moves backwards from location of search term to the first line
                if stringlist[c] == '': #locates nearest previous blank line
                    s = c #sets starting point to this blank line
                    break
            for c in range (i, len(string), +1): #program moves forward from location of search term to the last line
                if stringlist[c] == '': #locates nearest following blank line
                    e = c +1 #sets the ending point to c+1 to include the blank line 
                    break
            for c in range (s, e):
                print("Line ", c, ":", stringlist[c])
            print()
            i = e #ending point is now the starting point for the program to find the next search term occurence
    search = input('Enter Search Term: ') 