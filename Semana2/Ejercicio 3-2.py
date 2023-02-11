import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
alumnos = {'Jicela Lopez': 7.1, 'Victor Colorado': 8.2,'Jorge Quiroga': 9.3}

ax.bar(alumnos.keys(), alumnos.values(), color='gray', align="center")
plt.title("Calificaciones Grupo 41C")

plt.show()