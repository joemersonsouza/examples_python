from State import State

class Node():

    def __init__(self, state, move):
        self.state = state
        self.depth = 0
        self.children = []
        self.parent = None
        self.score = 0
        self.move = move

    def addChild(self, childNode):
        self.children.append(childNode)

    def printTree(self):
        print(self.depth, "-", self.state.value)
        for child in self.children:
            child.printTree()

    def getBestMove(self, bestScore):
        for child in self.children:
            if child.score == bestScore:
                return child.move
        
        return self.move
        