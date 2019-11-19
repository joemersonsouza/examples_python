import numpy as np
import Config
from Move import Move

class State:

    def __init__(self, boardValues = None):
        if boardValues is None:
            self.boardValues = self.getInitialState()
        else:
            self.boardValues = boardValues

    def getInitialState(self):
        initialState = -1 * np.ones((Config.nSquares, Config.nSquares), np.int8)
        return initialState

    def checkGoalState(self):
        winner = -1
        endFlag = False

        squareCoordinates = [
            [0,0,0,1,0,2],
            [1,0,1,1,1,2],
            [2,0,2,1,2,2],
            [0,0,1,0,2,0],
            [0,1,1,1,2,1],
            [0,2,1,2,2,2],
            [0,0,1,1,2,2],
            [0,2,1,1,2,0]]

        for lineIndex in range(len(squareCoordinates)):
            row1 = squareCoordinates[lineIndex][0]
            col1 = squareCoordinates[lineIndex][1]
            row2 = squareCoordinates[lineIndex][2]
            col2 = squareCoordinates[lineIndex][3]
            row3 = squareCoordinates[lineIndex][4]
            col3 = squareCoordinates[lineIndex][5]
            firstSquareValue = self.boardValues[row1, col1]
            secondSquareValue = self.boardValues[row2, col2]
            thirdSquareValue = self.boardValues[row3, col3]

            if(firstSquareValue != -1 and firstSquareValue == secondSquareValue) and \
                secondSquareValue == thirdSquareValue:
                if(firstSquareValue == Config.computerPlayer):
                    endFlag = True
                    winner = Config.computerPlayer
                    return endFlag, winner
                if (firstSquareValue == Config.humanPlayer):
                    endFlag = True
                    winner = Config.humanPlayer
                    return endFlag, winner

        for i in range(Config.nSquares):
            for j in range(Config.nSquares):
                if self.boardValues[i, j] == -1:
                    return endFlag, winner

        winner = Config.drawValue
        endFlag = True
        return endFlag, winner

    def checkSameState(self, firstBoard, secondBoard):
        sameCount = np.sum(firstBoard == secondBoard)

        return sameCount == (Config.nSquares * Config.nSquares)

    def checkSymetry(self, firstBoard, secondBoard):
        rootBoardValues = np.copy(firstBoard)

        for _ in range(3):
            rootBoardValues = np.rot90(rootBoardValues)
            if self.checkSameState(rootBoardValues, secondBoard):
                return True
        
        flipBoardValues = np.copy(firstBoard)
        flipBoardValues = np.fliplr(flipBoardValues)

        if self.checkSameState(flipBoardValues, secondBoard):
            return True

        flipBoardValues = np.copy(firstBoard)
        flipBoardValues = np.flipud(flipBoardValues)

        if self.checkSameState(flipBoardValues, secondBoard):
            return True

        mirrorBoardValues = np.copy(firstBoard)
        mirrorBoardValues = np.rot90(mirrorBoardValues)
        mirrorBoardValues = np.rot90(mirrorBoardValues)
        mirrorBoardValues = np.swapaxes(mirrorBoardValues, 0, 1)

        if self.checkSameState(flipBoardValues, secondBoard):
            return True

        return False

    def createChildState(self, move):
        boardValues = np.copy(self.boardValues)
        boardValues[move.row][move.col] = move.playerValue
        newChildState = State(boardValues)
        return newChildState
    
    def successorFunction(self, playerValue):

        endFlag, _ = self.checkGoalState()

        if endFlag:
            return [], []

        childStates = []
        moves = []

        for row in range(Config.nSquares):
            for col in range(Config.nSquares):

                if self.boardValues[row, col] == -1:
                    move = Move(row, col, playerValue)
                    newChildState = self.createChildState(move)

                    symmetricFlag = False
                    for childState in childStates:
                        if self.checkSymetry(newChildState.boardValues, childState.boardValues):
                            symmetricFlag = True
                    
                    if not symmetricFlag:
                        childStates.append(newChildState)
                        moves.append(move)
        
        return childStates, moves

    def evaluateState(self):

        endFlag, winner = self.checkGoalState()
        if endFlag:
            if winner == Config.computerPlayer:
                return 1000
            elif winner == Config.humanPlayer:
                return -1000
            else:
                return 0

        score = 0

        squareCoordinates = [
            [0,0,0,1,0,2],
            [1,0,1,1,1,2],
            [2,0,2,1,2,2],
            [0,0,1,0,2,0],
            [0,1,1,1,2,1],
            [0,2,1,2,2,2],
            [0,0,1,1,2,2],
            [0,2,1,1,2,0]]

        scores = [0,
                    1,
                    10,
                    100]

        for lineIndex in range(len(squareCoordinates)):
            pointsOnLine = 0
            opponentPointsOnLine = 0

            for pointIndex in range(Config.nSquares):
                row = squareCoordinates[lineIndex][2*pointIndex]
                col = squareCoordinates[lineIndex][2 * pointIndex + 1]

                if self.boardValues[row, col] == Config.humanPlayer:
                    opponentPointsOnLine += 1
                if self.boardValues[row, col] == Config.computerPlayer:
                    pointsOnLine += 1

            score += scores[pointsOnLine] - scores[opponentPointsOnLine]
        
        return score
