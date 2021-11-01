#Felipe Silva Ganho

#importação das bibliotecas úteis
import numpy as np
import matplotlib.pyplot as plt

#gera degrau
def degrau():
    u = []

    for i in range(-10, 101):
        u.append(1) if i >= 0 else u.append(0)

    return u

#gera h[n]
def sinal_h(u):
    h = []

    j = 0
    for i in range(-10, 101):
        if i >= 0:
            h.append(((0.96 ** i) * np.sin(np.pi/16 * i)) * (u[j] - u[j - 10]))
            j = j + 1
        else:
            h.append(0)
            j += 1

    return h

#gera x[n]
def sinal_x(n0, sinal):
    u = []

    for i in range(-10, 101):
        if i >= n0:
            if sinal == 1:
                u.append(1)
            else:
                u.append(-1)
        else:
            u.append(0)

    return u

#degrau
u = degrau()

#sinal h[n]
h = sinal_h(u)

#sinal x[n]
x = sinal_x(2, 1)

#resposta y[n]
y = np.array(np.convolve(x, h)[:111])

#amostras
n = np.arange(-10, 101, 1)

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
fig.set_size_inches(8, 5)
plt.show()