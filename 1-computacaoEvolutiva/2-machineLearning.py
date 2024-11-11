from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Gerar dados
np.random.seed(0)
x = np.random.rand(100, 1) * 10  # Valores de x entre 0 e 10
y = 2 * x + 3 + np.random.randn(100, 1)  # y = 2x + 3 + ruído

# Treinar o modelo de regressão linear
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

# Visualizar
plt.scatter(x, y, color='blue', label='Dados')
plt.plot(x, y_pred, color='red', label='Regressão Linear')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Regressão Linear Simples')
plt.show()
