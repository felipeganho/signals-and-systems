#Felipe Silva Ganho
#Exercício 2 - C

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

#frequência de amostragem
w_amp = 120 * 350
tam = (2 * np.pi) / w_amp
t = np.arange(-0.7, 0.7 + tam, tam)

#sinal x3(t)
x = np.sin(350 * t)

#N - tamanho da DTFS
N = np.power(2, 12)

#calculando a FT
X = (tam * N) * fft(x, N) / N

#vetor de frequência
w = fftfreq(len(X), d=(tam)) * (2 * np.pi)

#índices de frequência mudados de 0 a N-1 para -N/2 + 1 a N/2
#posicionando a frequência zero no meio do gráfico
wd, Xd = fftshift(w), fftshift(X)

#calculando módulo e fase
ModX, phasX = np.abs(Xd), np.angle(Xd)

#sinal no tempo
fig, ax = plt.subplots(3, 1)
ax[0].plot(t, x, 'c-', linewidth=2, label="")
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("t")
ax[0].set_xlim(-0.40, 0.40)
ax[0].set_title('x3(t)')
ax[0].grid(True)

#módulo do sinal
ax[1].plot(wd, ModX, 'r-',linewidth=2, label="")
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("rad/s")
ax[1].set_xlim(-450, 450)
ax[1].set_title('Magnitude')
ax[1].grid(True)

#fase do sinal
ax[2].stem(wd, phasX, 'g-', label="", use_line_collection=True)
ax[2].set_ylabel("Amplitude")
ax[2].set_xlabel("rad/s")
ax[2].set_xlim(-450, 450)
ax[2].set_title('Fase da FT')
ax[2].grid(True)

plt.tight_layout()
plt.show()