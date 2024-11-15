############
############ ALTHOUGH I GIVE YOU THIS TEMPLATE PROGRAM WITH THE NAME 'skeleton.py', 
############ YOU CAN RENAME IT TO ANYTHING YOU LIKE. HOWEVER, FOR THE PURPOSES OF 
############ THE EXPLANATION IN THESE COMMENTS, I ASSUME THAT THIS PROGRAM IS STILL 
############ CALLED 'skeleton.py'.
############
############ IF YOU WISH TO IMPORT STANDARD MODULES, YOU CAN ADD THEM AFTER THOSE BELOW.
############ NOTE THAT YOU ARE NOT ALLOWED TO IMPORT ANY NON-STANDARD MODULES! TO SEE
############ THE STANDARD MODULES, TAKE A LOOK IN 'validate_before_handin.py'.
############
############ DO NOT INCLUDE ANY COMMENTS ON A LINE WHERE YOU IMPORT A MODULE.
############

import os
import sys
import time
import random
from math import inf
from typing import List, Tuple

############ START OF SECTOR 1 (IGNORE THIS COMMENT)
############
############ NOW PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############ BY 'DO NOT TOUCH' I REALLY MEAN THIS. EVEN CHANGING THE SYNTAX, BY
############ ADDING SPACES OR COMMENTS OR LINE RETURNS AND SO ON, COULD MEAN THAT
############ CODES MIGHT NOT RUN WHEN I RUN THEM!
############

def read_file_into_string(input_file, ord_range):
    the_file = open(input_file, 'r') 
    current_char = the_file.read(1) 
    file_string = ""
    length = len(ord_range)
    while current_char != "":
        i = 0
        while i < length:
            if ord(current_char) >= ord_range[i][0] and ord(current_char) <= ord_range[i][1]:
                file_string = file_string + current_char
                i = length
            else:
                i = i + 1
        current_char = the_file.read(1)
    the_file.close()
    return file_string

def remove_all_spaces(the_string):
    length = len(the_string)
    new_string = ""
    for i in range(length):
        if the_string[i] != " ":
            new_string = new_string + the_string[i]
    return new_string

def integerize(the_string):
    length = len(the_string)
    stripped_string = "0"
    for i in range(0, length):
        if ord(the_string[i]) >= 48 and ord(the_string[i]) <= 57:
            stripped_string = stripped_string + the_string[i]
    resulting_int = int(stripped_string)
    return resulting_int

def convert_to_list_of_int(the_string):
    list_of_integers = []
    location = 0
    finished = False
    while finished == False:
        found_comma = the_string.find(',', location)
        if found_comma == -1:
            finished = True
        else:
            list_of_integers.append(integerize(the_string[location:found_comma]))
            location = found_comma + 1
            if the_string[location:location + 5] == "NOTE=":
                finished = True
    return list_of_integers

def build_distance_matrix(num_cities, distances, city_format):
    dist_matrix = []
    i = 0
    if city_format == "full":
        for j in range(num_cities):
            row = []
            for k in range(0, num_cities):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    elif city_format == "upper_tri":
        for j in range(0, num_cities):
            row = []
            for k in range(j):
                row.append(0)
            for k in range(num_cities - j):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    else:
        for j in range(0, num_cities):
            row = []
            for k in range(j + 1):
                row.append(0)
            for k in range(0, num_cities - (j + 1)):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    if city_format == "upper_tri" or city_format == "strict_upper_tri":
        for i in range(0, num_cities):
            for j in range(0, num_cities):
                if i > j:
                    dist_matrix[i][j] = dist_matrix[j][i]
    return dist_matrix

