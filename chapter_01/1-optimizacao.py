from deap import base, creator, tools, algorithms
import random
import numpy as np
import matplotlib.pyplot as plt

# Definir a função a ser otimizada (exemplo: f(x) = (x - 5) ** 2)
def objective_function(individual):
    x = individual[0]
    return (x - 5) ** 2,

# Criar o tipo de aptidão para minimização e o tipo de indivíduo
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Configuração do DEAP
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, 0, 10)  # Atributo do indivíduo
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, 1)  # Criar um indivíduo
toolbox.register("population", tools.initRepeat, list, toolbox.individual)  # Criar uma população
toolbox.register("evaluate", objective_function)  # Registrar a função de avaliação
toolbox.register("mate", tools.cxBlend, alpha=0.5)  # Crossover
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)  # Mutação
toolbox.register("select", tools.selTournament, tournsize=3)  # Seleção

# Parâmetros da simulação
population = toolbox.population(n=100)
num_generations = 30
fits = []

for gen in range(num_generations):
    # Avaliar todos os indivíduos na população
    fits_gen = []
    for ind in population:
        ind.fitness.values = toolbox.evaluate(ind)
        fits_gen.append(ind.fitness.values[0])  # Aqui garantimos que estamos acessando o valor correto

    fits.append(fits_gen)

    # Selecionar o próximo gerado
    offspring = toolbox.select(population, len(population))
    offspring = list(map(toolbox.clone, offspring))  # Clonar a próxima geração

    # Crossover e mutação
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < 0.5:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

    for mutant in offspring:
        if random.random() < 0.2:
            toolbox.mutate(mutant)
            del mutant.fitness.values

    # Atualizar a população
    population[:] = offspring

# Visualização dos resultados
plt.plot(range(num_generations), [min(f) for f in fits], label="Fitness Mínimo")
plt.xlabel("Gerações")
plt.ylabel("Fitness")
plt.title("Otimização de Funções - Evolução do Fitness")
plt.legend()
plt.show()
