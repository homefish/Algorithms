'''
This is a test for a genetic algorithm using Python 3

------------------------------------------------------------------

References:

Genetic algorithm series on codewars
1) Genetic Algorithm Series - #1 Generate
   https://www.codewars.com/kata/567d609f1c16d7369c000008

2) Genetic Algorithm Series - #2 Mutation 	
   https://www.codewars.com/kata/567b39b27d0a4606a5000057

3) Genetic Algorithm Series - #3 Crossover
   https://www.codewars.com/kata/567d71b93f8a50f461000019

4) Genetic Algorithm Series - #4 Get population and fitnesses
   https://www.codewars.com/kata/567b468357ed7411be00004a

5) Genetic Algorithm Series - #5 Roulette wheel selection
   https://www.codewars.com/kata/567b21565ffbdb30e3000010

------------------------------------------------------------------

Genetic algorithm series on tech.io
1) History
   https://tech.io/playgrounds/334/genetic-algorithms/history

2) Encoding
   https://tech.io/playgrounds/334/genetic-algorithms/encoding

3) Tools
   https://tech.io/playgrounds/334/genetic-algorithms/tools

4) Algorithm
   https://tech.io/playgrounds/334/genetic-algorithms/algorithm

5) What now?
   https://tech.io/playgrounds/334/genetic-algorithms/what-now    


------------------------------------------------------------------


Optimization Lecture Notes by Zsófia Lendek
http://lendek.net/teaching/opt_en/ 

- Chapter 4: Genetic Algorithms
http://lendek.net/teaching/opt_en/ga.pdf


------------------------------------------------------------------


ECE 630 Special Topics:
Engineering Analysis and Design Using Genetic Algorithms
Summer 2007
https://engineering.purdue.edu/~sudhoff/ee630/

Lecture 1: Biological Genetics and Evolution
https://engineering.purdue.edu/~sudhoff/ee630/Lecture01.pdf


'''

import random


def fitness(chromosome):
    '''
    calculates the fitness score of a chromosome,
    where chromosome is a string of '0' and '1'
    '''
    return sum(int(c) for c in chromosome)


def create_chromosome(size):
    '''
    parameters:
        size of chromosome
    returns:
        chromosome string of '0' and '1'
    '''
    return "".join(str(random.randint(0,1)) for _ in range(size))


def create_population(population_size, chromosome_size):
    '''
    parameters:
        population_size
        chromosome_size
    returns
        list of chromosomes
    '''
    return [create_chromosome(chromosome_size) for _ in range(population_size)]


def mutate(chromosome):
    p = 1 / len(chromosome)
    new_chromosome = "".join((c, str((int(c)+1)%2))[random.random() <= p] for c in chromosome)
    return new_chromosome    


def crossover(chromosome1, chromosome2):
    index = random.randint(1, len(chromosome1)-1)
    a = chromosome1[:index] + chromosome2[index:]
    b = chromosome2[:index] + chromosome1[index:]
    return [a,b]


def selection(chromosomes_list):
    GRADED_RETAIN_PERCENT = 0.2     # percentage of retained best fitting individuals
    NONGRADED_RETAIN_PERCENT = 0.3  # percentage of retained remaining individuals (randomly selected)
    # TODO: implement the selection function
    #  * Sort individuals by their fitting score
    chromosomes_list.sort(reverse = True)
    
    #  * Select the best individuals
    best_individuals = chromosomes_list[:int(GRADED_RETAIN_PERCENT * len(chromosomes_list))]
    
    #  * Randomly select other individuals
    remaining_individuals = chromosomes_list[int(GRADED_RETAIN_PERCENT * len(chromosomes_list)):]
    other_individuals = random.shuffle(remaining_individuals)
    other_individuals = remaining_individuals[:int(NONGRADED_RETAIN_PERCENT * len(chromosomes_list))]
    
    return best_individuals + other_individuals


def generation(population):
    
    # selection
    select = selection(population)
    
    # reproduction
    # As long as we need individuals in the new population, fill it with children
    children = []
    # TODO: implement the reproduction
    while len(children) + len(select) < len(population):
        ## crossover
        parent1 = random.choice(select) # randomly selected
        parent2 = random.choice(select) # randomly selected
        # use the crossover(parent1, parent2) function created on exercise 2
        child1, child2 = crossover(parent1, parent2)
        
        ## mutation
        # use the mutation(child) function created on exercise 2
        child1 = mutate(child1)
        child2 = mutate(child2)
        children.append(child1)
        children.append(child2)
    
    # return the new generation
    return select + children


def is_answer(chrom):
    return chrom == '1' * len(chrom)
        


def algorithm():
    chrom_size = 100
    population_size = 10
    MAX_ITERATION = 1000

    
    # create the base population
    population = create_population(population_size, chrom_size)
    #print("initial population:")
    #print(population)
    #print()
    
    answers = []
    
    # while a solution has not been found :
    iteration = 0
    
    while not answers:
        iteration += 1
        ## create the next generation
        
        population = generation(population)  # ???
        #print(iteration, population)
        #print()
        
        ## display the average score of the population (watch it improve)
        # print(get_mean_score(population), file=sys.stderr)
    
        ## check if a solution has been found
        for chrom in population:
            if is_answer(chrom):
                print("found solution: ", chrom)
                answers.append(chrom)

        if iteration == MAX_ITERATION:
            print("max iteration reached")
            break

        if iteration % 10 == 0:
            print(iteration)
    
    # TODO: print the solution
    print("required iterations: ", iteration)
    print("answers: ", answers)


if __name__ == '__main__':
    algorithm()
    




