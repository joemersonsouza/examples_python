import numpy as np
import random
import math
import matplotlib.pyplot as plt
import Config

class EvolutionarySearch:

    def __init__(self, nChromosomes):
        self.nChromosomes = nChromosomes
        self.fitness = self.fitness = np.zeros((Config.maxPopulation, 1))
        self.generationCount = 0

        self.population = np.zeros((Config.maxPopulation, self.nChromosomes), np.int8)

        for i in range(Config.maxPopulation):
            for j in range(self.nChromosomes):
                self.population[i, j] = random.randrange(0,2)

    def getIndividual(self, index):
        return self.population[index, :]

    def computeIndividualFitness(self, index, reward):
        self.fitness[index] += reward
        #self.computeFitnessWheel()
    
    def computeFitnessWheel(self):

        self.wheel = np.zeros((Config.maxPopulation, 1))
        self.wheel[0] = self.fitness[0]

        for index in range(1, Config.maxPopulation):
            self.wheel[index] = self.wheel[index - 1 ] + self.fitness[index]

        lastValue = self.wheel[Config.maxPopulation - 1]
        self.wheel = self.wheel / lastValue
    
    def selectParents(self):
        index1 = np.argmax(self.fitness)
        valueIndex1 = self.fitness[index1]
        self.fitness[index1] = -100
        index2 = np.argmax(self.fitness)
        self.fitness[index1] = valueIndex1
        return index1, index2
    
    def performVariation(self):

        newPopulation = np.zeros((Config.maxPopulation, self.nChromosomes), np.int8)

        for index in range(Config.maxPopulation):

            indexP1, indexP2 = self.selectParents()
            
            firstIndividual = self.population[indexP1, :]
            secondIndividual = self.population[indexP2, :]

            rand = random.random()
            if rand < Config.crossoverRate:
                child = self.crossOverParents(firstIndividual, secondIndividual)
            else:
                if self.fitness[indexP1] > self.fitness[indexP2]:
                    child = firstIndividual
                else:
                    child = secondIndividual

            child = self.mutateChild(child)

            newPopulation[index, :] = child
            self.fitness[indexP1] = self.fitness[indexP2] = -1

        self.population = newPopulation

    def crossOverParents(self, firstIndividual, secondIndividual):

        crossOverPoint = int(math.floor(self.nChromosomes * random.random()))
        firstPart = firstIndividual[0 : crossOverPoint + 1]
        secondpart = secondIndividual[crossOverPoint + 1: ]
        
        child = np.concatenate((firstPart, secondpart))

        return child
    
    def mutateChild(self, child):
        for index in range(self.nChromosomes):
            rand = random.random()
            if rand < Config.mutanteRation:
                child[index] = random.randrange(0,2)

        return child

    def search(self):
        
        self.generationCount += 1

        print("Mutations = " + str(self.generationCount))
        
        self.performVariation()
