#Felipe Silva Ganho

#importação das bibliotecas úteis
import numpy as np
import matplotlib.pyplot as plt

#gera o sinal h[n]
def sinal_h():
    h = []

    for i in range(-2, 5):
        h.append(1) if i >= 0 and i <= 2 else h.append(0)

    return h

#gera o sinal x[n]
def sinal_x():
    x = []

    for i in range(-2, 5):
        if i == 0:
            x.append(0.5)

        elif i == 1:
            x.append(2)

        else:
            x.append(0)

    return x

#amostras
n = np.arange(-2, 5, 1)

#sinal x[n]
x = sinal_x()

#sinal h[n]
h = sinal_h()

#resposta y[n]
y = np.array(np.convolve(x, h)[:7])

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
ax[2].set_title('y[n]')

fig.tight_layout()
plt.show()