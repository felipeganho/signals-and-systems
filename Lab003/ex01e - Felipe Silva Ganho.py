#Felipe Silva Ganho
#Exercício 1 - Item E

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

#cria sinal especificado
def gera_sinal(N, periodo):
    x = []
    cont = 0
    for i in range(0, ((periodo * N))):
        if cont >= 1 and cont <= 4:
            x.append(1)
            cont += 1
        elif cont >= 5 and cont <= 8:
            x.append(-1)
            cont += 1
        else:
            x.append(0)
            cont = 1

    return x

#calcula DTFS
def realiza_DTFS(x):
  return fft(x)/len(x)

#deslocamento do sinal
def desloca_sinal(X, w):
  return fftshift(X), fftshift(w)

#retorna sinal original
def retorna_sinal(X, x):
  return np.real(ifft(X)*len(x))

#período e quantidade de períodos
N, nper = 9, 2

#vetor de amostras
n = np.arange(0, nper * N)

#sinal x[n]
x = gera_sinal(N, nper)

#cálculo da DTFS
X = realiza_DTFS(x)

#vetor de frequência
w = fftfreq(len(n), d=1/N)

#posiciona frequência zero no meio do gráfico
Xd, w = desloca_sinal(X, w)

#obtém os espectros de magnitude e fase
ModX, phasX = np.abs(Xd), np.angle(Xd)

#operação realizada devido a erros de arredondamento, sendo necessário filtragem de sinais muito pequenos
phasX[ModX < 0.00001] = 0

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
