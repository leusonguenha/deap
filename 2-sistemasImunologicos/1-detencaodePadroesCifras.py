import random
import string

# Função para gerar uma chave de substituição aleatória
def generate_key():
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    return ''.join(alphabet)

# Função para cifrar uma mensagem usando uma chave
def encrypt(message, key):
    alphabet = string.ascii_lowercase
    return ''.join(key[alphabet.index(c)] if c in alphabet else c for c in message)

# Função para decifrar uma mensagem usando uma chave
def decrypt(encrypted_message, key):
    alphabet = string.ascii_lowercase
    return ''.join(alphabet[key.index(c)] if c in key else c for c in encrypted_message)

# Função de fitness: quantas letras correspondem à original
def fitness(key, message, original_message):
    decrypted_message = decrypt(message, key)
    return sum(1 for a, b in zip(decrypted_message, original_message) if a == b)

# Algoritmo genético para detectar a chave
def genetic_algorithm(original_message, encrypted_message, population_size=100, generations=1000):
    population = [generate_key() for _ in range(population_size)]
    
    for _ in range(generations):
        population.sort(key=lambda k: -fitness(k, encrypted_message, original_message))
        if fitness(population[0], encrypted_message, original_message) == len(original_message):
            return population[0]  # A chave foi encontrada
        
        # Reproduzir
        next_generation = population[:10]  # Top 10 para reprodução
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:20], 2)
            child = ''.join(random.choice([p1, p2]) for p1, p2 in zip(parent1, parent2))
            next_generation.append(child)
        
        population = next_generation
    
    return population[0]  # Melhor chave após gerações

# Exemplo de uso
original_msg = "hello"
key = generate_key()
encrypted_msg = encrypt(original_msg, key)

detected_key = genetic_algorithm(original_msg, encrypted_msg)
print(f"Chave detectada: {detected_key}")
