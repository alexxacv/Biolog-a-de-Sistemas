from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

def lac_derivatives(x, t, alpha, beta, K):
    m, p = x
    dxdt = [alpha/(1+p**K) - m,
            beta*m - p]
    return dxdt

alpha = 0.02  # Tasa de producción de ARNm
beta = 1.0    # Tasa de producción de proteína
K = 2.0       # Constante de Hill
x0 = [0.0, 0.0]  # Condiciones iniciales
t = np.linspace(0, 10, 100)  # Vector de tiempo

from scipy.integrate import odeint

sol = odeint(lac_derivatives, x0, t, args=(alpha, beta, K))

plt.figure()
plt.plot(t, sol[:, 0], label='mRNA')
plt.plot(t, sol[:, 1], label='Proteína')
plt.legend(loc='best')
plt.xlabel('Tiempo')
plt.ylabel('Concentración')
plt.title('Dinámica del operón lac')
plt.show()

