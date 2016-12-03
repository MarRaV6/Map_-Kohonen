from random import random
from settings import *


class OutputLayer:
    def __init__(self, weight_relation_vector, quantity_cluster):
        self.weight_relation_vector = weight_relation_vector
        self.quantity_cluster = quantity_cluster
        self.new_number = 0

        self.matrix_distance_neuron = []
        self.__form_matrix_distance()

    def __form_matrix_distance(self):
        for i in range(self.quantity_cluster):
            self.matrix_distance_neuron.append([])
            for j in range(self.quantity_cluster):
                sum = 0
                for k in range(QUANTITY_INPUT):
                    sum += (self.weight_relation_vector[j][k] - self.weight_relation_vector[i][k]) ** 2

                sum = sum ** 0.5
                self.matrix_distance_neuron[i].append(round(sum, 5))

    def change_weight(self, number_winner, delta_function, speed_function, input):
        neibour = self.matrix_distance_neuron[number_winner]
        new_weight = []
        for i in range(self.quantity_cluster):
            new_weight.append([])
            if i != number_winner:
                if (neibour[i] < delta_function) and (neibour[i] > MIN_DELTA_WEIGHT):
                    for k in range(QUANTITY_INPUT):
                        weight = self.weight_relation_vector[i][k] + speed_function * (2.7 ** (- neibour[i] / (2 * delta_function))) * (input[k] - self.weight_relation_vector[i][k])
                        new_weight[i].append(round(weight, 5))
                else:
                    new_weight[i] = self.weight_relation_vector[i]

            else:
                for k in range(QUANTITY_INPUT):
                    weight = self.weight_relation_vector[i][k] + speed_function * NEIBOURHOOD * \
                                                                 (input[k] - self.weight_relation_vector[i][k])
                    new_weight[i].append(round(weight, 5))

                self.new_number = new_weight[i]

            #print('из', self.weight_relation_vector[i], 'в', new_weight[i])
            #print('-------------')

        #coordinates_new_weight = vizual_sample(QUANTITY_INPUT, self.quantity_cluster, new_weight)
        #plt.plot(coordinates_new_weight[0],coordinates_new_weight[1], 'ro')
        #plt.plot(coordinates_output_weight[0], coordinates_output_weight[1], 'go')
        #plt.show()

        self.weight_relation_vector = new_weight
        self.__form_matrix_distance()
