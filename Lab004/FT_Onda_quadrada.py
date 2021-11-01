import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft, fftfreq, fftshift
import scipy as sc
from scipy import signal

def square(wt, duty = 0.5):
    sq = sc.signal.square(wt, duty=duty )
    return sq


def FS(x, t, Ts, Tam):
    # calculando a Fs
    X = fft(x) / len(x)

    # criando o vetor de frequencia
    w = fftfreq(len(t), d=Tam)

    # Os indices de frequencia são mudados de 0 a N-1 para (-N/2 + 1) a (N/2)
    # posicionando a freq. zero no meio do gráfico
    Xd = fftshift(X)
    wd = fftshift(w)

    # calculando o modulo - magnitude do espectro
    ModX = np.abs(Xd)

    return ModX,wd


# definindo o sinal continuo periódico
fs = 1000        # freq. do sinal periódico
w0 = 2*pi*fs    # frequencia angular
Ts = 1/fs       # período fundamental do sinal
Tam = 1/(100*fs)   	# período de amostragem 100 vezes menor que o período do sinal

# Criando o vetor de tempo,5 períodos, e intervalo de Tam
tp = np.arange(-Ts/2,Ts/2,Tam)
# criando x(t)
s = ((square((w0*tp)+(pi/2),duty = 0.50))+1)/2
pz = np.zeros(len(s))

fig, ax = plt.subplots(3,2)
fig1, ax1 = plt.subplots(2,1)

id = 0
for Np in [1,4,100, 10000]:
    x = np.array(s)
    for npz in range(1,Np):
            x = np.append(x,pz)
    t = np.arange(0,Np*Ts,Tam)
    ModX,w = FS(x,t, Ts,Tam)

    if id < 3:
        ax[id][0].plot(t, x, 'c-', linewidth=2, label="x(t)")
        ax[id][0].set_ylabel("Amplitude")
        ax[id][0].set_xlabel("tempo [s]")
        ax[id][0].grid(True)
        ax[id][0].set_title('x(t) com T1/T = '+str(Ts/(Ts*Np)))

        ax[id][1].stem(w, ModX, 'c-', label="|X[K]|")
        ax[id][1].set_ylabel("Amplitude")
        ax[id][1].set_xlabel("k")
        ax[id][1].grid(True)
        ax[id][1].set_xlim(-5000, 5000)
        ax[id][1].set_title('|X[k]| com T1/T = ' + str(Ts/(Ts*Np)))
        id = id + 1
    else:
        ax1[0].plot(t, x, 'c-', linewidth=2, label="x(t)")
        ax1[0].set_ylabel("Amplitude")
        ax1[0].set_xlabel("tempo [s]")
        ax1[0].grid(True)
        ax1[0].set_title('x(t) com T1/T = ' + str(Ts / (Ts * Np)))

        ax1[1].plot(w, ModX, 'c-', label="|X[K]|")
        ax1[1].set_ylabel("Amplitude")
        ax1[1].set_xlabel("k")
        ax1[1].grid(True)
        ax1[1].set_xlim(-10000, 10000)
        ax1[1].set_title('|X[k]| com T1/T = ' + str(Ts / (Ts * Np)))

fig.tight_layout()
fig1.tight_layout()
plt.show()



