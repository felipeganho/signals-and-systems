#Felipe Silva Ganho
#Exercício 2 - Item B

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

#cria sinal especificado
def gera_sinal(n):
  return np.cos(((np.pi * 10)/21) * n) + (np.cos(((np.pi * 4)/21) * n)*1j)

#desloca sinal
def desloca_sinal(X):
  return fftshift(X)

#retorna sinal original
def retorna_sinal(X, x):
  return np.real(ifft(X)*len(x))

#período e quantidade de períodos do sinal
N, nper = 21, 1

#vetor de amostras
n = np.arange(0, nper * N)

#sinal x[n] = cos(((pi * 10)/21) * n) + (sin(((pi * 4)/21) * n)*1j)
X = gera_sinal(n)

#vetor de frequência
w = fftfreq(len(n), d=1/N)

#retorna sinal no domínio do tempo
xr = retorna_sinal(X, n)

#geral sinal no domínio do tempo
plt.figure(figsize=(8, 5))
plt.grid(True)
plt.stem(w, xr, use_line_collection=True)
plt.title('x[n] = cos(((pi * 10)/21) * n) + (sin(((pi * 4)/21) * n)*1j)')
plt.ylabel('Amplitude')
plt.xlabel('Amostra')
plt.show()