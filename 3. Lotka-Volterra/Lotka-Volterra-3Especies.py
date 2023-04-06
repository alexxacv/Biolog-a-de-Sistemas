#Modelo de Lotka Volterra con tres especies, donde la especie "x" es depredadora de la "y" y la "y" es depredadora de la "z":

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# Definimos las ecuaciones diferenciales del modelo 
def lotka_volterra(t, y, a, b, c, d, e, f, g, h, i):
    x, y, z = y
    dxdt = a*x - b*x*y
    dydt = c*x*y - d*y - e*y*z
    dzdt = f*y*z - g*z - h*x*z
    return [dxdt, dydt, dzdt]

# Definimos los parámetros del modelo
a = 1.5   # Tasa de crecimiento de la especie x
b = 1.0   # Tasa de mortalidad de la especie x por la especie y
c = 3.0   # Tasa de crecimiento de la especie y por la especie x
d = 1.0   # Tasa de mortalidad de la especie y
e = 1.5   # Tasa de mortalidad de la especie y por la especie z
f = 3.0   # Tasa de crecimiento de la especie z por la especie y
g = 1.0   # Tasa de mortalidad de la especie z
h = 1.5   # Tasa de mortalidad de la especie x por la especie z
i = 1.0   # Tasa de mortalidad de la especie x

# Definimos las condiciones iniciales para el modelo
x0 = 10.0  # Población inicial de la especie x
y0 = 2.0   # Población inicial de la especie y
z0 = 5.0   # Población inicial de la especie z
y_init = [x0, y0, z0]

# Definimos el tiempo de la simulación del modelo
t0 = 0.0   # Tiempo inicial
tf = 50.0  # Tiempo final
t_eval = np.linspace(t0, tf, 1000)  # Es el vector de tiempo para evaluar la solución del modelo

# Resolvemos las ecuaciones diferenciales
sol = solve_ivp(lotka_volterra, [t0, tf], y_init, t_eval=t_eval, args=(a, b, c, d, e, f, g, h, i))

# Imprimir los resultados de las ecuaciones diferenciales
print(sol.y)

# Graficamos la solución
plt.plot(sol.t, sol.y[0], label='Especie x')
plt.plot(sol.t, sol.y[1], label='Especie y')
plt.plot(sol.t, sol.y[2], label='Especie z')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.legend()
plt.show()
