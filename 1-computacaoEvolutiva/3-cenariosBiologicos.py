import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do modelo
K = 100  # Capacidade de suporte
P0 = 10  # População inicial
r = 0.2  # Taxa de crescimento
time = np.linspace(0, 50, 200)  # Intervalo de tempo

# Função de crescimento logístico
def logistic_growth(t, K, P0, r):
    return K / (1 + ((K - P0) / P0) * np.exp(-r * t))

# Calcular população ao longo do tempo
population = logistic_growth(time, K, P0, r)

# Visualizar
plt.plot(time, population, label='Crescimento Logístico')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.title('Simulação de Crescimento Populacional (Modelo Logístico)')
plt.legend()
plt.show()
