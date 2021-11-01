#Felipe Silva Ganho
#Exercício 2 - D

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

#função de trem de impulso
def trem_impulso(t, Tam):
    trem_impulso = np.arange(t[0], (t[-1] + t[1] - t[0]), t[1] - t[0])

    for i in range(len(trem_impulso)):
        if (t[i] % Tam != 0):
            trem_impulso[i] = 0
        else:
            trem_impulso[i] = 1

    return trem_impulso

#frequência de amostragem
w_amp = 2
tam = (2 * np.pi) / w_amp
t = np.arange(-20, 20 + tam/np.pi, tam/np.pi)

#sinal x4(t)
x4 = trem_impulso(t, 10)

#N - tamanho da DTFS
N = np.power(2, 12)

#calculando a FT
X = (tam * N) * fft(x4, N) / N

#vetor de frequência
w = fftfreq(len(X), d=(tam)) * (2 * np.pi)

#índices de frequência mudados de 0 a N-1 para -N/2 + 1 a N/2
#posicionando a frequência zero no meio do gráfico
wd, Xd = fftshift(w), fftshift(X)

#calculando módulo e fase do sinal
ModX, phasX = np.abs(Xd), np.angle(Xd)

#sinal no tempo
fig, ax = plt.subplots(3,1)
ax[0].stem(t, x4, 'c-', label="", use_line_collection=True)
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("t")
ax[0].set_title('x4(t)')
ax[0].grid(True)

#módulo do sinal
ax[1].plot(wd, ModX, 'r-',linewidth=2, label="")
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("rad/s")
ax[1].set_title('Magnitude')
ax[1].grid(True)

#fase do sinal
ax[2].stem(wd, phasX, 'g-', label="", use_line_collection=True)
ax[2].set_ylabel("Amplitude")
ax[2].set_xlabel("rad/s")
ax[2].set_title('Fase da FT')
ax[2].grid(True)

plt.tight_layout()
plt.show()