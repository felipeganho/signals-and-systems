#Felipe Silva Ganho

import numpy as np
import matplotlib.pyplot as plt

#intervalo
n = np.arange(-10, 21, 1)

#sinal x1
#x1[n] = cos(pi/6 * n);
x1 = np.cos(np.pi/6 * n)

#sinal x1 deslocado
x1_desloc = np.cos((np.pi/6) * (n-4))

#mudando a escala de x1
x1_deslocEscala = (0.9 * x1_desloc)

#item A
#sinal de saída y1
y1 = x1 + x1_deslocEscala

#sinal x2
#x2[n] = cos(pi/6 * n);
x2 = np.cos(np.pi/6 * n)
def sinalX2Deslocado(n):
    x2 = []

    for i in range(len(n)):
        if(n[i] >= -10 and n[i] <= 20):
            x2.append(np.cos(np.pi/6 * n[i]))
        else:
            x2.append(0)

    return x2

#sinal x2 deslocado
x2_desloc = sinalX2Deslocado(n-4)

#mudando a escala de x2
x2_deslocEscala = (list(map(lambda x: x * 0.9, x2_desloc)))

#item B
#sinal de saída y2
y2 = x2 + x2_deslocEscala

#x1 refletido
ny12 = np.arange(-20, 11, 1)
x1_refletido = np.cos(np.pi/6 * ny12)

#gera uma função degrau
def degrau(n):
  u = []

  for i in range(len(n)):
    u.append(1) if n[i] >= 0 else u.append(0)

  return u

#degrau deslocado
degrau_deslocCD = np.array(degrau(n+3))

#item C
y3 = x1_refletido * degrau_deslocCD

#x2 refletido
x2_refletido = np.array(sinalX2Deslocado(ny12))

#item D
y4 = x2_refletido * degrau_deslocCD

#degrau_deslocE
degrau_deslocE = degrau(n-5)

#item E
y5 = x1 * degrau_deslocE

degrau_deslocF5 = degrau(n-5)
degrau_deslocF10 = degrau(n-10)

def subtrai_degrau(u1, u2):
    u_total = []

    j = 0
    for i in range(-10, 21):
        subtrai = u1[j] - u2[j]
        u_total.append(subtrai)
        j += 1

    return u_total

degrauF = subtrai_degrau(degrau_deslocF5, degrau_deslocF10)

#item F
y6 = x1 * degrauF

#degrau deslocado item g
degrau_deslocG = degrau(n+1)

#item G
y7 = x1 + degrau_deslocG

#plotando os gráficos y1 e y2
figure, axis = plt.subplots(2)

#gráfico y1
axis[0].stem(n, y1)
axis[0].set_ylabel("Amplitude")
axis[0].set_xlabel("Amostras")
axis[0].set_title("y1[n] = x1[n] + 0.9x1[n-4]")

#gráfico y2
axis[1].stem(n, y2)
axis[1].set_ylabel("Amplitude")
axis[1].set_xlabel("Amostras")
axis[1].set_title("y2[n] = x2[n] + 0.9x2[n-4]")

plt.subplots_adjust(wspace=0.9, hspace=0.9)
plt.show()

#plotando os gráficos y3 e y4
figure1, axis = plt.subplots(2)

#gráfico y3
axis[0].stem(n, y3)
axis[0].set_ylabel("Amplitude")
axis[0].set_xlabel("Amostras")
axis[0].set_title("y3[n] = x1[-n]u[n+3]")

#gráfico y4
axis[1].stem(n, y4)
axis[1].set_ylabel("Amplitude")
axis[1].set_xlabel("Amostras")
axis[1].set_title("y4[n] = x2[-n]u[n+3]")

plt.subplots_adjust(wspace=0.9, hspace=0.9)
plt.show()

#plotando os gráficos y5, y6 e y7
figure2, axis = plt.subplots(3)

#gráfico y5
axis[0].stem(n, y5)
axis[0].set_ylabel("Amplitude")
axis[0].set_xlabel("Amostras")
axis[0].set_title("y5[n] = x1[n]u[n-5]")

#gráfico y6
axis[1].stem(n, y6)
axis[1].set_ylabel("Amplitude")
axis[1].set_xlabel("Amostras")
axis[1].set_title("y6[n] = x1[n]{u[n-5] - u[n-10]}")

#gráfico y7
axis[2].stem(n, y7)
axis[2].set_ylabel("Amplitude")
axis[2].set_xlabel("Amostras")
axis[2].set_title("y7[n] = x1[n] + u[n+1]")

plt.subplots_adjust(wspace=0.9, hspace=0.9)
plt.show()