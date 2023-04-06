#Modelo Lotka-Volterra para dos especies presa-depredador

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# Primero se definen Definir las ecuaciones diferenciales del modelo 
def lotka_volterra(t, y, a, b, c, d):
    x, y = y
    dxdt = a*x - b*x*y
    dydt = c*x*y - d*y
    print(f"dx/dt={dxdt}, dy/dt={dydt}") #Esto imprime lo resultados de las E.D. en cada iteracción
    return [dxdt, dydt]

# Definimos los parámetros del modelo
a = 6.2   # Tasa de crecimiento de la presa
b = 3.0   # Tasa de mortalidad de la presa por los depredadores
c = 4.5   # Tasa de crecimiento de los depredadores por las presas
d = 2.0   # Tasa de mortalidad de los depredadores

# Definimos las condiciones iniciales
x0 = 20.0  # Población inicial de la presa
y0 = 2.0   # Población inicial del depredador
y_init = [x0, y0]

# Definimos el tiempo de simulación
t0 = 0.0   # Tiempo inicial
tf = 50.0  # Tiempo final
t_eval = np.linspace(t0, tf, 1000)  # Es el vector de tiempo para evaluar la solución

# Ahora se resuelven las ecuaciones diferenciales
sol = solve_ivp(lotka_volterra, [t0, tf], y_init, t_eval=t_eval, args=(a, b, c, d))



# Finalmente se Grafica la solución
plt.plot(sol.t, sol.y[0], label='Presa')
plt.plot(sol.t, sol.y[1], label='Depredador')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.legend()
plt.show()