def read_in_algorithm_codes_and_tariffs(alg_codes_file):
    flag = "good"
    code_dictionary = {}   
    tariff_dictionary = {}  
    if not os.path.exists(alg_codes_file):
        flag = "not_exist"  
        return code_dictionary, tariff_dictionary, flag
    ord_range = [[32, 126]]
    file_string = read_file_into_string(alg_codes_file, ord_range)  
    location = 0
    EOF = False
    list_of_items = []  
    while EOF == False: 
        found_comma = file_string.find(",", location)
        if found_comma == -1:
            EOF = True
            sandwich = file_string[location:]
        else:
            sandwich = file_string[location:found_comma]
            location = found_comma + 1
        list_of_items.append(sandwich)
    third_length = int(len(list_of_items)/3)
    for i in range(third_length):
        code_dictionary[list_of_items[3 * i]] = list_of_items[3 * i + 1]
        tariff_dictionary[list_of_items[3 * i]] = int(list_of_items[3 * i + 2])
    return code_dictionary, tariff_dictionary, flag

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ THE RESERVED VARIABLE 'input_file' IS THE CITY FILE UNDER CONSIDERATION.
############
############ IT CAN BE SUPPLIED BY SETTING THE VARIABLE BELOW OR VIA A COMMAND-LINE
############ EXECUTION OF THE FORM 'python skeleton.py city_file.txt'. WHEN SUPPLYING
############ THE CITY FILE VIA A COMMAND-LINE EXECUTION, ANY ASSIGNMENT OF THE VARIABLE
############ 'input_file' IN THE LINE BELOW iS SUPPRESSED.
############
############ IT IS ASSUMED THAT THIS PROGRAM 'skeleton.py' SITS IN A FOLDER THE NAME OF
############ WHICH IS YOUR USER-NAME, E.G., 'abcd12', WHICH IN TURN SITS IN ANOTHER
############ FOLDER. IN THIS OTHER FOLDER IS THE FOLDER 'city-files' AND NO MATTER HOW
############ THE NAME OF THE CITY FILE IS SUPPLIED TO THIS PROGRAM, IT IS ASSUMED THAT 
############ THE CITY FILE IS IN THE FOLDER 'city-files'.
############
############ END OF SECTOR 1 (IGNORE THIS COMMENT)

input_file = "AISearchfile017.txt"

############ START OF SECTOR 2 (IGNORE THIS COMMENT)
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if len(sys.argv) > 1:
    input_file = sys.argv[1]

############ END OF SECTOR 2 (IGNORE THIS COMMENT)
path_for_city_files = "../city-files"
############ START OF SECTOR 3 (IGNORE THIS COMMENT)
    
if os.path.isfile(path_for_city_files + "/" + input_file):
    ord_range = [[32, 126]]
    file_string = read_file_into_string(path_for_city_files + "/" + input_file, ord_range)
    file_string = remove_all_spaces(file_string)
    print("I have found and read the input file " + input_file + ":")
else:
    print("*** error: The city file " + input_file + " does not exist in the city-file folder.")
    sys.exit()

location = file_string.find("SIZE=")
if location == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
comma = file_string.find(",", location)
if comma == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
num_cities_as_string = file_string[location + 5:comma]
num_cities = integerize(num_cities_as_string)
print("   the number of cities is stored in 'num_cities' and is " + str(num_cities))

comma = comma + 1
stripped_file_string = file_string[comma:]
distances = convert_to_list_of_int(stripped_file_string)

counted_distances = len(distances)
if counted_distances == num_cities * num_cities:
    city_format = "full"
elif counted_distances == (num_cities * (num_cities + 1))/2:
    city_format = "upper_tri"
elif counted_distances == (num_cities * (num_cities - 1))/2:
    city_format = "strict_upper_tri"
else:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()

dist_matrix = build_distance_matrix(num_cities, distances, city_format)
print("   the distance matrix 'dist_matrix' has been built.")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ YOU NOW HAVE THE NUMBER OF CITIES STORED IN THE INTEGER VARIABLE 'num_cities'
############ AND THE TWO_DIMENSIONAL MATRIX 'dist_matrix' HOLDS THE INTEGER CITY-TO-CITY 
############ DISTANCES SO THAT 'dist_matrix[i][j]' IS THE DISTANCE FROM CITY 'i' TO CITY 'j'.
############ BOTH 'num_cities' AND 'dist_matrix' ARE RESERVED VARIABLES AND SHOULD FEED
############ INTO YOUR IMPLEMENTATIONS.
############
############ THERE NOW FOLLOWS CODE THAT READS THE ALGORITHM CODES AND TARIFFS FROM
############ THE TEXT-FILE 'alg_codes_and_tariffs.txt' INTO THE RESERVED DICTIONARIES
############ 'code_dictionary' AND 'tariff_dictionary'. DO NOT AMEND THIS CODE!
############ THE TEXT FILE 'alg_codes_and_tariffs.txt' SHOULD BE IN THE SAME FOLDER AS
############ THE FOLDER 'city-files' AND THE FOLDER WHOSE NAME IS YOUR USER-NAME.
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############
############ END OF SECTOR 3 (IGNORE THIS COMMENT)

