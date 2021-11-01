import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft, fftfreq, fftshift

# gerando os sinais
L = 256
Ts = 0.01
t = np.arange(0,L,Ts)

# sinais amostrados
x1 = 5**(-2*t)
x2 = np.cos(2*pi*20*t)

X1 = Ts*fft(x1)
X2 = Ts*fft(x2)

w = fftfreq(len(X1), d=1.0)*(2*pi)
wdr = fftshift(w/Ts) #[rad/s]
wdh = fftshift(w/(2*pi*Ts)) #[Hz]

# calculando o modulo - magnitude do espectro
X1d = fftshift(X1)
ModX1 = np.abs(X1d)
phasX1 = np.angle(X1d)

X2d = fftshift(X2)
ModX2 = np.abs(X2d)
phasX2 = np.angle(X2d)

phasX2[ModX2 < 0.00001] = 0

fig1, ax1 = plt.subplots(3,1)
ax1[0].stem(t, x1, 'c-', label="x1[n]=x1(nTs)")
ax1[0].set_ylabel("Amplitude")
ax1[0].set_xlabel("nTs [s]")
ax1[0].grid(True)
ax1[0].set_xlim(0, 1)
ax1[0].set_title('x1[n]=x1(nTs)')

ax1[1].plot(wdr, ModX1, 'c-', linewidth=2, label="|X1[k]|")
ax1[1].set_ylabel("Amplitude")
ax1[1].set_xlabel("[rad/s]")
ax1[1].grid(True)
ax1[1].set_xlim(-200, 200)
ax1[1].set_title('|X1[k]|')

ax1[2].plot(wdr, phasX1, 'c-', linewidth=2, label="angle(X1[k])")
ax1[2].set_ylabel("Amplitude")
ax1[2].set_xlabel("[rad/s]")
ax1[2].grid(True)
ax1[2].set_xlim(-200, 200)
ax1[2].set_title('angle(X1[k])')

fig2, ax2 = plt.subplots(3,1)
ax2[0].stem(t, x2, 'c-', label="x2[n]=x2(nTs)")
ax2[0].set_ylabel("Amplitude")
ax2[0].set_xlabel("nTs [s]")
ax2[0].grid(True)
ax2[0].set_xlim(0, 1)
ax2[0].set_title('x2[n]=x2(nTs)')

ax2[1].plot(wdh, ModX2, 'c-', linewidth=2, label="|X2[k]|")
ax2[1].set_ylabel("Amplitude")
ax2[1].set_xlabel("[Hz]")
ax2[1].grid(True)
ax2[1].set_xlim(-35, 35)
ax2[1].set_title('|X2[k]|')

ax2[2].plot(wdh, phasX2, 'c-', linewidth=2, label="angle(X2[k])")
ax2[2].set_ylabel("Amplitude")
ax2[2].set_xlabel("[Hz]")
ax2[2].grid(True)
ax2[2].set_xlim(-35, 35)
ax2[2].set_title('angle(X2[k])')


fig1.tight_layout()
fig2.tight_layout()
plt.show()


