import numpy as np
import random
import math
import matplotlib.pyplot as plt
import Config

class EvolutionarySearch:

    def __init__(self, nChromosomes, unique, display):
        self.nChromosomes = nChromosomes
        self.unique = unique
        self.display = display
        self.wheel = []
        self.fitness = []

        self.population = np.zeros((Config.maxPopulation, self.nChromosomes), np.int8)

        for i in range(Config.maxPopulation):
            if self.unique:
                array = np.arange(self.nChromosomes)
                np.random.shuffle(array)

            for j in range(self.nChromosomes):
                if not self.unique:
                    value = math.floor(self.nChromosomes * random.random())
                    self.population[i, j] = value
                else:
                    self.population[i, j] = array[j]

    def drawIndividual(self, individual):

        figure = plt.figure()
        axis = figure.add_subplot(111)
        colors = ["black", "white"]

        for i in range(self.nChromosomes):
            chIndex = i % 2
            for j in range(self.nChromosomes):
                rect = plt.Rectangle((i,j), 1, 1, color=colors[chIndex])
                chIndex = 1 - chIndex
                axis.add_patch(rect)

        for i in range(self.nChromosomes):
            circle = plt.Circle((individual[i] + 0.5, i+0.5), 0.4, color = "blue")
            axis.add_patch(circle)

        axis.axis([0, self.nChromosomes, 0, self.nChromosomes])
        plt.title(str(individual))
        plt.grid
        plt.show()

    def computeIndividualFitness(self, individual):
        nAttacks = 0

        for i in range(self.nChromosomes):
            for j in range(i + 1, self.nChromosomes):

                if individual[i] == individual [j]:
                    nAttacks += 1

                difOne = j - i
                difTwo = math.fabs(individual[j] - individual[i])
                if difOne == difTwo:
                    nAttacks += 1
        
        return Config.maxFitness - nAttacks
    
    def computePopulationFitness(self):

        self.fitness = np.zeros((Config.maxPopulation, 1))

        for index in range(Config.maxPopulation):
            individual = self.population[index, :]

            self.fitness[index] = self.computeIndividualFitness(individual)
            self.computeFitnessWheel()
    
    def computeFitnessWheel(self):

        self.wheel = np.zeros((Config.maxPopulation, 1))
        self.wheel[0] = self.fitness[0]

        for index in range(1, Config.maxPopulation):
            self.wheel[index] = self.wheel[index - 1 ] + self.fitness[index]

        lastValue = self.wheel[Config.maxPopulation - 1]
        self.wheel = self.wheel / lastValue
    
    def selectParent(self):

        rand = random.random()
        for index in range(Config.maxPopulation):
            if self.wheel[index] >= rand:
                return index
    
    def performVariation(self):

        newPopulation = np.zeros((Config.maxPopulation, self.nChromosomes), np.int8)

        for index in range(Config.maxPopulation):

            indexP1 = self.selectParent()
            indexP2 = self.selectParent()
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

        self.population = newPopulation

    def crossOverParents(self, firstIndividual, secondIndividual):

        crossOverPoint = int(math.floor(self.nChromosomes * random.random()))

        firstPart = firstIndividual[0 : crossOverPoint + 1]

        if not self.unique:
            secondpart = secondIndividual[crossOverPoint + 1: ]
        else:
            secondpart = np.copy(secondIndividual)
            for index in range(len(firstPart)):
                j = np.argwhere(secondpart==firstPart[index])
                secondpart = np.delete(secondpart, j)
        
        child = np.concatenate((firstPart, secondpart))

        return child
    
    def mutateChild(self, child):

        for index in range(self.nChromosomes):
            rand = random.random()

            if rand < Config.mutanteRation:

                if not self.unique:
                    child[index] = int(math.floor(self.nChromosomes * random.random()))
                else:
                    j = int(math.floor(self.nChromosomes * random.random()))
                    child[index], child[j] = child[j], child[index]

        return child


    def checkBestSolution(self):

        solution = None
        found = False

        maxFitness = np.argmax(self.fitness)
        maxFitnessValue = self.fitness[maxFitness]

        if maxFitnessValue == Config.maxFitness:
            found = True
            solution = self.population[maxFitness, :]
        
        return found, solution

    def search(self):

        self.computePopulationFitness()

        self.generationCount = 0

        while True:

            found, solution = self.checkBestSolution()

            if found:
                print("Mutations = " + str(self.generationCount))
                print("S(x) = " + str(solution))
                self.drawIndividual(solution)
                break
            
            self.performVariation()

            self.computePopulationFitness()

            self.generationCount += 1
