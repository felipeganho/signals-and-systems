import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft, fftfreq, fftshift

# gerando os sinais
L = 256
n = np.arange(0,L)

# pulso
N = 20
x1 = np.ones(N)
x1 = np.append(x1,np.zeros(L-N))

# cossenoide Janelado
N = 200
n1 = np.arange(0,N)
x2 = np.cos((4*pi*n1)/N)
x2 = np.append(x2,np.zeros(L-N))

# chirpado
x3 = np.cos(pi*(n**2)/(4*L))

X1 = fft(x1)
X2 = fft(x2)
X3 = fft(x3)

w = fftfreq(len(X1), d=1.0)*(2*pi)
wd = fftshift(w/pi)

# calculando o modulo - magnitude do espectro
X1d = fftshift(X1)
ModX1 = np.abs(X1d)
phasX1 = np.angle(X1d)

X2d = fftshift(X2)
ModX2 = np.abs(X2d)
phasX2 = np.angle(X2d)

X3d = fftshift(X3)
ModX3 = np.abs(X3d)
phasX3 = np.angle(X3d)


fig1, ax1 = plt.subplots(3,1)
ax1[0].stem(n, x1, 'c-', label="x1[n]")
ax1[0].set_ylabel("Amplitude")
ax1[0].set_xlabel("amostras")
ax1[0].grid(True)
ax1[0].set_title('x1[n]')

ax1[1].plot(wd, ModX1, 'c-', linewidth=2, label="|X1[k]|")
ax1[1].set_ylabel("Amplitude")
ax1[1].set_xlabel("w/pi")
ax1[1].grid(True)
ax1[1].set_title('|X1[k]|')

ax1[2].plot(wd, phasX1, 'c-', linewidth=2, label="angle(X1[k])")
ax1[2].set_ylabel("Amplitude")
ax1[2].set_xlabel("w/pi")
ax1[2].grid(True)
ax1[2].set_title('angle(X1[k])')

fig2, ax2 = plt.subplots(3,1)
ax2[0].stem(n, x2, 'c-', label="x2[n]")
ax2[0].set_ylabel("Amplitude")
ax2[0].set_xlabel("amostras")
ax2[0].grid(True)
ax2[0].set_title('x2[n]')

ax2[1].plot(wd, ModX2, 'c-', linewidth=2, label="|X2[k]|")
ax2[1].set_ylabel("Amplitude")
ax2[1].set_xlabel("w/pi")
ax2[1].grid(True)
ax2[1].set_title('|X2[k]|')

ax2[2].plot(wd, phasX2, 'c-', linewidth=2, label="angle(X2[k])")
ax2[2].set_ylabel("Amplitude")
ax2[2].set_xlabel("w/pi")
ax2[2].grid(True)
ax2[2].set_title('angle(X2[k])')

fig3, ax3 = plt.subplots(3,1)
ax3[0].stem(n, x3, 'c-', label="x3[n]")
ax3[0].set_ylabel("Amplitude")
ax3[0].set_xlabel("amostras")
ax3[0].grid(True)
ax3[0].set_xlim(0, 100)
ax3[0].set_title('x3[n]')

ax3[1].plot(wd, ModX3, 'c-', linewidth=2, label="|X3[k]|")
ax3[1].set_ylabel("Amplitude")
ax3[1].set_xlabel("w/pi")
ax3[1].grid(True)
ax3[1].set_title('|X3[k]|')

ax3[2].plot(wd, phasX3, 'c-', linewidth=2, label="angle(X3[k])")
ax3[2].set_ylabel("Amplitude")
ax3[2].set_xlabel("w/pi")
ax3[2].grid(True)
ax3[2].set_title('angle(X3[k])')

fig1.tight_layout()
fig2.tight_layout()
fig3.tight_layout()
plt.show()


