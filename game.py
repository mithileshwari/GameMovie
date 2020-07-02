import random
import sys
import builtins
import subprocess
f = open("moviename.txt", "r")
cnt = 0


class inputmovie():
    def display(self, f):
        global cnt
        for x in f:
            cnt = cnt + 1

    def selectRandomMovie(self, f):
        global cnt
        f = open("moviename.txt", "r")
        all_lines = f.readlines()
        print(cnt)
        return all_lines[random.randint(0, cnt - 1)]


def printSpaces(movie):
    spaces = ""
    for x in movie:
        if (x == ' '):
            spaces += " "
            #print(" ", end=" ")
        else:
            spaces += "_"
            #print("_", end=" ")
    return spaces


def RunGame(attempt, movie, spaces , wrong , wrongchar, numspaces):
    if (attempt > 15):
        print("You lost the Game!")
        return 0
    CurrChar = ""
    if spaces == movie:
        print("You Won! Congrats ")
        print(movie)
        return 1
    stop_code = 'stop'
    try:
        CurrChar = input("enter a char:")
        print(CurrChar)
    except Exception as e:
        print(e)
    if CurrChar == movie:
        print("You Won! Congrats ")
        return 1
    if len(CurrChar) == 1:
        CurrChar = CurrChar[0]

    found = 0


    attempt = attempt + 1
    currspaces = 0
    for i in range(len(movie)):
        if CurrChar == movie[i]:
            print(CurrChar)
            numspaces = numspaces - 1
            spaces = spaces[:i] + CurrChar + spaces[i+1:]
            found = found + 1

    #if movie == spaces:
    if numspaces == 0:
        print("You Won! Congrats ")
        print(movie)
        return 1


    if(found == 0):
        wrong = wrong + 1
        wrongchar = wrongchar + " " + CurrChar

    print("%d wrong letters : %s" % (wrong, wrongchar))
    print("You are guessing : ", spaces)

    RunGame(attempt, movie, spaces, wrong, wrongchar, numspaces)






def main():
    c = inputmovie()
    c.display(f)
    movie = c.selectRandomMovie(f)
    print(movie)

    print(len(movie))
    movie.rstrip()
    movie.lstrip()
    spaces =  printSpaces(movie)
    print(len(spaces))
    spaces = spaces[0:len(spaces) -1]
    spaces.rstrip()
    spaces.lstrip()
    attempt = 0
    wrong = 0
    wrongchar = ""
    print("You are guessing", spaces)
    RunGame(attempt, movie, spaces, wrong, wrongchar, len(spaces))


if __name__ == "__main__":
    main()
