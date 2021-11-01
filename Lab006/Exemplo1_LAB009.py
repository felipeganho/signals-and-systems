import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from scipy.fft import fft, ifft, fftfreq, fftshift
import scipy as sc
from scipy import signal

def AnalisadorEspectro(x,t,N,Lfreq,titleTempo,titleFreq):
    # sinal x, vetor de tempo t
    # N - tamanho da fft
    # Lfreq - limite superior da frequencia
    # titletempo e titlefreq - title dos graficos do tempo e da freq.

    # calculando sua FT
    Tam = t[1]-t[0]
    X = fft(x, N)*Tam
    w = fftfreq(len(X), d=Tam)
    # Os indices de frequencia são mudados de 0 a N-1 para -N/2 + 1 a N/2
    # posicionando a freq. zero no meio do gráfico
    wd = fftshift(w)
    Xd = fftshift(X)

    # calculando o modulo - magnitude do espectro
    ModX = np.abs(Xd)

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(t, x, 'r-', lw=2, label="x(t)")
    ax[0].set_ylabel("Amplitude")
    ax[0].set_xlabel("tempo [s]")
    ax[0].grid(True)
    # ax[0].set_xlim(0,1 )
    ax[0].set_title(titleTempo)

    ax[1].plot(wd, ModX, 'c-', lw=2, label="|X(jw)|")
    ax[1].set_ylabel("Amplitude")
    ax[1].set_xlabel("Freq. [Hz]")
    ax[1].grid(True)
    if Lfreq != 0:
        ax[1].set_xlim(0, Lfreq)
    ax[1].set_title(titleFreq)
    # ax[1].set_yscale('symlog')
    fig.tight_layout()
    return ModX,wd


# definindo o sinal no tempo continuo
f = 100        # freq. do sinal contínuo
w0 = 2*pi*f    # frequencia angular
T  = 1/f       # período fundamental do sinal
Tamc = T/1008   # período de amostragem para representar o sinal continuo 1000 vezes menor que o período do sinal

# Criando o vetor de tempo, 5 períodos, e intervalo de Tamc
t = np.arange(0,T*6,Tamc)
x = 100*np.cos(w0*t)

Modx,wd = AnalisadorEspectro(x,t,2**18,1000,'x(t)','|X(jw)|')

# Fazendo a amostragem
Ts = T/10       # periodo do trem de impulso, periodo da amostragem
delta = sc.signal.unit_impulse(len(t), range(0, len(t),int(Ts/Tamc)))
AnalisadorEspectro(delta,t,2**18,2500,'delta(t) Ts ='+str(Ts),'|DELTA(jw)|')
# amostrando o sinal
xs1 = x * delta # sinal amostrado representado no dominio contínuo
Modx1,wd1 = AnalisadorEspectro(xs1,t,2**18,2500,'xs1(t) Ts = '+str(Ts),'|Xs1(jw)|')

# Fazendo a amostragem
Ts = T/4 # periodo do trem de impulso, periodo da amostragem
delta = sc.signal.unit_impulse(len(t), range(0, len(t),int(Ts/Tamc)))
AnalisadorEspectro(delta,t,2**18,1000,'delta(t) Ts ='+str(Ts),'|DELTA(jw)|')
# amostrando o sinal
xs2 = x * delta
Modx2,wd2 = AnalisadorEspectro(xs2,t,2**18,1000,'xs2(t) Ts ='+str(Ts),'|Xs2(jw)|')

# Fazendo a amostragem
Ts = T/1.25 # periodo do trem de impulso, periodo da amostragem
delta = sc.signal.unit_impulse(len(t), range(0, len(t),int(Ts/Tamc)))
AnalisadorEspectro(delta,t,2**18,500,'delta(t) Ts ='+str(Ts),'|DELTA(jw)|')
# amostrando o sinal
xs3 = x * delta
Modx3,wd3 = AnalisadorEspectro(xs3,t,2**18,500,'xs3(t) Ts ='+str(Ts),'|Xs3(jw)|')


#Juntando todos os graficos juntos para omparação

fig1, ax1 = plt.subplots()
ax1.plot(t, x, 'c-', lw=2, label="x(t)")
ax1.plot(t, xs1, 'y-x', lw=1, label="xs1(t)")
ax1.plot(t, xs2, 'g-o', lw=1, label="xs2(t)")
ax1.plot(t, xs3, 'r*', lw=1, label="xs3(t)")
ax1.set_ylabel("Amplitude")
ax1.set_xlabel("tempo [s]")
ax1.grid(True)
ax1.legend()
ax1.set_xlim(0,0.025)
ax1.set_title('x(t)')


Modx = Modx/max(Modx)
Modx1 = Modx1/max(Modx1)
Modx2 = Modx2/max(Modx2)
Modx3 = Modx3/max(Modx3)

fig2, ax2 = plt.subplots()
ax2.plot(wd, Modx1, 'y-x', lw=1, label="|Xs1(jw)|")
ax2.plot(wd, Modx2, 'g-o', lw=1, label="|Xs2(jw)|")
ax2.plot(wd, Modx3, 'r-*', lw=1, label="|Xs3(jw)|")
ax2.plot(wd, Modx, 'c-', lw=4, label="|X(jw)|")
ax2.set_ylabel("Amplitude")
ax2.set_xlabel("Freq. [Hz]")
ax2.grid(True)
ax2.legend()
ax2.set_xlim(0,300)
ax2.set_title('|X(jw)| normalizado')
plt.legend(loc='upper right')


plt.show()