############ START OF SECTOR 4 (IGNORE THIS COMMENT)
path_for_alg_codes_and_tariffs = "../alg_codes_and_tariffs.txt"
############ END OF SECTOR 4 (IGNORE THIS COMMENT)

############ START OF SECTOR 5 (IGNORE THIS COMMENT)
code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs(path_for_alg_codes_and_tariffs)

if flag != "good":
    print("*** error: The text file 'alg_codes_and_tariffs.txt' does not exist.")
    sys.exit()

print("The codes and tariffs have been read from 'alg_codes_and_tariffs.txt':")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU NOW NEED TO SUPPLY SOME PARAMETERS.
############
############ THE RESERVED STRING VARIABLE 'my_user_name' SHOULD BE SET AT YOUR
############ USER-NAME, E.G., "abcd12"
############
############ END OF SECTOR 5 (IGNORE THIS COMMENT)

my_user_name = "ttrq46"

############ START OF SECTOR 6 (IGNORE THIS COMMENT)
############
############ YOU CAN SUPPLY, IF YOU WANT, YOUR FULL NAME. THIS IS NOT USED AT ALL BUT SERVES AS
############ AN EXTRA CHECK THAT THIS FILE BELONGS TO YOU. IF YOU DO NOT WANT TO SUPPLY YOUR
############ NAME THEN EITHER SET THE STRING VARIABLES 'my_first_name' AND 'my_last_name' AT 
############ SOMETHING LIKE "Mickey" AND "Mouse" OR AS THE EMPTY STRING (AS THEY ARE NOW;
############ BUT PLEASE ENSURE THAT THE RESERVED VARIABLES 'my_first_name' AND 'my_last_name'
############ ARE SET AT SOMETHING).
############
############ END OF SECTOR 6 (IGNORE THIS COMMENT)

my_first_name = "Yosef"
my_last_name = "Berezovskiy"

############ START OF SECTOR 7 (IGNORE THIS COMMENT)
############
############ YOU NEED TO SUPPLY THE ALGORITHM CODE IN THE RESERVED STRING VARIABLE 'algorithm_code'
############ FOR THE ALGORITHM YOU ARE IMPLEMENTING. IT NEEDS TO BE A LEGAL CODE FROM THE TEXT-FILE
############ 'alg_codes_and_tariffs.txt' (READ THIS FILE TO SEE THE CODES).
############
############ END OF SECTOR 7 (IGNORE THIS COMMENT)

algorithm_code = "AC"

############ START OF SECTOR 8 (IGNORE THIS COMMENT)
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if not algorithm_code in code_dictionary:
    print("*** error: the algorithm code " + algorithm_code + " is illegal")
    sys.exit()
print("   your algorithm code is legal and is " + algorithm_code + " -" + code_dictionary[algorithm_code] + ".")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU CAN ADD A NOTE THAT WILL BE ADDED AT THE END OF THE RESULTING TOUR FILE IF YOU LIKE,
############ E.G., "in my basic greedy search, I broke ties by always visiting the first 
############ city found" BY USING THE RESERVED STRING VARIABLE 'added_note' OR LEAVE IT EMPTY
############ IF YOU WISH. THIS HAS NO EFFECT ON MARKS BUT HELPS YOU TO REMEMBER THINGS ABOUT
############ YOUR TOUR THAT YOU MIGHT BE INTERESTED IN LATER.
############
############ END OF SECTOR 8 (IGNORE THIS COMMENT)

added_note = "Basic version of Ranked Ant Colony Optimization incorporating an additional hyperparameter to set the quantity of pheromone left by an ant on the city-to-city edge after it visits the city. This allows additional control over exploration and exploitation + as determined experimentally, increasing likelihood of obtaining optimal/close to optimal solutions. This implementation also incorporates basic 2-opt local search techniques to refine discovered tours and allows convergence in less iterations"

