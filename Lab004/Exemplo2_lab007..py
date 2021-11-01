import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft, fftfreq, fftshift


# Criando o vetor de tempo
# Frequencia de amostragem
wam = 10*100 # 10 é a freq. máx do sinal
Tam = (2*pi)/wam
t = np.arange(-5,5,Tam)

x = np.exp(-1*np.abs(t))*np.cos(10*t)

# N - tamanho da DTFS
N = 2**12

# calculando a FT
X = (Tam*N)*fft(x,N)/N

# imprimindo os parametros
print(" M = " + str(len(x)))
print(" N = " + str(N))
print(" Tam = "+ str(Tam))

#criando o vetor de frequencia
w = fftfreq(len(X), d=(Tam))*(2*pi)

# Os indices de frequencia são mudados de 0 a N-1 para -N/2 + 1 a N/2
# posicionando a freq. zero no meio do gráfico
wd = fftshift(w)
Xd = fftshift(X)

# calculando o modulo - magnitude do espectro
ModX = np.abs(Xd)

fig, ax1 = plt.subplots()
ax1.plot(wd, ModX, 'r-', linewidth=1, label="y(t)")
ax1.set_ylabel("Amplitude")
ax1.set_xlabel("frequencia [rad/s]")
ax1.grid(True)
# ax1.legend()
ax1.set_xlim(-40, 40)
ax1.set_title('|X(e^jw)|')

fig1, ax = plt.subplots()
ax.plot(t, x, 'c-', linewidth=2, label="x(t)")
ax.set_ylabel("Amplitude")
ax.set_xlabel("tempo [s]")
ax.grid(True)
ax.set_title('x(t)')

plt.show()
