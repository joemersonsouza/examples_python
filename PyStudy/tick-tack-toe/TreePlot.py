import pydot
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pylab as pl
from Node import Node
import Config


class TreePlot():

    def __init__(self):
        self.graph = pydot.Dot(graph_type="graph", dpi=800)
        self.index = 0

    def createGraph(self, node, bestMove):

        boardValues = node.state.boardValues
        htmlString = "<<table>"
        rows, cols = boardValues.shape

        for i in range(rows):
            htmlString += "<tr>"
            for j in range(cols):
                if boardValues[i,j] == -1:
                    htmlString += "<td bgcolor='#FF0000'>&nbsp;</td>"
                elif boardValues[i, j] == 0:
                    htmlString += "<td bgcolor='#00FF00'>"+Config.moveTexts[0]+"</td>"
                elif boardValues[i, j] == 1:
                    htmlString += "<td bgcolor='#0000FF'>"+Config.moveTexts[1]+"</td>"
            htmlString += "</tr>"
        htmlString += "</table>>"

        shape = "plaintext"

        if node.depth == 1 and node.move == bestMove:
            shape = "plain"

        parentGraphNode = pydot.Node(str(self.index), 
                                            shape=shape, 
                                            label=htmlString, 
                                            xlabel = node.score)
        
        self.index += 1

        self.graph.add_node(parentGraphNode)

        for childNode in node.children:
            childGraphNode = self.createGraph(childNode, bestMove)

            edge = pydot.Edge(parentGraphNode, childGraphNode, label = "[" + 
            str(childNode.move.row) + "," + str(childNode.move.col) + "]")

            self.graph.add_edge(edge)
        
        return parentGraphNode

    def generateDiagram(self, rootNode, currentNode):

        self.createGraph(rootNode, currentNode)

        figure = pl.figure()
        figure.add_subplot(1, 1, 1)

        self.graph.write_png('ticktack.png')
        img = mpimg.imread('ticktack.png')
        plt.imshow(img)
        plt.axis('off')
        plt.axis('tight')
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()
