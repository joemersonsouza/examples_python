from MinimaxSearch import MinimaxSearch
from State import State

initialState = State()
maxDepth = 2
display = True
miniMax = MinimaxSearch(initialState, maxDepth, display)
miniMax.search()