#Felipe Silva Ganho
#Exercício 1

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

#gera função rampa
def rampa(t, to):
    rampa = np.arange(t[0], t[-1] + t[1] - t[0], t[1] - t[0])

    j = 0
    for i in range(len(rampa)):
        if (to > rampa[i]):
            rampa[i] = 0
        else:
            rampa[i] = j
            j = j + (t[1] - t[0])

    return rampa

#frequência máxima do sinal
wam = 1000

#taxa de amostragem
tam = (2 * np.pi) / wam

#vetor de tempo
t = np.arange(-10, 10 + tam, tam)

#sinal x(t)
x = 0.2 * (rampa(t, -5) - 2 * rampa(t, 0) + rampa(t, 5))

#sinal p(t)
p = np.cos(10 * t)

#sinal y(t)
y = p * x

#N - tamanho da DTFS
N = np.power(2, 16)

#calculando a FT
X = ((tam * N) * fft(x, N)) / N
Y = (tam * N) * fft(y, N) / N

#vetor de frequência
w = fftfreq(len(X), d=(tam)) * (2 * np.pi)

#índices de frequência mudados de 0 a N-1 para -N/2 + 1 a N/2
#posicionando a frequência zero no meio do gráfico
wd, Xd, Yd = fftshift(w), fftshift(X), fftshift(Y)

#módulo - magnitude do espectro
ModX = np.abs(Xd)
ModY = np.abs(Yd)

#gera gráficos
#gráficos do item A
fig, ax = plt.subplots(2, 1)
ax[0].plot(t, x, linewidth=2)
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("t")
ax[0].grid(True)
ax[0].set_title('x(t)')

ax[1].plot(wd, ModX, linewidth=2)
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("rad/s")
ax[1].set_xlim(-10, 10)
ax[1].grid(True)
ax[1].set_title('|X(e^jw)|')

#gráficos do item B
fig1, ax1 = plt.subplots(2, 1)
ax1[0].plot(t, y, linewidth=2)
ax1[0].set_ylabel("Amplitude")
ax1[0].set_xlabel("t")
ax1[0].set_xlim(-7.5, 7.5)
ax1[0].grid(True)
ax1[0].set_title('y(t)')

ax1[1].plot(wd, ModY, linewidth=2)
ax1[1].set_ylabel("Amplitude")
ax1[1].set_xlabel("rad/s")
ax1[1].set_xlim(-20, 20)
ax1[1].grid(True)
ax1[1].set_title('|Y(e^jw)|')

fig.tight_layout()
fig1.tight_layout()
plt.show()