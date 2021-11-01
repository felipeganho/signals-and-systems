#Felipe Silva Ganho
#Exercício 4 - Item B

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, fftfreq, fftshift, ifft
import scipy as sc
from scipy import signal

#gera sinal de onda quadrada
def square(wt, duty=0.5):
    sq = sc.signal.square(wt, duty=duty)
    return sq

#retorna sinal original
def retorna_sinal(X, x):
  return np.real(ifft(X)*len(x))

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

#Item I
#valor de RC
RC = 0.01

#sinal H(jw)
H = (1/RC)/((1/RC) + 1j*w)

#sinal Y(t)
Y = X * H

#deslocamento dos sinais
Yd = fftshift(Y)
wd = fftshift(w)

#módulo e fase do sinal
ModY, phaseY = np.abs(Yd), np.angle(Yd)

#operação realizada devido a erros de arredondamento, sendo necessário filtragem de sinais muito pequenos
phaseY[ModY < 0.00001] = 0

#sinal no domínio do tempo
y = retorna_sinal(Y, s)

#gera gráfico do sinal, módulo e fase
fig, ax = plt.subplots(3, 1)

ax[0].stem(wd, ModY, use_line_collection=True)
ax[0].set_xlabel("t")
ax[0].set_ylabel("|Y(t)|")
ax[0].set_title('Representação |Y(t)| com RC=0.01s')

ax[1].stem(wd, phaseY, use_line_collection=True)
ax[1].set_xlabel("t")
ax[1].set_ylabel("angle(Y(t))")
ax[1].set_title('Representação angle(Y(t)) com RC=0.01s')

ax[2].stem(t, y, use_line_collection=True)
ax[2].set_xlabel("t")
ax[2].set_ylabel("y(t)")
ax[2].set_title('Representação do sinal y(t) com RC=0.01s')

fig.tight_layout()
plt.show()

#Item II
#valor de RC
RC = 0.1

#sinal H(jw)
H = (1 / RC) / ((1 / RC) + 1j * w)

#sinal Y(t)
Y = X * H

#deslocamento dos sinais
Yd = fftshift(Y)
wd = fftshift(w)

#módulo e fase do sinal
ModY, phaseY = np.abs(Yd), np.angle(Yd)

#operação realizada devido a erros de arredondamento, sendo necessário filtragem de sinais muito pequenos
phaseY[ModY < 0.00001] = 0

#sinal no domínio do tempo
y = retorna_sinal(Y, s)

#gera gráfico do sinal, módulo e fase
fig, ax = plt.subplots(3, 1)

ax[0].stem(wd, ModY, use_line_collection=True)
ax[0].set_xlabel("t")
ax[0].set_ylabel("|Y(t)|")
ax[0].set_title('Representação |Y(t)| com RC=0.1s')

ax[1].stem(wd, phaseY, use_line_collection=True)
ax[1].set_xlabel("t")
ax[1].set_ylabel("angle(Y(t))")
ax[1].set_title('Representação angle(Y(t)) com RC=0.1s')

ax[2].stem(t, y, use_line_collection=True)
ax[2].set_xlabel("t")
ax[2].set_ylabel("y(t)")
ax[2].set_title('Representação do sinal y(t) com RC=0.1s')

fig.tight_layout()
plt.show()

#Item III
#valor de RC
RC = 1

#sinal H(jw)
H = (1 / RC) / ((1 / RC) + 1j * w)

#sinal Y(t)
Y = X * H

#deslocamento dos sinais
Yd = fftshift(Y)
wd = fftshift(w)

#módulo e fase do sinal
ModY, phaseY = np.abs(Yd), np.angle(Yd)

#operação realizada devido a erros de arredondamento, sendo necessário filtragem de sinais muito pequenos
phaseY[ModY < 0.00001] = 0

#sinal no domínio do tempo
y = retorna_sinal(Y, s)

#gera gráfico do sinal, módulo e fase
fig, ax = plt.subplots(3, 1)

ax[0].stem(wd, ModY, use_line_collection=True)
ax[0].set_xlabel("t")
ax[0].set_ylabel("|Y(t)|")
ax[0].set_title('Representação |Y(t)| com RC=1s')

ax[1].stem(wd, phaseY, use_line_collection=True)
ax[1].set_xlabel("t")
ax[1].set_ylabel("angle(Y(t))")
ax[1].set_title('Representação angle(Y(t)) com RC=1s')

ax[2].stem(t, y, use_line_collection=True)
ax[2].set_xlabel("t")
ax[2].set_ylabel("y(t)")
ax[2].set_title('Representação do sinal y(t) com RC=1s')

fig.tight_layout()
plt.show()