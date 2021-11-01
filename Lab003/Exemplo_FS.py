import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft, fftfreq, fftshift

# definindo o sinal continuo periódico
fs = 100        # freq. do sinal periódico
w0 = 2*pi*fs    # frequencia angular
Ts = 1/fs       # período fundamental do sinal
Tam = Ts/100   	# período de amostragem 100 vezes menor que o período do sinal

# Criando o vetor de tempo,5 períodos, e intervalo de Tam
t = np.arange(0,Ts*5,Tam)
# criando x(t)
x = 1 + np.sin(w0*t)+2*np.cos(w0*t)+np.cos( (2*w0*t)+ pi/4 )

# calculando a FS
X = fft(x)/len(x)

#criando o vetor de frequencia
w = fftfreq(len(t), d=(1/Ts)*Tam)

# Os indices de frequencia são mudados de 0 a N-1 para (-N/2 + 1) a (N/2)
# posicionando a freq. zero no meio do gráfico
Xd = fftshift(X)
wd = fftshift(w)

# calculando o modulo - magnitude do espectro
ModX = np.abs(Xd)
# calculando a fase do espectro
phasX = np.angle(Xd)

# devido a erros de arredondamentos numericos da fft devemos filtrar os sinais muito pequenos!
phasX[ModX < 0.00001] = 0 # cuidado com isso aqui, isso depende do previo conhecimento do sinal

# retornando o sinal ao dominio do tempo
xr = ifft(X)*len(x)

xr = np.real(xr) # ignorando os erros de arrendondamento do fft e ifft

fig, ax1 = plt.subplots(2,1)
ax1[0].plot(t,x, 'c-', linewidth=2 , label="x(t)")
ax1[0].set_ylabel("Amplitude")
ax1[0].set_xlabel("tempo [s]")
ax1[0].grid(True)
ax1[0].set_title('x[n] - Original')

ax1[1].plot(t,xr, 'c-', linewidth=2, label="xr(t)")
ax1[1].set_ylabel("Amplitude")
ax1[1].set_xlabel("tempo [s]")
ax1[1].grid(True)
ax1[1].set_title('x(t) - Recuperado')


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
