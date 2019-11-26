import retro
import Config
import numpy as np
from EvolutionarySearch import EvolutionarySearch

def main():
    env = retro.make(game='Airstriker-Genesis')
    obs = env.reset()
    agent = EvolutionarySearch(Config.maxChromosomes)
    index = 0
    while True:
        if(index > Config.maxPopulation-1):
            index = 0

        action = agent.getIndividual(index)
        obs, reward, done, info = env.step(action)
        env.render()
        agent.computeIndividualFitness(index, reward)
        index += 1
  
        if done:
            print(reward, info, action, index)
            agent.search()
            obs = env.reset()
    env.close()


if __name__ == "__main__":
    main()