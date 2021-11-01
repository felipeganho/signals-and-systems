#Felipe Silva Ganho
#Exercício 2 - Item A

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

def sinal(t):
    x = []

    for i in t:
        x.append(100 * np.cos(2 * np.pi * 100 * i) * np.exp(-100 * i)) if i >= 0 else x.append(0)

    return x

#gerando os sinais
L = 256
Ts = 1 / 5000
t = np.arange(0, L, Ts)

#sinal x(t)
x1 = sinal(t)

X1 = Ts * fft(x1)

w = fftfreq(len(X1), d=1.0) * (2 * np.pi)

wdh = fftshift(w / (2 * np.pi * Ts))
X1d = fftshift(X1)

#calculando o modulo - magnitude do espectro
ModX1 = np.abs(X1d)
phasX1 = np.angle(X1d)

phasX1[ModX1 < 0.00001] = 0

fig1, ax = plt.subplots(3, 1)
ax[0].stem(t, x1, 'r-', use_line_collection=True)
ax[0].set_title('x1[n]=x1(nTs)')
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("nTs [s]")
ax[0].set_xlim(0, 0.04)

ax[1].plot(wdh, ModX1, 'g-', linewidth=2)
ax[1].set_title('|X1[k]|')
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("[Hz]")

ax[2].plot(wdh, phasX1, 'b-', linewidth=2)
ax[2].set_title('angle(X1[k])')
ax[2].set_ylabel("Amplitude")
ax[2].set_xlabel("[Hz]")

fig1.tight_layout()
plt.show()