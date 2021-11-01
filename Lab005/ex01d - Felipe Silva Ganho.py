#Felipe Silva Ganho
#Exercício 1 - Item D

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

def sinal(n):
    x = []

    for i in n:
        x.append(np.power(0.9 * np.exp(1j * (np.pi / 3)), i)) if i >= 0 else x.append(0)

    return x

#gerando os sinais
L = 256
n = np.arange(0, L)

#sinal x[n]
x = sinal(n)

X = fft(x)

#vetor de frequência
w = fftfreq(len(X), d=1.0) * (2 * np.pi)

wd = fftshift(w / np.pi)
Xd = fftshift(X)

#módulo e fase
ModX, phasX = np.abs(Xd), np.angle(Xd)

#gráficos
fig1, ax = plt.subplots(3, 1)
ax[0].stem(n, x, 'r-', use_line_collection=True)
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("n")
ax[0].set_xlim(-2, 40)
ax[0].set_title('x[n]')

ax[1].plot(wd, ModX, 'g-', linewidth=2)
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("w/pi")
ax[1].set_title('|X[k]|')

ax[2].plot(wd, phasX, 'b-', linewidth=2)
ax[2].set_ylabel("Amplitude")
ax[2].set_xlabel("w/pi")
ax[2].set_title('angle(X[k])')

fig1.tight_layout()
plt.show()