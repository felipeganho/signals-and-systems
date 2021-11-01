#Felipe Silva Ganho

import numpy as np
import matplotlib.pyplot as plt

#letra A
tA = np.arange(-10, 11, 1)  #intervalo
xA = 2 * np.cos((np.pi/4) * tA)  #sinal

#letra B
tB = np.arange(-10, 10, 0.001) #intervalo
xB = 2 * np.cos((np.pi/4) * tB)  #sinal

#plotando o gráfico
figure, axis = plt.subplots(2)

#tempo discreto
axis[0].stem(tA, xA)
axis[0].set_ylabel("Amplitude")
axis[0].set_xlabel("Amostras")
axis[0].set_title("Sinal de tempo discreto")

#tempo contínuo
axis[1].plot(tB, xB)
axis[1].set_ylabel("Amplitude")
axis[1].set_xlabel("Tempo")
axis[1].set_title("Sinal de tempo contínuo")

plt.subplots_adjust(wspace=0.6, hspace=0.6)
plt.show()
