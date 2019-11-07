from Node import Node
from TreePlot import TreePlot
import Config

class MinimaxSearch():

    def __init__(self, currentState, maxDepth, display):
        self.currentState = currentState
        self.maxDepth = maxDepth
        self.display = display

    def search(self):

        rootNode = Node(self.currentState, None)

        maxPlayerFlag = True
        playerValue = Config.computerPlayer
        depth = self.maxDepth

        bestScore = self.minimax(rootNode, depth, maxPlayerFlag, playerValue)

        bestMove = rootNode.getBestMove(bestScore)

        if self.display:
            treePlot = TreePlot()
            treePlot.generateDiagram(rootNode, bestMove)

        return bestMove

    def minimax(self, node, depth, maxPlayerFlag, playerValue):
        if depth == 0:
            node.score = node.state.evaluateState()
            return node.score
        else:
            if maxPlayerFlag:
                score = -float("inf")
            else:
                score = float("inf")

            childStates, moves = node.state.successorFunction(playerValue)

            if len(childStates) == 0:
                node.score = node.state.evaluateState()
                return node.score
            
            for index in range(len(childStates)):
                childState, move = childStates[index], moves[index]
                childNode = Node(childState, move)

                node.addChild(childNode)

                childScore = self.minimax(childNode, depth -1, not maxPlayerFlag, 1-playerValue)

                if maxPlayerFlag:
                    score = max(score, childScore)
                else:
                    score = min(score, childScore)

            node.score = score
            return score