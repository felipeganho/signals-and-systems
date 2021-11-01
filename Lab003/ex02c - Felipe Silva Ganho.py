#Felipe Silva Ganho
#Exercício 2 - Item C

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

#módulo do sinal
def sinal_modulo(n):
  modulo = []

  for i in range(len(n)):
    if i == 3 or i == 4:
      modulo.append(1)
    else:
      modulo.append(0)

  return modulo

#fase do sinal
def sinal_fase(n):
  fase = []

  for i in range(len(n)):
    if i == 3:
      fase.append(-1)
    elif i == 4:
      fase.append(1)
    else:
      fase.append(0)

  return fase

#cria sinal especificado
def gera_sinal(modX, phasX):
    X = []

    for i in range(len(modX)):
        ret_x = modX[i] * np.cos(phasX[i] * (np.pi / 2))
        ret_y = modX[i] * np.sin(phasX[i] * (np.pi / 2))

        retangular = complex(ret_x, ret_y)

        X.append(retangular)
    return X

#retorna sinal original
def retorna_sinal(X, x):
  return np.real(ifft(X)*len(x))

#período do sinal
N = 7

#vetor de amostras
n = np.arange(0, N)

#vetor de frequência
w = fftfreq(len(n), d=1/N)

#calcula módulo e fase
ModX, phasX = sinal_modulo(n), sinal_fase(n)

#calcula sinal X
X = gera_sinal(ModX, phasX)

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