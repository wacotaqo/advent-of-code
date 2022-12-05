import os
import sys

filename = "adventofcode2022_day02_input.txt"

class Element:
    def __init__(self, letters):
        self.letters = letters # set of letters, e.g. ('A', 'B')
                
class Rock(Element):
    def __init__(self):
        self.__init__(('A', 'X'))
        
class Paper(Element):
    def __init__(self):
        self.__init__(('B', 'Y'))

class Scissors(Element):
    def __init__(self):
        self.__init__(('C', 'Z'))

class Player:
    def __init__(self, letters):
        self.letters = letters # set of letters, e.g. ('A', 'B')
        
class Opponent1(Player):
    def __init__(self):
        self.Player(('A', 'B', 'C'))

class Me(Player):
    def __init__(self):
        self.Player(('X', 'Y', 'Z'))

class PlayRPSRound:
    def __init__(self, 

def readfile(filename, path=os.getcwd()):
    fh = open(os.path.join(path, filename), "r")
    file_data = fh.read()
    fh.close()    
    return file_data

def read_RPS_file(filename):
    RPS_input = readfile(filename).splitlines()
    
    print (RPS_input)
    
read_RPS_file("adventofcode2022_day02_input.txt")