############
############ NOW YOUR CODE SHOULD BEGIN.
############










ANT_COUNT = 10
ITERATIONS_COUNT = 100
ALPHA = 3
BETA = 1
RHO = 0.1
W = 6
Q = 10
LOCAL_SEARCH_PERIOD = 25

class RankedAntColonyOptimization:
    """
    Ranked Ant Colony Optimization (Ranked ACO) algorithm for solving the Traveling Salesman Problem (TSP)
    using a 2D distance matrix.
    """
    def __init__(self, dist_matrix: List[List[float]], ant_count: int = ANT_COUNT,
                 iterations_count: int = ITERATIONS_COUNT, alpha: float = ALPHA, beta: float = BETA,
                 rho: float = RHO, w: int = W, q: float = Q, two_opt_period: int = LOCAL_SEARCH_PERIOD):
        """
        Initialize a new instance of the Ranked ACO algorithm with the given parameters.

        :param dist_matrix: The distance matrix representing the pairwise distances between cities.
        :param ant_count: The number of ants to use in the algorithm.
        :param iterations_count: The number of iterations the algorithm will run.
        :param alpha: The relative importance of pheromone trail in the algorithm.
        :param beta: The relative importance of heuristic information (inverse of distance) in the algorithm.
        :param rho: The pheromone evaporation rate.
        :param w: The number of top-ranked ants used to update the pheromone trails.
        :param q: A constant to be added to the pheromone update value.
        :param two_opt_period: The period (in iterations) for applying 2-opt local search.
        """
        self.dist_matrix = dist_matrix
        self.ant_count = ant_count
        self.iterations_count = iterations_count
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.w = W
        self.q = q
        self.two_opt_period = two_opt_period
        self.city_count = len(dist_matrix)
        self.tau_matrix = self.initialize_tau_matrix()
        self.timeout = 55
        self.start_time = None
        
    def nearest_neighbour(self) -> Tuple[List[int], float]:
        """
        Finds a tour using the Nearest Neighbour (NN) heuristic.

        :return: A tuple containing the NN tour and its length.
        """
        visited = [False] * self.city_count
        current_city = random.randint(0, self.city_count - 1)
        visited[current_city] = True
        tour = [current_city]
        tour_length = 0
        
        for _ in range(self.city_count - 1):
            min_distance = inf
            nearest_city = -1
            for j in range(self.city_count):
                if not visited[j] and self.dist_matrix[current_city][j] < min_distance:
                    min_distance = self.dist_matrix[current_city][j]
                    nearest_city = j
            visited[nearest_city] = True
            tour.append(nearest_city)
            tour_length += min_distance
            current_city = nearest_city
        tour_length += self.dist_matrix[current_city][0]
        return tour, tour_length
    
    def initialize_tau_matrix(self) -> List[List[float]]:
        """
        Initializes the pheromone trail matrix.

        :return: The initialized pheromone trail matrix.
        """
        l_nn_tour, l_nn = self.nearest_neighbour()
        tau_0 = self.city_count / l_nn
        tau_matrix = [[tau_0 for _ in range(self.city_count)] for _ in range(self.city_count)]
        for i in range(self.city_count):
            for j in range(self.city_count):
                tau_matrix[i][j] = tau_0
        return tau_matrix
    
    def choose_next_city(self, current_city: int, forbidden_cities: List[bool]) -> int:
        """
        Chooses the next city for an ant based on the current city, the pheromone trails, and the set of forbidden cities.

        :param current_city: The current city of the ant.
        :param forbidden_cities: A list of forbidden cities.
        :return: The index of the chosen next city.
        """
        probabilities = []

        for city in range(self.city_count):
            if not forbidden_cities[city] and self.dist_matrix[current_city][city] != 0:
                tau_for_city = self.tau_matrix[current_city][city] ** self.alpha
                eta_for_city = (1 / self.dist_matrix[current_city][city]) ** self.beta
                probabilities.append(tau_for_city * eta_for_city)
            else:
                probabilities.append(0)
        probabilities_sum = sum(probabilities)
        if probabilities_sum != 0:
            probabilities = [tau_eta_product / probabilities_sum for tau_eta_product in probabilities]
        else:
            while True:
                next_city =  random.randint(0, self.city_count - 1)
                if not forbidden_cities[next_city]:
                    return next_city                        
        return random.choices(range(self.city_count), weights=probabilities, k=1)[0]
    
    def two_opt(self, tour: List[int]) -> Tuple[List[int], float]:
        """
        Applies the 2-opt local search to improve a given tour.

        :param tour: A list representing the initial tour.
        :return: A tuple containing the improved tour and its length.
        """
        improved = True
        while improved:
            improved = False
            for i in range(1, len(tour) - 1):
                for j in range(i + 1, len(tour)):
                    if j - i == 1:
                        continue
                    old_cost = self.dist_matrix[tour[i - 1]][tour[i]] + self.dist_matrix[tour[j - 1]][tour[j]]
                    new_cost = self.dist_matrix[tour[i - 1]][tour[j - 1]] + self.dist_matrix[tour[i]][tour[j]]
                    if new_cost < old_cost:
                        tour[i:j] = reversed(tour[i:j])
                        improved = True
                        break
                if improved:
                    break
        tour_length = sum(self.dist_matrix[tour[city - 1]][tour[city]] for city in range(self.city_count))
        return tour, tour_length
    
    def build_ant_trail(self) -> Tuple[List[int], float]:
        """
        Constructs a tour for a single ant by choosing the next city using the `choose_next_city` method.

        :return: A tuple containing the tour and its length.
        """
        forbidden_cities = [False] * self.city_count
        current_city = random.randint(0, self.city_count - 1)
        try:
            forbidden_cities[current_city] = True
        except IndexError:
            print(current_city)
        tour = [current_city]
        
        for _ in range(self.city_count - 1):
            next_city = self.choose_next_city(current_city, forbidden_cities)
            forbidden_cities[next_city] = True
            tour.append(next_city)
            current_city = next_city
            
        tour_length = sum(self.dist_matrix[tour[city - 1]][tour[city]] for city in range(self.city_count))

        return tour, tour_length
        
    def update_tau(self, tours: List[List[int]], tour_lengths: List[float]) -> None:
        """
        Updates the pheromone trail matrix based on the tours and tour lengths of the ants in the current iteration. Also updates the pheromone 
        trail for the best tour.
        :param tours: A list of tours constructed by the ants in the current iteration.
        :param tour_lengths: A list of the lengths of the tours in the current iteration.
        """
        delta_tau = [[0 for _ in range(self.city_count)] for _ in range(self.city_count)]
        
        sorted_tours = sorted(zip(tour_lengths, tours))
        top_ranked_tours = sorted_tours[:self.w]
        
        for rank, (length, tour) in enumerate(top_ranked_tours):
            for i in range(1, len(tour)):
                delta_tau[tour[i - 1]][tour[i]] += (self.w - rank + self.q) / length
                delta_tau[tour[i]][tour[i - 1]] += (self.w - rank + self.q) / length
        for i in range(self.city_count):
                for j in range(self.city_count):
                    self.tau_matrix[i][j] = (1 - self.rho) * self.tau_matrix[i][j] + delta_tau[i][j]
        
        best_tour_length, best_tour = top_ranked_tours[0][0], top_ranked_tours[0][1]
        
        for i in range(1, len(best_tour)):
            self.tau_matrix[best_tour[i - 1]][best_tour[i]] += self.w / best_tour_length
            self.tau_matrix[best_tour[i]][best_tour[i - 1]] += self.w / best_tour_length
            
    def run(self) -> Tuple[List[int], float]:
        """
        Runs the Ranked ACO algorithm for the given number of iterations.

        :return: A tuple containing the best tour found and its length.
        """
        
        best_tour = None
        best_tour_length = inf
        self.start_time = time.time()
        for iteration in range(self.iterations_count): 
            tours = []
            tour_lengths = []
            
            for _ in range(self.ant_count): 
                if self.timeout and time.time() - self.start_time > self.timeout:
                    break
                tour, tour_length = self.build_ant_trail()
                if iteration % self.two_opt_period == 0:
                    tour, tour_length = self.two_opt(tour)
                tours.append(tour)
                tour_lengths.append(tour_length)

                if tour_length < best_tour_length:
                    best_tour = tour
                    best_tour_length = tour_length
                    
            self.update_tau(tours, tour_lengths)
        return best_tour, best_tour_length




