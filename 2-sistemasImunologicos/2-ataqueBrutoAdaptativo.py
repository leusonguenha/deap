import itertools
import string

# Função para simular um ataque de força bruta
def brute_force_attack(target_hash, password_length, common_passwords):
    # Tenta senhas comuns primeiro
    for password in common_passwords:
        if hash_password(password) == target_hash:
            return password

    # Gera senhas de comprimento variável
    for length in range(1, password_length + 1):
        for guess in itertools.product(string.ascii_lowercase, repeat=length):
            guess_password = ''.join(guess)
            if hash_password(guess_password) == target_hash:
                return guess_password
    
    return None  

# Função para simular o hash da senha
def hash_password(password):
    return sum(ord(char) for char in password)  # Simplificação do hash

# Exemplo de uso
common_passwords = ["123456", "password", "12345678"]
target_password = "abc"
target_hash = hash_password(target_password)

found_password = brute_force_attack(target_hash, 3, common_passwords)
print(f"Senha encontrada: {found_password}")
