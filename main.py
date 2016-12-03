import matplotlib.pyplot as plt
import random
from math import e

from input_layer import InputLayer
from output_layer import OutputLayer

from settings import *


def vizual_sample(number_input, lenght_data, list_data):
    coordinates = []
    for k in range(number_input):
        coordinates.append([])
        for i in range(lenght_data):
            coordinates[k].append(list_data[i][k])

    return coordinates


def form_sample(size_sample):
    input_vector = []

    for i in range(size_sample):
        t = [round((random.random()), 5) for _ in range(QUANTITY_INPUT)]
        input_vector.append(t)

    return input_vector


def form_weight_relation(quantity_cluster):
    weight_relation_vector = []
    for _ in range(quantity_cluster):
        t = [round((random.uniform(0.4, 0.6)), 5) for _ in range(QUANTITY_INPUT)]
        weight_relation_vector.append(t)

    return weight_relation_vector


if __name__ == '__main__':
    epoch = 10
    size_sample = 100
    quantity_cluster = 5

    output_layer = OutputLayer(form_weight_relation(quantity_cluster), quantity_cluster)
    input_layer = InputLayer(form_sample(size_sample), output_layer, size_sample=size_sample)

    help_epoch = []
    help_function = []

    speed_function_start = 0.5
    delta_function_start = 0.5
    for i in range(epoch):
        delta_function = (- i / (epoch + 1) + 1)
        #delta_function = 1
        speed_function = speed_function_start * e ** (i/epoch)
        k = input_layer.epoch(output_layer.weight_relation_vector, output_layer.quantity_cluster, delta_function, speed_function)

    coordinates_input_sample = vizual_sample(QUANTITY_INPUT, input_layer.size_sample, input_layer.input_vector)
    coordinates_output_weight = vizual_sample(QUANTITY_INPUT, output_layer.quantity_cluster, output_layer.weight_relation_vector)

    plt.plot(coordinates_input_sample[0], coordinates_input_sample[1], 'ro')
    #plt.plot(input_neuron_obj.input_vector[k][0], input_neuron_obj.input_vector[k][1], 'go')
    plt.plot(coordinates_output_weight[0], coordinates_output_weight[1], 'bo')
    plt.plot(input_layer.number[0], input_layer.number[1], 'gx')
    plt.plot(output_layer.new_number[0], output_layer.new_number[1], 'rx')
    plt.show()

    # создать класс Учитель и объединить слои
    # передать учителю экземпляр сети (инстанцию)
    # поменять функцию соседства