ranked_aco = RankedAntColonyOptimization(dist_matrix=dist_matrix)
tour, tour_length = ranked_aco.run()





############ START OF SECTOR 9 (IGNORE THIS COMMENT)
############
############ YOUR CODE SHOULD NOW BE COMPLETE AND WHEN EXECUTION OF THIS PROGRAM 'skeleton.py'
############ REACHES THIS POINT, YOU SHOULD HAVE COMPUTED A TOUR IN THE RESERVED LIST VARIABLE 'tour', 
############ WHICH HOLDS A LIST OF THE INTEGERS FROM {0, 1, ..., 'num_cities' - 1} SO THAT EVERY INTEGER
############ APPEARS EXACTLY ONCE, AND YOU SHOULD ALSO HOLD THE LENGTH OF THIS TOUR IN THE RESERVED
############ INTEGER VARIABLE 'tour_length'.
############
############ YOUR TOUR WILL BE PACKAGED IN A TOUR FILE OF THE APPROPRIATE FORMAT AND THIS TOUR FILE'S,
############ NAME WILL BE A MIX OF THE NAME OF THE CITY FILE, THE NAME OF THIS PROGRAM AND THE
############ CURRENT DATE AND TIME. SO, EVERY SUCCESSFUL EXECUTION GIVES A TOUR FILE WITH A UNIQUE
############ NAME AND YOU CAN RENAME THE ONES YOU WANT TO KEEP LATER.
############
############ DO NOT TOUCH OR ALTER THE CODE BELOW THIS POINT! YOU HAVE BEEN WARNED!
############

