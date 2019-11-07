import Constraint as cst
import collections
import numpy as np
import copy


class State:

    def __init__(self, assignment=None, variable=None, value=None):
        if assignment == None:
            self.assignment = self.getInitialState()
        else:
            currentValue = copy.deepcopy(assignment)
            currentValue[variable] = value
            self.assignment = currentValue

    def getInitialState(self):
        return collections.OrderedDict()

    def selectUnassignedVariable(self):
        for variable in cst.variables:
            if variable not in self.assignment:
                return variable

    def selectHeuristicUnassignedVariable(self):
        
        remainingValues = {}

        for variable in cst.variables:
            if variable not in self.assignment:
                remainingValues[variable] = self.findPossibleValuesCount(variable)
        
        min_val = min(remainingValues.values())
        minVariables = [k for k, v in remainingValues.items() if v == min_val]
        print("remainingValues ", remainingValues)
        print("minVariables ", minVariables)

        if len(minVariables) > 0:
            constraintCounts = {}

            for variable in minVariables:
                constraintCounts[variable] = self.findConstraintsCount(variable)

            max_val = max(constraintCounts.values())
            maxConstraintsVariables = [k for k, v in constraintCounts.items() if v == max_val]
            print("constraintCounts ", constraintCounts)
            print("maxValue ", max_val)
            print("maxConstraintsVariables ", maxConstraintsVariables)

            return maxConstraintsVariables[0]

        return minVariables[0]

    def getOrderDomainValues(self):
        return cst.domainValues

    def getHeuristicOrderDomainValues(self, variable):
        
        neighbourValuesCounts = []

        for value in cst.domainValues:
            if cst.checkConstraints(self.assignment, variable, value):
                neighbourValuesCount = 0

                childState = State(self.assignment, variable, value)

                for neighbour in cst.constraints[variable]:
                    if neighbour not in self.assignment:
                        for domain in cst.domainValues:
                            if cst.checkConstraints(childState.assignment, neighbour, domain):
                                neighbourValuesCount += 1

                neighbourValuesCounts.append(-neighbourValuesCount)
            else:
                neighbourValuesCounts.append(0)

        sortedCounts = sorted(zip(neighbourValuesCounts, cst.domainValues))
        print("sortedCounts ", sortedCounts)
        
        return  [x for (_,x) in sortedCounts]

    def checkGoalState(self):
        return len(self.assignment) == len(cst.variables)

    def drawState(self):
        image = np.zeros((7, 7, 3), np.uint8)
        for key in self.assignment:
            if self.assignment[key] == "red":
                channeIndex = 0
            elif self.assignment[key] == "green":
                channeIndex = 1
            else:
                channeIndex = 2

            for(xcoord, ycoord) in cst.positions[key]:
                image[xcoord, ycoord, channeIndex] = 255

        return image

    def findPossibleValuesCount(self, variable):
        count = 0
        for value in cst.domainValues:
            if(cst.checkConstraints(self.assignment, variable, value)):
                count +=1

        return count

    def findConstraintsCount(self, variable):
        count = 0

        for neighbor in cst.constraints[variable]:
            if neighbor not in self.assignment:
                count +=1
        
        return count
