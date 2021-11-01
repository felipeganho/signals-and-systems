#Felipe Silva Ganho
#Exercício 2 - B

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

#gera função degrau
def degrau(t, to):
    degrau = np.arange(t[0], (t[-1] + t[1] - t[0]), t[1] - t[0])

    for i in range(len(degrau)):
        if degrau[i] >= to:
            degrau[i] = 1
        else:
            degrau[i] = 0

    return degrau

#frequência e tempo
wamp = 300
tam = (2 * np.pi) / wamp
t = np.arange(0, 10 + tam, tam)

#sinal x2(t)
x2 = np.exp(-t) * degrau(t, 0)

#N - tamanho da DTFS
N = np.power(2, 12)

#calculando a FT
X = (tam * N) * fft(x2, N) / N

#vetor de frequência
w = fftfreq(len(X), d=(tam)) * (2 * np.pi)

#índices de frequência mudados de 0 a N-1 para -N/2 + 1 a N/2
#posicionando a frequência zero no meio do gráfico
wd, Xd = fftshift(w), fftshift(X)

#módulo e fase do sinal
ModX, phasX = np.abs(Xd), np.angle(Xd)

#sinal no tempo
fig, ax = plt.subplots(3, 1)
ax[0].plot(t, x2, linewidth=2, label="")
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("t")
ax[0].set_title('x2(t)')
ax[0].grid(True)

#módulo do sinal
ax[1].plot(wd, ModX, linewidth=2, label="")
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("rad/s")
ax[1].set_xlim(-50, 50)
ax[1].set_title('Magnitude')
ax[1].grid(True)

#fase do sinal
ax[2].stem(wd, phasX, label="", use_line_collection=True)
ax[2].set_ylabel("Amplitude")
ax[2].set_xlabel("rad/s")
ax[2].set_xlim(-10, 10)
ax[2].set_title('Fase da FT')
ax[2].grid(True)

plt.tight_layout()
plt.show()
