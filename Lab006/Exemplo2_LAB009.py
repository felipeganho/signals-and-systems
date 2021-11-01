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
fmax = 66.5       # freq. máxima do sinal contínuo

T  = 1/fmax       # período fundamental do sinal
Tamc = T/1000   # período de amostragem para representar o sinal continuo 1000 vezes menor que o período do sinal


# Criando o vetor de tempo,3 períodos, e intervalo de Tam
t = np.arange(0,T*3,Tamc)

u0_005 = np.zeros(len(t))
u0_005[ t >= 0.005] = 1
u0_02 = np.zeros(len(t))
u0_02[t > 0.02 ] = 1

x = u0_005-u0_02



Modx,wd = AnalisadorEspectro(x,t,2**18,1000,'x(t)','|X(jw)|')

# Fazendo a amostragem
Ts = T/10       # periodo do trem de impulso
delta = sc.signal.unit_impulse(len(t), range(0, len(t),int(Ts/Tamc)))
AnalisadorEspectro(delta,t,2**18,3500,'delta(t) Ts ='+str(Ts),'|DELTA(jw)|')
# amostrando o sinal
xs1 = x * delta
Modx1,wd1 = AnalisadorEspectro(xs1,t,2**18,2500,'xs(t) Ts = '+str(Ts),'|Xs(jw)|')

Ts = T/4
delta = sc.signal.unit_impulse(len(t), range(0, len(t),int(Ts/Tamc)))
AnalisadorEspectro(delta,t,2**18,3500,'delta(t) Ts ='+str(Ts),'|DELTA(jw)|')
# amostrando o sinal
xs2 = x * delta
Modx2,wd2 = AnalisadorEspectro(xs2,t,2**18,1000,'xs(t) Ts ='+str(Ts),'|Xs(jw)|')


Ts = T/1.5
delta = sc.signal.unit_impulse(len(t), range(0, len(t),int(Ts/Tamc)))
AnalisadorEspectro(delta,t,2**18,200,'delta(t) Ts ='+str(Ts),'|DELTA(jw)|')
# amostrando o sinal
xs3 = x * delta
Modx3,wd3 = AnalisadorEspectro(xs3,t,2**18,0,'xs(t) Ts ='+str(Ts),'|Xs(jw)|')


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
ax2.set_xlabel("Frq. [Hz]")
ax2.grid(True)
ax2.legend()
ax2.set_xlim(0,300)
ax2.set_title('|X(jw)| normalizado')
plt.legend(loc='upper right')


plt.show()
