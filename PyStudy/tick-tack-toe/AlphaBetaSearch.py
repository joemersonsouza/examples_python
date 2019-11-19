from Node import Node

class AlphaBetaSearch:

    def __init__(self, currentState, currentMaxDepth):
        self.currentMaxDepth = currentMaxDepth
        self.currentState = currentState

    def search(self):
        rootNode = Node(self.currentState, None)

        maxPlayerFlag = True
        playerIndex = 0
        depth = self.currentMaxDepth
        alpha = -float("inf")
        beta = float("inf")

        bestScore = self.alphaBetaSearch(rootNode, depth, maxPlayerFlag, playerIndex, alpha, beta)

        bestMove = rootNode.getBestMove(bestScore)

        return bestMove

    def alphaBetaSearch(self, node, depth, maxPlayerFlag, playerIndex, alpha, beta):
        if depth == 0:
            node.score = node.evaluateState()
            return node.score
        else:
            childStates, moves = node.state.successorFunction(playerIndex) 

            if len(childStates) == 0:
                node.score = node.state.evaluateState()
                return node.score
            
            for index in range(len(childStates)):
                childState, move = childStates[index], moves[index]
                childNode = Node(childState, move)

                node.addChild(childNode)

                childScore = self.alphaBetaSearch(childNode, depth - 1, \
                    not maxPlayerFlag, 1 - playerIndex, alpha, beta)
                
                if maxPlayerFlag:
                    alpha = max(alpha, childScore)
                    node.score = alpha
                    if beta <= alpha:
                        return alpha
                else:
                    beta = min(beta, childScore)
                    node.score = beta
                    if beta <= alpha:
                        return beta

            node.alpha = alpha
            node.beta = beta

            if maxPlayerFlag:
                return alpha
            else:
                return beta