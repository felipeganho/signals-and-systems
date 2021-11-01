#Felipe Silva Ganho
#Exercício 2 - Item A

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import ifft, fftfreq

#cria sinal especificado
def gera_sinal(n):
  return np.cos(((np.pi * 6)/17) * n)

#retorna sinal original
def retorna_sinal(X, x):
  return np.real(ifft(X)*len(x))

#período do sinal
N = 17

#vetor de amostras
n = np.arange(0, N)

#sinal X[n] = cos(((pi * 6)/17) * n)
X = gera_sinal(n)

#vetor de frequência
w = fftfreq(len(n), d=1/N)

#retorna sinal no domínio do tempo
xr = retorna_sinal(X, n)

#geral sinal no domínio do tempo
plt.figure(figsize=(8, 5))
plt.grid(True)
plt.stem(w, xr, use_line_collection=True)
plt.title('x[n] = cos(((pi * 6)/17) * n)')
plt.ylabel('Amplitude')
plt.xlabel('Amostra')
plt.show()
