from EvolutionarySearch import EvolutionarySearch
import Config
import random


ev = EvolutionarySearch(Config.maxChromosomes)

for i in range(Config.maxPopulation):
    ev.computeIndividualFitness(i, random.randrange(0, 200))

print(ev.selectParents())
# ev.search()

# for i in range(Config.maxPopulation):
#     print(ev.getIndividual(i))