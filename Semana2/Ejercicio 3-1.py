import matplotlib.pyplot as plt
import numpy as np

ventas = np.array ([52004,13530,74758,45987,34576,80456,45678,23456,65432,55555])
años = np.array ([2012,2013,2014,2015,2016,2017,2018,2019,2020,2021])

plt.plot(años,ventas)

plt.show()