flag = "good"
length = len(tour)
for i in range(0, length):
    if isinstance(tour[i], int) == False:
        flag = "bad"
    else:
        tour[i] = int(tour[i])
if flag == "bad":
    print("*** error: Your tour contains non-integer values.")
    sys.exit()
if isinstance(tour_length, int) == False:
    print("*** error: The tour-length is a non-integer value.")
    sys.exit()
tour_length = int(tour_length)
if len(tour) != num_cities:
    print("*** error: The tour does not consist of " + str(num_cities) + " cities as there are, in fact, " + str(len(tour)) + ".")
    sys.exit()
flag = "good"
for i in range(0, num_cities):
    if not i in tour:
        flag = "bad"
if flag == "bad":
    print("*** error: Your tour has illegal or repeated city names.")
    sys.exit()
check_tour_length = 0
for i in range(0, num_cities - 1):
    check_tour_length = check_tour_length + dist_matrix[tour[i]][tour[i + 1]]
check_tour_length = check_tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
if tour_length != check_tour_length:
    flag = print("*** error: The length of your tour is not " + str(tour_length) + "; it is actually " + str(check_tour_length) + ".")
    sys.exit()
print("You, user " + my_user_name + ", have successfully built a tour of length " + str(tour_length) + "!")

local_time = time.asctime(time.localtime(time.time()))
output_file_time = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
output_file_time = output_file_time.replace(" ", "0")
script_name = os.path.basename(sys.argv[0])
if len(sys.argv) > 2:
    output_file_time = sys.argv[2]
output_file_name = script_name[0:len(script_name) - 3] + "_" + input_file[0:len(input_file) - 4] + "_" + output_file_time + ".txt"

f = open(output_file_name,'w')
f.write("USER = " + my_user_name + " (" + my_first_name + " " + my_last_name + "),\n")
f.write("ALGORITHM CODE = " + algorithm_code + ", NAME OF CITY-FILE = " + input_file + ",\n")
f.write("SIZE = " + str(num_cities) + ", TOUR LENGTH = " + str(tour_length) + ",\n")
f.write(str(tour[0]))
for i in range(1,num_cities):
    f.write("," + str(tour[i]))
f.write(",\nNOTE = " + added_note)
f.close()
print("I have successfully written your tour to the tour file:\n   " + output_file_name + ".")

############ END OF SECTOR 9 (IGNORE THIS COMMENT)
    
    











    

