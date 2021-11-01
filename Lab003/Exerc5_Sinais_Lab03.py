import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft, fftfreq, fftshift
import scipy as sc
from scipy import signal

def square(wt, duty = 0.5):
    sq = sc.signal.square(wt, duty=duty )
    return sq

# definindo o sinal continuo periódico
fs = 1000        # freq. do sinal periódico
w0 = 2*pi*fs    # frequencia angular
Ts = 1/fs       # período fundamental do sinal
Tam = 1/(100*fs)   	# período de amostragem 100 vezes menor que o período do sinal

Np = 30          # quantidade de periodos no vetor do sinal
# Criando o vetor de tempo,5 períodos, e intervalo de Tam
t = np.arange(0,Ts*Np,Tam)
# criando x(t)
s = 2.5*square(w0*t,duty = 0.50)

frand = np.random.rand(2)   # fase aleatoria para as variaveis do sinal ns(t)
Vfrq = (1+np.cos(200*t+(pi*frand[0]) ))*(100/2)
Vdc = (1+np.cos(200*t+(pi*frand[1])))*(5/2)
ns = Vdc + 2.5*np.cos(2*pi*Vfrq*t)

x = s + ns

fig0, ax0 = plt.subplots(3,1)
ax0[0].plot(t, s, 'c-', lw=2,  label="s(t)")
ax0[0].set_ylabel("Amplitude")
ax0[0].set_xlabel("tempo [s]")
ax0[0].grid(True)
# ax0[0].legend()
ax0[0].set_title('s(t)')

ax0[1].plot(t, ns, 'r-',lw=2,  label="ns(t)")
ax0[1].set_ylabel("Amplitude")
ax0[1].set_xlabel("tempo [s]")
ax0[1].grid(True)
# ax0[1].legend()
ax0[1].set_title('ns(t)')

ax0[2].plot(t, x, 'r-',lw=2,  label="x[t]=s[t]+N(t)")
ax0[2].set_ylabel("Amplitude")
ax0[2].set_xlabel("tempo [s]")
ax0[2].grid(True)
# ax0[2].legend()
ax0[2].set_title('x(t)=s(t)+ns(t)')


#criando o vetor de frequencia
w = fftfreq(len(t), d=(1/Ts)*Tam)

# calculando a FS dos sinais envolvidos
X = fft(x)/len(x)
S = fft(s)/len(x)
N = fft(ns)/len(x)

# calculando o modulo - magnitude do espectro
ModX = np.abs(X)
ModS = np.abs(S)
ModN = np.abs(N)

# plotando a magnitude dos sinais envolvidos
fig1, ax1 = plt.subplots(3, 1)
ax1[0].stem(w,ModS, 'c*', label="|S[K]|")
ax1[0].set_ylabel("Amplitude")
ax1[0].set_xlabel("k")
ax1[0].grid(True)
#ax1[0].set_xlim(-25, 25)
ax1[0].set_title('|S[K]|')

ax1[1].stem(w,ModN, 'c-', label="|N[K]|")
ax1[1].set_ylabel("Amplitude")
ax1[1].set_xlabel("k")
ax1[1].grid(True)
ax1[1].set_xlim(-2, 2)
ax1[1].set_title('|N[K]|')

ax1[2].stem(w,ModX, 'c-', label="|X[K]|")
ax1[2].set_ylabel("Amplitude")
ax1[2].set_xlabel("k")
ax1[2].grid(True)
# ax1[2].set_xlim(-2, 2)
ax1[2].set_title('|X[k]|')

fig0.tight_layout()
fig1.tight_layout()

plt.show()
