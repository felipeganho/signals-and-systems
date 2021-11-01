#Felipe Silva Ganho
#Exercício 2 - Item B

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
Ts = 1 / 1000
t = np.arange(0, L, Ts)

#sinal x(t)
x2 = sinal(t)

X2 = Ts * fft(x2)

w = fftfreq(len(X2), d=1.0) * (2 * np.pi)

wdh = fftshift(w / (2 * np.pi * Ts))
X2d = fftshift(X2)

#calculando o modulo - magnitude do espectro
ModX2 = np.abs(X2d)
phasX2 = np.angle(X2d)

phasX2[ModX2 < 0.00001] = 0

fig1, ax = plt.subplots(3, 1)
ax[0].stem(t, x2, 'r-', use_line_collection=True)
ax[0].set_title('x2[n]=x2(nTs)')
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("nTs [s]")
ax[0].set_xlim(0, 0.04)

ax[1].plot(wdh, ModX2, 'g-', linewidth=2)
ax[1].set_title('|X2[k]|')
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("[Hz]")

ax[2].plot(wdh, phasX2, 'b-', linewidth=2)
ax[2].set_title('angle(X2[k])')
ax[2].set_ylabel("Amplitude")
ax[2].set_xlabel("[Hz]")

fig1.tight_layout()
plt.show()