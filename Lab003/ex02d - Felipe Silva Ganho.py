#Felipe Silva Ganho
#Exercício 2 - Item D

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

#cria sinal especificado
def gera_sinal(N, nper):
    x = []

    cont = 0
    for i in np.arange(0, N * nper):
        if cont == 0:
            x.append(-0.5)
            cont += 1
        elif cont == 1:
            x.append(1)
            cont += 1
        elif cont == 6:
            x.append(1)
            cont = 0
        else:
            x.append(0)
            cont += 1

    return x

#desloca sinal
def desloca_sinal(X):
  return fftshift(X)

#retorna sinal original
def retorna_sinal(X, x):
  return np.real(ifft(X)*len(x))

#período do sinal
N, nper = 7, 1

#vetor de amostras
n = np.arange(0, N * nper)

#vetor de frequência
w = fftfreq(len(n), d=1/N)

#calcula sinal X
X = gera_sinal(N, nper)

#retorna sinal no domínio do tempo
xr = retorna_sinal(X, n)

#geral sinal no domínio do tempo
plt.figure(figsize=(8, 5))
plt.grid(True)
plt.stem(w, xr, use_line_collection=True)
plt.title('xr')
plt.ylabel('Amplitude')
plt.xlabel('Amostra')
plt.show()