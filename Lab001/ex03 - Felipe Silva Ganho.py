#Felipe Silva Ganho

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(0, 48, 48, endpoint=False) #tempo
x = (t * (np.pi/8)) #sinal

#gera sinal de onda quadrada
sinalOndaQuadrada = signal.square(x, 0.5)

plt.figure(figsize=(8, 5))
plt.stem(t, sinalOndaQuadrada)
plt.title('x[n] = square[n*pi/8]')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')

plt.show()
