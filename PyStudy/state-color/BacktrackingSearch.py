from State import State
from Node import Node
import Constraint as cst
import matplotlib.pyplot as plt

class BacktrackingSearch():

    displayImage = False

    def __init__(self, isToDisplay=False):
        self.displayImage = isToDisplay

    def showImage(self, state):
        if self.displayImage:
            image = state.drawState()
            plt.imshow(image)
            font = {'family': 'serif',
                    'color': 'white',
                    'weight': 'normal',
                    'size': 15
                    }

            for variable in cst.variables:
                avgx = 0
                avgy = 0
                for (posx, posy) in cst.positions[variable]:
                    avgx += posx
                    avgy += posy
                avgx /= len(cst.positions[variable])
                avgy /= len(cst.positions[variable])
                plt.text(avgy-0.5, avgx, variable, fontdict=font)
            plt.axis('off')
            plt.show()

    def search(self):
        initialState= State()
        rootNode = Node(initialState)

        self.performBacktrackSearch(rootNode, rootNode)

    def performBacktrackSearch(self, rootNode, node):

        print("Assignment", node.state.assignment)

        if node.state.checkGoalState():
            print("reached goal state")
            return True
        else:
            variable = node.state.selectUnassignedVariable()
            self.showImage(node.state)
            
            for value in node.state.getOrderDomainValues():
                if cst.checkConstraints(node.state.assignment, variable, value):
                    childNode = Node(State(node.state.assignment, variable, value))
                    node.addChild(childNode)
                    self.showImage(childNode.state)
                    result = self.performBacktrackSearch(rootNode, childNode)
                    if result:
                        return True
            return False

bts = BacktrackingSearch(True)
bts.search()