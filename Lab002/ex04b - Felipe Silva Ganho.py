#Felipe Silva Ganho

#importação das bibliotecas úteis
import numpy as np
import matplotlib.pyplot as plt

#gera impulso com deslocamento
def impulso(n0, sinal):
  imp = []

  for i in range(-2, 21):
    if i == n0:
      if sinal == 1:
        imp.append(1)
      else:
        imp.append(-1)
    else:
      imp.append(0)

  return imp

#realiza a subtração de dois impulsos
def subtrai_impulso(i_1, i_2):
  i_total = []

  j = 0
  for i in range(-2, 21):
    soma = i_1[j] + i_2[j]
    i_total.append(soma)
    j += 1

  return i_total

#gera um degrau
def degrau():
  u = []

  for i in range(-2, 21):
    u.append(1) if i >= 0 else u.append(0)

  return u

#amostras
n = np.arange(-2, 21, 1)

#impulso sem deslocamento
imp = impulso(0, 1)

#impulso com deslocamneto -1
imp_2 = impulso(1, 0)

#sinal h[n]
h = subtrai_impulso(imp, imp_2)

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
ax[1].set_title('h[n] = δ[n] - δ[n-1]')

ax[2].stem(n, y, use_line_collection=True)
ax[2].set_xlabel("Amostras")
ax[2].set_ylabel("Amplitude")
ax[2].set_title('y[n] = x[n] * h[n]')

fig.tight_layout()
fig.set_size_inches(8, 5)
plt.show()
