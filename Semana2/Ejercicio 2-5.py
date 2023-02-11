#Grafico animado
import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp

x = np.linspace(0, 1, 50)
t = np.linspace(0, 1, 20)
X, T = np.meshgrid(x, t)
Y = np.sin(2*np.pi*(X+T))
timeline = amp.Timeline(t, units='s', fps=60)


block = amp.blocks.Line(X, Y, marker=".", linestyle="-", color="b")
anim = amp.Animation([block],timeline)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("y")

anim.save_gif('graph_anim.gif')
anim.controls()

plt.show()