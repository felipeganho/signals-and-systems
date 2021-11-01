#Felipe Silva Ganho

#importação das bibliotecas úteis
import numpy as np
import matplotlib.pyplot as plt

#gera o degrau negativo
def degrau_negativo():
  u = []

  for i in range(-2, 21):
    u.append((-i) * 1) if i >= 0 else u.append(0)

  return u

#dera degrau
def degrau():
  u = []

  for i in range(-2, 21):
    u.append(1) if i >= 0 else u.append(0)

  return u

#amostras
n = np.arange(-2, 21, 1)

#sinal h[n]
h = degrau_negativo()

#sinal x[n]
x = degrau()

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
ax[1].set_title('h[n] = (-n)u[n]')

ax[2].stem(n, y, use_line_collection=True)
ax[2].set_xlabel("Amostras")
ax[2].set_ylabel("Amplitude")
ax[2].set_title('y[n] = x[n] * h[n]')

fig.tight_layout()
fig.set_size_inches(8, 5)
plt.show()
