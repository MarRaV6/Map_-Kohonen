import random
from settings import *


class InputLayer:
    def __init__(self, input_vector, output, size_sample=0, number=0):
        self.input_vector = input_vector
        self.output = output
        self.size_sample = size_sample
        self.number = number

    def epoch(self, weight_vector, number_cluster, delta_function, speed_function):
        i = random.randint(0, self.size_sample-1)
        euclidean_distance = []
        for j in range(number_cluster):
            sum = 0
            for k in range(QUANTITY_INPUT):
                sum += (self.input_vector[i][k] - weight_vector[j][k]) ** 2
            euclidean_distance.append(sum ** 0.5)

        min_distance = min(euclidean_distance)
        number_neuron_winner = euclidean_distance.index(min_distance)
        self.number = weight_vector[number_neuron_winner]
        print(number_neuron_winner, 'при', self.input_vector[i], '(', i, ')')

        self.output.change_weight(number_neuron_winner, delta_function, speed_function, self.input_vector[i])

        # добавить константы максимального расстояния и минимального отличия веса.
        return i
