#!/usr/bin/env python

import math
import random


def calc_dist(a_x, a_y, b_x, b_y):
    # Calculates the distance between two positions
    return math.sqrt((b_x - a_x)**2 +
                     (b_y - a_y)**2)


def generate_pathway(sequence):
    # Generates a pathway vector of a specific sequence of positions
    return [(sequence[i], sequence[i+1])
            for i in range(len(sequence)-1)]


def calc_fitness(pathway, distances):
    # Calculates the fitness of a specific pathway using distances dict
    fitness = 0
    for a, b in pathway:
        fitness += distances[a+b]
    return fitness


def mutate_sequence(sequence):
    # Exchanges two random positions of sequence and return mutated sequence
    mutated_sequence = list(sequence)
    pos1 = pos2 = 0
    while pos1 == pos2:
        pos1 = random.randint(0, len(sequence)-1)
        pos2 = random.randint(0, len(sequence)-1)
    mutated_sequence[pos1] = sequence[pos2]
    mutated_sequence[pos2] = sequence[pos1]

    return "".join(mutated_sequence)


def main():
    # Searching for the optimal pathway between coordinates
    # Optimal pathway would have the least combined distance
    coordinates = (
        ("A", 1, 10),
        ("B", 4, 5),
        ("C", 9, 9),
        ("D", 10, 1),
        ("E", 7, 6),
        ("F", 3, 9),
        ("G", 2, 3)
    )

    # Calculate all distances and loading them into reference dict
    distances = {}
    for a, a_x, a_y in coordinates:
        for b, b_x, b_y in coordinates:
            if a != b:
                dist = calc_dist(a_x, a_y, b_x, b_y)
                distances[a+b] = dist

    # Select initial sequene for optimization
    best_sequence = "".join([ele[0] for ele in coordinates])

    best_pathway = generate_pathway(best_sequence)

    best_fitness = calc_fitness(best_pathway, distances)
    print(best_sequence, best_fitness)
    for i in range(100):
        # Mutate base sequence
        sequence = mutate_sequence(best_sequence)

        # Generate pathway vectors
        pathway = generate_pathway(sequence)

        # Calculate fitness using distances dictionary
        fitness = calc_fitness(pathway, distances)

        # If fitness improves compared to last generation, use the mutated sequence as basis
        if fitness < best_fitness:
            best_sequence = sequence
            best_fitness = fitness
            print(sequence, fitness)


if __name__ == "__main__":
    main()
