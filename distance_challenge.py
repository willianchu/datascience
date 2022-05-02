
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose 
import numpy as np

city_mapper = {
    0:'Vancouver',
    1:'Toronto',
    2:'Munich',
    3:'London',
    4:'Barcelona',
    5:'Paris',
    6:'Florence',
    7:'Dubai',
    8:'Perth',
    9:'Melbourne',
    10:'New Zealand',
    11:'India',
    12:'Nepal',
    13:'Japan',
    14:'Thailand',
    15:'Hawaii',
    16:'Seattle'    
}

# ditance between all cities in hours.
dist_list = [
    (0,1,4.0000),(0,2,10.0000),(0,3,9.3330),(0,4,13.0000),(0,5,9.7500),(0,6,12.5000),
    (0,7,17.5000),(0,8,22.0000),(0,9,18.7500),(0,10,16.7500),(0,11,24.0000),(0,12,22.0000),(0,13,10.0000),
    (0,14,25.0000),(0,15,6.0000),(0,16,0.5000),(1,2,8.7500),(1,3,6.7500),(1,4,10.0000),
    (1,5,7.2500),(1,6,10.0000),(1,7,12.7500),(1,8,29.0000),(1,9,25.0000),(1,10,24.0000),(1,11,22.5000),
    (1,12,19.0000),(1,13,16.0000),(1,14,22.0000),(1,15,10.0000),(1,16,5.0000),(2,3,2.0000),(2,4,2.0000),
    (2,5,1.5000),(2,6,1.2500),(2,7,6.0000),(2,8,18.5000),(2,9,21.5000),(2,10,30.0000),(2,11,12.0000),
    (2,12,12.2500),(2,13,14.0000),(2,14,13.5000),(2,15,18.5000),(2,16,13.0000),(3,4,2.0000),(3,5,1.0000),
    (3,6,2.0000),(3,7,6.7500),(3,8,18.7500),(3,9,21.5000),(3,10,27.0000),(3,11,13.0000),(3,12,11.5000),
    (3,13,12.0000),(3,14,12.0000),(3,15,17.5000),(3,16,10.0000),(4,5,2.3000),(4,6,1.7500),
    (4,7,6.5000),(4,8,19.7500),(4,9,21.0000),(4,10,31.0000),(4,11,17.0000),(4,12,12.2500),(4,13,15.5000),
    (4,14,14.0000),(4,15,21.5000),(4,16,13.5000),(5,6,1.7500),(5,7,6.6600),(5,8,18.5000),
    (5,9,21.7500),(5,10,30.0000),(5,11,16.0000),(5,12,12.0000),(5,13,12.0000),(5,14,13.6600),(5,15,18.0000),
    (5,16,12.7500),(6,7,10.7500),(6,8,25.0000),(6,9,25.0000),(6,10,34.0000),(6,11,17.0000),
    (6,12,15.5000),(6,13,15.7500),(6,14,15.0000),(6,15,21.7500),(6,16,14.0000),(7,8,10.5000),
    (7,9,13.4500),(7,10,21.7500),(7,11,7.8000),(7,12,3.7500),(7,13,9.5000),(7,14,6.0000),(7,15,18.7500),
    (7,16,14.7500),(8,9,3.5000),(8,10,19.0000),(8,11,22.0000),(8,12,12.7500),(8,13,13.7500),(8,14,10.5000),
    (8,15,16.3300),(8,16,22.5000),(9,10,6.0000),(9,11,26.0000),(9,12,16.0000),(9,13,10.0000),(9,14,9.0000),
    (9,15,10.2500),(9,16,19.5000),(10,11,33.0000),(10,12,20.4400),(10,13,15.0000),(10,14,20.0000),(10,15,22.0000),
    (10,16,19.5000),(11,12,5.0000),(11,13,17.7500),(11,14,9.2500),(11,15,36.0000),(11,16,28.0000),(12,13,6.3300),
    (12,14,10.3300),(12,15,24.0000),(12,16,24.0000),(13,14,10.5000),(13,15,6.7500),(13,16,9.0000),
    (14,15,27.0000),(14,16,25.0000),(15,16,5.5000)
]
# Initialize fitness function object using dist_list

#createlist of city coordinates
coords_list = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 0)]
# Initialize fitness function object using coords_list
fitness_coords = mlrose.TravellingSales(coords = coords_list)

# Initialize fitness function object using dist_list
fitness_dists = mlrose.TravellingSales(distances = dist_list)

# define a optimization object

problem_fit = mlrose.TSPOpt(length = 17, fitness_fn = fitness_coords, maximize=False)

# Define optimization problem object
problem_no_fit = mlrose.TSPOpt(length = 17, coords = coords_list, maximize=False)

# Solve problem using the genetic algorithm ##
best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2, mutation_prob = 0.3, max_attempts = 100)

# def city_name(city_num):
#     return city_mapper[city_num]

# def print_route(route):
#     for i in range(len(route)):
#         print(city_name(route[i]), end = ' ')
#     print()

print('The best state found is: ', best_state)

print('The fitness at the best state is: ', best_fitness)

#print type of best_state 
# print(type(best_state))

# print_route(best_state)

# Use mlrose to find the most optimal route to visit all the places in city_mapper throughout the challenge.


