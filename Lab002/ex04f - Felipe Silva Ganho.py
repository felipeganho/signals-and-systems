#Felipe Silva Ganho

#importação das bibliotecas úteis
import numpy as np
import matplotlib.pyplot as plt

#gera sinal h[n]
def sinal_h(n0, sinal):
  u = []

  for i in range(-2, 21):
    if i >= n0:
      u.append((np.sin((1/12)* np.pi * i)) * 1) if sinal == 1 else u.append((np.sin((1/12)* np.pi * i)) * -1)

    else:
      u.append((np.sin((1/12)* np.pi * i)) * 0)

  return u

#gera degrau
def degrau_normal():
  u = []

  for i in range(-2, 21):
    u.append(1) if i >= 0 else u.append(0)

  return u

#amostras
n = np.arange(-2, 21, 1)

#sinal h[n]
h = sinal_h(3, 1)

#sinal x[n]
x = degrau_normal()

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
ax[1].set_title('h[n] = sen[1/12 * pi * n]u[n-3]')

ax[2].stem(n, y, use_line_collection=True)
ax[2].set_xlabel("Amostras")
ax[2].set_ylabel("Amplitude")
ax[2].set_title('y[n] = x[n] * h[n]')

fig.tight_layout()
fig.set_size_inches(8, 5)
plt.show()