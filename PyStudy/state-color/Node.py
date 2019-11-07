from State import State

class Node:

    childNode = None
    state = State()

    def __init__(self, state=None):
        if(state != None):
            self.state = state
        self.children = []

    def addChild(self, childNode):
        self.childNode = childNode