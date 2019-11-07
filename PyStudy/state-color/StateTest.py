from State import State
import matplotlib.pyplot as plt
import Constraint as cst

class StateTest():

    def testImage(self):

        initialState = State()
        intermediateState = State(initialState.assignment, "state1", "red")

        image = intermediateState.drawState()
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

    def testHeuristic(self):

        initialState = State()
        intermediateState = State(initialState.assignment, "state1", "red")

        variable = intermediateState.selectHeuristicUnassignedVariable()

        print("Variable ", variable)

        print("---------------------------")

        orderDomainValues = intermediateState.getHeuristicOrderDomainValues(variable)

        print("orderDomainValues ", orderDomainValues)

stateTest = StateTest()

stateTest.testHeuristic()