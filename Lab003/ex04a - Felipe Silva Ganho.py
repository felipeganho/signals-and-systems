#Felipe Silva Ganho
#Exercício 4 - Item A

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, fftfreq, fftshift
import scipy as sc
from scipy import signal

#gera sinal de onda quadrada
def square(wt, duty=0.5):
    sq = sc.signal.square(wt, duty=duty)
    return sq

#sinal contínuo periódico
fs = 1                  #frequência do sinal periódico
w0 = 2 * pi * fs        #frequência angular
Ts = 1 / fs             #período fundamental do sinal
Tam = 1 / (100 * fs)    #período de amostragem 100 vezes menor que o período do sinal

#números de períodos do sinal
Np = 4

#tempo com 5 períodos e intervalo Tam
t = np.arange(0, Ts * Np, Tam)

#cria sinal de onda quadrada
s = 0.5 * square(w0 * t, duty=0.25) + 0.5

#cálculo da FS
X = (fft(s) / len(s))

#vetor de frequência
w = fftfreq(len(t), d=(1 / Ts) * Tam)

#deslocamento do sinal e do vetor de frequência
Xd = fftshift(X)
wd = fftshift(w)

#cálculo do módulo do sinal
ModX = np.abs(Xd)

#cálculo da fase do sinal
phaseX = np.angle(Xd)

#gera gráfico dos espectros de magnitude e fase
fig, ax = plt.subplots(2, 1, figsize = (8,5))

ax[0].stem(wd, ModX, use_line_collection=True)
ax[0].set_xlabel("t")
ax[0].set_ylabel("|X(t)|")
ax[0].set_title('Representação FS do modulo |X(k)| do sinal Vs(t)')
ax[0].grid(True)

ax[1].stem(wd, phaseX, use_line_collection=True)
ax[1].set_xlabel("t")
ax[1].set_ylabel("angle(X(t))")
ax[1].set_title('Representação FS do angulo angle(X(k)) sinal Vs(t)')
ax[1].grid(True)

fig.tight_layout()
fig.set_size_inches(8, 5)
plt.show()