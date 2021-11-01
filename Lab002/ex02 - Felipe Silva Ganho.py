#Felipe Silva Ganho

#importação das bibliotecas úteis
import numpy as np
import matplotlib.pyplot as plt

#gera função com ou sem deslocamento
def degrau(n, n0=0):
    n = n-n0
    u = np.array([])
    for i in n:
        if(i >= 0):
            u = np.append(u, 1)
        else:
            u = np.append(u, 0)
    return u

#amostras
n = np.arange(-10, 101, 1)

#sinal h[n]
h = degrau(n) - degrau(n, 10)

#sinal x[n]
x = degrau(n, 2) - degrau(n, 7)

#resposta y[n]
y = np.array(np.convolve(x, h)[:111])

#gera gráfico
fig, ax = plt.subplots(3, 1)

ax[0].stem(n, x, use_line_collection=True)
ax[0].set_xlabel("Amostras")
ax[0].set_ylabel("Amplitude")
ax[0].set_title('x[n]')

ax[1].stem(n, h, use_line_collection=True)
ax[1].set_xlabel("Amostras")
ax[1].set_ylabel("Amplitude")
ax[1].set_title('h[n]')

ax[2].stem(n, y, use_line_collection=True)
ax[2].set_xlabel("Amostras")
ax[2].set_ylabel("Amplitude")
ax[2].set_title('y[n] = x[n] * h[n]')

fig.tight_layout()
plt.show()