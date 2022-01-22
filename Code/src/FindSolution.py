from Data import Data
from GeneticAlgorithms import GeneticAlgorithms
from Population import Population
from ClassScheduleDT import *

class FindSolution():
    def __init__(self, data: Data, population_size, number_of_elite_schedules, tournament_selection_size, mutation_rate):
        self._data = data
        self._POPULATION_SIZE = population_size
        self._NUMBER_OF_ELITE_SCHEDULES = number_of_elite_schedules
        self._TOURNAMENT_SELECTION_SIZE = tournament_selection_size
        self._MUTATION_RATE = mutation_rate

        # generation and sorted solution by time
        self._solution = self._find()
        self._solution.sort(key=lambda x: x.getMeetingTime().getId())

    def _find(self):

        generticAlogrithm = GeneticAlgorithms(self._data, self._POPULATION_SIZE, self._NUMBER_OF_ELITE_SCHEDULES, self._TOURNAMENT_SELECTION_SIZE, self._MUTATION_RATE)
        # Get first Sample to cross
        count_break = 0
        population = Population(self._POPULATION_SIZE, self._data)
        while (population.getSchedule()[0].getFitness() != 1.0):
            # Tạo ra được 1 quần thể mới có 9 cá thể.
            population = generticAlogrithm.evolve(population)
            population.getSchedule().sort(key=lambda x: x.getFitness(), reverse=True)
            print('Fitness:', population.getSchedule()[0].getFitness())

            count_break += 1
            if (count_break == 100): return False

        return population.getSchedule()[0].getClasses()

    def getTimeTable(self):
        return self._solution

    def __str__(self) -> str:
        return str()