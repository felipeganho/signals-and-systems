import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft, fftfreq, fftshift


# criando o vetor de amostra com tamanho nper  periodos do sinal
N = 24 # periodo do sinal
nper = 2 # quantidade de periodos em x[n]
n = np.arange(0,nper*N)

#criando o vetor do sinal x[n] = 1 + sen((pi/12)*n + (3*pi/8))
xp1 = np.ones(len(n))
x = xp1 + np.sin( ((pi/12)*n)+(3*pi/8) )

# calculando a DTFS
X = fft(x,N)/N

#criando o vetor de frequencia
w = fftfreq(len(X), d=1/N)

# Os indices de frequencia são mudados de 0 a N-1 para -N/2 + 1 a N/2
# posicionando a freq. zero no meio do gráfico
Xd = fftshift(X)
wd = fftshift(w)

# calculando o modulo - magnitude do espectro
ModX = np.abs(Xd)
# calculando a fase do espectro
phasX = np.angle(Xd)

# devido a erros de arredondamentos numericos da fft devemos filtrar os sinais muito pequenos!
phasX[ModX < 0.00001] = 0 #  cuidado com isso aqui, isso depende do previo conhecimento do sinal

# retornando o sinal ao dominio do tempo
xr = ifft(X,N)*N
for i in range(1,nper):
    xr = np.append(xr,xr)

nr = np.arange(0,N*nper)
xr = np.real(xr) # ignorando os erros de arrendondamento do fft e ifft

fig, ax1 = plt.subplots(2,1)
ax1[0].stem(n,x, 'c-', label="x[n]")
ax1[0].set_ylabel("Amplitude")
ax1[0].set_xlabel("amostras")
ax1[0].grid(True)
ax1[0].set_title('x[n] - Original - Quantidade de Periodos ='+str(nper))

ax1[1].stem(nr,xr, 'c-', label="xr[n]")
ax1[1].set_ylabel("Amplitude")
ax1[1].set_xlabel("amostras")
ax1[1].grid(True)
ax1[1].set_title('x[n] - Recuperado')


fig1, ax = plt.subplots(2, 1)
ax[0].stem(wd,ModX, 'c-', label="|X[K]|")
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("k")
ax[0].grid(True)
ax[0].set_title('|X[k]|')

ax[1].stem(wd,phasX, 'c-', label="angle(X[k])")
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("k")
ax[1].grid(True)
ax[1].set_title('angle(X[k])')

fig.tight_layout()
fig1.tight_layout()

plt.show()
