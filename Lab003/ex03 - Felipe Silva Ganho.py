#Felipe Silva Ganho
#Exercício 3

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from scipy import signal
from numpy.fft import fft, ifft, fftfreq, fftshift

#cria sinal especificado
def gera_sinal(t):
  return signal.sawtooth(1.3 * np.pi * t)*0.75 + 0.25

#calcula DTFS
def realiza_DTFS(x):
  return fft(x)/len(x)

#deslocamento do sinal
def desloca_sinal(X, w):
  return fftshift(X), fftshift(w)

#retorna sinal original
def retorna_sinal(X, x):
  return np.real(ifft(X)*len(x))

#definindo o sinal contínuo periódico
fs = 1            #frequência do sinal periódico
w0 = 2 * pi * fs  #frequência angular
Ts = 1/fs         #período fundamental do sinal
Tam = Ts/100   	  #período de amostragem 100 vezes menor que o período do sinal

#vetor de tempo com 5 períodos e intervalo de Tam
t = np.arange(0, Ts, Tam)

#vetor do sinal x[n]
x = gera_sinal(t)

#calculando a DTFS
X = realiza_DTFS(x)

#vetor de frequência
w = fftfreq(len(t), d=1/Ts)

#posiciona frequência zero no meio do gráfico
Xd, w = desloca_sinal(X, w)

#obtém os espectros de magnitude e fase
ModX, phasX = np.abs(Xd), np.angle(Xd)

#operação realizada devido a erros de arredondamento, sendo necessário filtragem de sinais muito pequenos
phasX[ModX < 0.00001] = 0

#retorna sinal no domínio do tempo
xr = retorna_sinal(X, x)

#gera gráfico dos espectros de magnitude e fase
fig, ax = plt.subplots(2, 1, figsize = (8,5))

ax[0].stem(w, ModX, use_line_collection=True)
ax[0].set_xlabel("k")
ax[0].set_ylabel("Amplitude")
ax[0].set_title('|X[k]|')
ax[0].grid(True)

ax[1].stem(w, phasX, use_line_collection=True)
ax[1].set_xlabel("k")
ax[1].set_ylabel("Amplitude")
ax[1].set_title('angle(X[k])')
ax[1].grid(True)

fig.tight_layout()
fig.set_size_inches(8, 5)
plt.show()