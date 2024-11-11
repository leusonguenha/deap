import numpy as np
import matplotlib.pyplot as plt

# Definir parâmetros do Algoritmo Genético
POPULATION_SIZE = 50
NUM_GENERATIONS = 100
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
X1_BOUND = (0, 6)  # Limites para x1 e x2
X2_BOUND = (0, 10)

# Função objetivo com penalização
def fitness_function(x1, x2):
    z = 3 * x1 + 2 * x2
    penalty = 0
    if x1 + x2 > 6:
        penalty += 10 * (x1 + x2 - 6)
    if 5 * x1 + 2 * x2 > 20:
        penalty += 10 * (5 * x1 + 2 * x2 - 20)
    return z - penalty

# Inicializar população
def initialize_population(size):
    population = []
    for _ in range(size):
        x1 = np.random.uniform(X1_BOUND[0], X1_BOUND[1])
        x2 = np.random.uniform(X2_BOUND[0], X2_BOUND[1])
        population.append((x1, x2))
    return population

# Seleção por torneio
def tournament_selection(population, fitness_values):
    selected = []
    for _ in range(len(population)):
        i, j = np.random.randint(0, len(population), 2)
        if fitness_values[i] > fitness_values[j]:
            selected.append(population[i])
        else:
            selected.append(population[j])
    return selected

# Crossover de ponto único
def crossover(parent1, parent2):
    if np.random.rand() < CROSSOVER_RATE:
        alpha = np.random.rand()
        child1 = (alpha * parent1[0] + (1 - alpha) * parent2[0],
                  alpha * parent1[1] + (1 - alpha) * parent2[1])
        child2 = ((1 - alpha) * parent1[0] + alpha * parent2[0],
                  (1 - alpha) * parent1[1] + alpha * parent2[1])
        return child1, child2
    return parent1, parent2

# Mutação
def mutate(individual):
    x1, x2 = individual
    if np.random.rand() < MUTATION_RATE:
        x1 = np.clip(x1 + np.random.uniform(-1, 1), X1_BOUND[0], X1_BOUND[1])
    if np.random.rand() < MUTATION_RATE:
        x2 = np.clip(x2 + np.random.uniform(-1, 1), X2_BOUND[0], X2_BOUND[1])
    return (x1, x2)

# Algoritmo Genético
def genetic_algorithm():
    population = initialize_population(POPULATION_SIZE)
    best_solution = None
    best_fitness = float('-inf')
    
    # Armazenar dados para visualização
    best_fitness_history = []
    x1_history = []
    x2_history = []
    
    for generation in range(NUM_GENERATIONS):
        fitness_values = [fitness_function(x1, x2) for x1, x2 in population]
        
        # Atualizar melhor solução
        max_fitness = max(fitness_values)
        if max_fitness > best_fitness:
            best_fitness = max_fitness
            best_solution = population[np.argmax(fitness_values)]
        
        # Armazenar o melhor fitness e os valores de x1, x2
        best_fitness_history.append(best_fitness)
        x1_history.append(best_solution[0])
        x2_history.append(best_solution[1])
        
        # Seleção, Crossover e Mutação
        selected_population = tournament_selection(population, fitness_values)
        next_generation = []
        for i in range(0, len(selected_population), 2):
            parent1 = selected_population[i]
            parent2 = selected_population[i + 1] if i + 1 < len(selected_population) else selected_population[0]
            child1, child2 = crossover(parent1, parent2)
            next_generation.append(mutate(child1))
            next_generation.append(mutate(child2))
        
        population = next_generation
    
    return best_solution, best_fitness, best_fitness_history, x1_history, x2_history

# Executar o Algoritmo Genético e obter os dados
solution, fitness, fitness_history, x1_history, x2_history = genetic_algorithm()
print("Melhor solução encontrada (x1, x2):", solution)
print("Valor máximo da função objetivo:", fitness)

# Visualizar gráfico de solução objetivo
plt.figure(figsize=(12, 5))

# Gráfico da função objetivo
plt.subplot(1, 2, 1)
plt.plot(fitness_history, label="Valor da Função Objetivo")
plt.xlabel("Gerações")
plt.ylabel("Fitness")
plt.title("Evolução da Função Objetivo")
plt.legend()

# Gráficos de x1 e x2
plt.subplot(1, 2, 2)
plt.plot(x1_history, label="x1")
plt.plot(x2_history, label="x2")
plt.xlabel("Gerações")
plt.ylabel("Valores de x1 e x2")
plt.title("Evolução de x1 e x2")
plt.legend()

plt.tight_layout()
plt.show()
