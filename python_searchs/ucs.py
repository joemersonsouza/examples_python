# ucs.py
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
        Method responsable to return where the problem is starting
    """
    def getStartState(self):
        return self.startState

    """
        Method responsable to check if it's found a solution
    """
    def isGoalState(self,state):
        return state == self.goal

    """
        Method responsable to return the possibles state that we can 
        find a solution
    """
    def getSuccessors(self, state):
        successorList = []
        for edge in self.fullState:
            """ Getting all states when initial state is equal to start state """
            if edge[0]==state:
                successorList.append((edge[1],edge[0]+DIVISOR+edge[1]+DIVISOR+str(edge[2]),edge[2]))
            """ Getting all states when final state is equal to goal """
            if edge[1]==state:
                successorList.append((edge[0],edge[0]+DIVISOR+edge[1]+DIVISOR+str(edge[2]),edge[2]))
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
        ucsResult = uniformCostSearch(self)
        print ucsResult
        if(len(ucsResult) > 0):
            print "Total Km is "+str(self.totalCost)

    """
        Uniformed Search Cost Method
        This method use a heap with priority
    """
def uniformCostSearch(problem):
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
            if not coord in explored:
                new_actions = actions + [direction]
                fringe.push((coord, new_actions), problem.getCostOfActions(new_actions))

    return []

"""
    Method that return a mocked list of cities
"""
def getCities():
    return ["New York","Orleans","Chicago","New Jersey","Okland","New England","Minessota","Pittsburg","San Francisco","San Andreas","Washington"]

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
    for city in getCities():
        print city

"""
    Method responsable to valid if the setted city is valid
"""
def validCity(city):
    return city in getCities()

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
