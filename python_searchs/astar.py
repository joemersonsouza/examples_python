# a*s.py
# ---------
# Developed by Joemerson Souza
# This implementation was possible thanks to Berkley and Coursera
# The basic structure was primarily implemented by John DeNero (denero@cs.berkeley.edu) 
# and Dan Klein (klein@cs.berkeley.edu)

import heapq
import random
import string

DIVISOR = "-"

"""
    Implements a heap with cost. On UCS we need to use a queue with cost 
    because when we need to find an item we use it to get a better solution.
    In this implementation, is not possible to change a cost of an item
    but you can put the same object with other cost
"""
class UcsQueue:

    def  __init__(self):
        self.heap = []

    def push(self, item, priority):
        pair = (priority,item)
        heapq.heappush(self.heap,pair)

    def pop(self):
        (priority,item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0
    
    def length(self):
        return len(self.heap)

    def getItem(self):
        (item, cost) = heapq.heappop(self.heap)
        return item

"""
    Implements methods responsable to control and help ucs structure
    to find a solution using UcsQueue focusing on cost
"""
class SearchProblem:
    """
        Constructor
    """
    def __init__(self, fullState, goal, start):
        self.startState = start
        self.goal = goal
        self.fullState = fullState
        self.totalCost = 0

    """
        Manhattan method is responsable to calculate the absolute value
        between current position to goal
    """
    def getManhattanValue(self, position):
        xy1 = position
        xy2 = problem.goal
        return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

    """
        Manhattan method is responsable to calculate the heuristic value
        between current position to goal using the Euclidean formule
    """
    def getEuclideanValue(self, position):
        xy1 = position
        xy2 = problem.goal
        return ( (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2 ) ** 0.5

    """
        Method responsable to return where the problem is starting
    """
    def getStartState(self):
        return self.startState

    """
        Method responsable to check if it's found a solution
    """
    def isGoalState(self,state):
        return state == self.goal

    def getListCitiesWithoutPosition(self, state):
        if(state == None):
            return [list(row[0] for row in self.fullState)]
        else:
            return [list(row[0] for row in state)]

    """
        Method responsable to return the possibles state that we can 
        find a solution
    """
    def getSuccessors(self, state):
        successorList = []
        for edge in self.getListCitiesWithoutPosition(None):
            """ Getting all states when initial state is equal to start state """
            print self.getListCitiesWithoutPosition(edge[0])
            if self.getListCitiesWithoutPosition(edge[0])==state:
                successorList.append((edge[1],edge[0]+DIVISOR+edge[1]+DIVISOR+str(edge[2]),edge[2]))
            """ Getting all states when final state is equal to goal """
            if self.getListCitiesWithoutPosition(edge[1])==state:
                successorList.append((edge[0],edge[0]+DIVISOR+edge[1]+DIVISOR+str(edge[2]),edge[2]))
        print successorList
        return successorList

    """
        Method responsable to return the cost of the possible state
        It's get the actions found and find the cost of all
    """
    def getCostOfActions(self,actions):
        cost=0
        for action in actions:
            listCities = string.split(action, DIVISOR)
            for edge in self.fullState:
                if edge[0]==listCities[0] and edge[1]==listCities[1]:
                    cost+=edge[2]
                if edge[1]==listCities[0] and edge[0]==listCities[1]:
                    cost+=edge[2]
        return cost
    
    """
        This method split the solution and sum the cos of all
    """
    def setTotalCost(self, state):
        for city in state:
            data = city.split(DIVISOR)
            self.totalCost += int(data[2])

    """
        Method responsable to run the problem using Uniformed Search Cost
        print the result with the cost of it
    """
    def runTest(self):
        ucsResult = aStarSearch(self)
        print ucsResult
        if(len(ucsResult) > 0):
            print "Total Km is "+str(self.totalCost)

    """
        Uniformed Search Cost Method
        This method use a heap with priority
    """
def aStarSearch(problem):
    fringe = UcsQueue()
    fringe.push( (problem.getStartState(), []), 0)
    explored = []
    
    while not fringe.isEmpty():
        node, actions = fringe.pop()
        
        if problem.isGoalState(node):
            problem.setTotalCost(actions)
            return actions
        
        explored.append(node)
        
        for coord, direction, steps in problem.getSuccessors(node):
            print coord
            if not coord in explored:
                new_actions = actions + [direction]
                fringe.push((coord, new_actions), problem.getCostOfActions(new_actions))

    return []

"""
    Method that return a mocked list of cities
"""
def getCities():
    return [("New York",1,2),("Orleans",3,6),("Chicago",2,2),("New Jersey",1,3),("Okland",3,3),("New England",1,7),("Minessota",2,5),("Pittsburg",2,1),("San Francisco",3,1),("San Andreas",3,2),("Washington",1,1)]

"""
    Method that to return a randomic city
"""
def getRandomCity():
    return random.choice(getCities())

"""
    Method responsable to return a list of tuple
    this tuple has two city and the cost of it
    The first city is the start point
    The second city is the end point
    The distance is the cost of this tuple
"""
def createRandomList(level, listOfCities):
    for i in range(0,level):
        firstCity = getRandomCity()
        secondCity = getRandomCity()
        distance = random.randint(1,10000)
        value = (firstCity, secondCity,distance)
        listOfCities.append(value)
    
"""
    Method responsable to show the mocked cities
"""
def showCities():
    for city, posx, posy in getCities():
        print city

"""
    Method responsable to valid if the setted city is valid
"""
def validCity(city):
    return filter(lambda value : value[0] == city, getCities())
"""
    Method responsable to get any valid city
    The situation is used to show if the point is to start or finish
"""
def getPoint(situation):
    message = "Set city " + situation
    value = ""
    print message
    while True:
        value = raw_input()
        if(validCity(value)):
            break
        showCities()
        print message

    return value

"""
    Method responsable to show the possible cities to choice
"""
def showList(listOfCities):
    for item in listOfCities:
        print item

def main():
    level = 20
    listOfCities = []
    createRandomList(level,listOfCities)
    showCities()
    showList(listOfCities)
    startState = getPoint("from:")
    endState = getPoint("to:")
    problem = SearchProblem(listOfCities, startState, endState)
    problem.runTest()

if __name__ == '__main__':
    main()
