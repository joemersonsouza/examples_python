
from EvolutionarySearch import EvolutionarySearch

nQueens = 8
ev = EvolutionarySearch(nQueens, True, True)

print(ev.population)

ev.search()