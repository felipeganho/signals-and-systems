#Felipe Silva Ganho

#importação das bibliotecas úteis
import numpy as np
import matplotlib.pyplot as plt

#gera degrau
def degrau(n0, sinal):
    u = []

    for i in range(-2, 21):
        if i >= n0:
            if sinal == 1:
                u.append(1)
            else:
                u.append(-1)
        else:
            u.append(0)

    return u

#realiza a subtração de dois degrais
def subtrai_degrau(u1, u2):
    u_total = []

    j = 0
    for i in range(-2, 21):
        soma = u1[j] + u2[j]
        u_total.append(((-1) ** j) * soma)
        j += 1

    return u_total

#amostras
n = np.arange(-2, 21, 1)

#degrau com deslocamento -2
u_2 = degrau(-2, 1)

#degrau com deslocamento -3
u_3 = degrau(3, 0)

#sinal h[n]
h = subtrai_degrau(u_2, u_3)

#sinal x[n]
x = degrau(0, 1)

#resposta y[n]
y = np.array(np.convolve(x, h)[:23])

#gera gráfico
fig, ax = plt.subplots(3, 1)

ax[0].stem(n, x, use_line_collection=True)
ax[0].set_xlabel("Amostras")
ax[0].set_ylabel("Amplitude")
ax[0].set_title('x[n] = u[n]')

ax[1].stem(n, h, use_line_collection=True)
ax[1].set_xlabel("Amostras")
ax[1].set_ylabel("Amplitude")
ax[1].set_title('h[n] = {(-1)**n}(u[n+2]-u[n-3]) ')

ax[2].stem(n, y, use_line_collection=True)
ax[2].set_xlabel("Amostras")
ax[2].set_ylabel("Amplitude")
ax[2].set_title('y[n] = x[n] * h[n]')

fig.tight_layout()
fig.set_size_inches(8, 5)
plt.show()
