#Felipe Silva Ganho
#Exercício 2 - A

#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

#gera função degrau
def degrau(t, to):
    degrau = np.arange(t[0], (t[-1] + t[1] - t[0]), t[1] - t[0])

    for i in range(len(degrau)):
        if degrau[i] >= to:
            degrau[i] = 1
        else:
            degrau[i] = 0

    return degrau

#frequência e tempo de cada item
#item A
wamp_a = 300
tam_a = (2 * np.pi) / wamp_a
t1_a = 2
t_a = t1_a / 0.0001
ta = np.arange(0, t_a + tam_a, tam_a)

#item B
wamp_b = wamp_a * (5 / 6)
tam_b = (2 * np.pi) / wamp_b
t1_b = t1_a / 2
t_b = t1_b / 0.0001
tb = np.arange(0, t_b + tam_b, tam_b)

#item C
wamp_c = wamp_a * (1 / 3)
tam_c = (2 * np.pi) / wamp_c
t1_c = t1_a * (7 / 40)
t_c = t1_c / 0.0001
tc = np.arange(0, t_c + tam_c, tam_c)

#sinais x1a, x1b, x1c
x1a = degrau(ta, 0) - degrau(ta, 2)
x1b = degrau(tb, 0) - degrau(tb, 1)
x1c = degrau(tc, 0) - degrau(tc, 0.35)

#N - tamanho da DTFS
N = np.power(2, 12)

#calculando a FT
Xa, Xb, Xc = ((tam_a * N) * fft(x1a, N) / N), ((tam_b * N) * fft(x1b, N) / N), ((tam_c * N) * fft(x1c, N) / N)

#vetores de frequência
wa, wb, wc = (fftfreq(len(Xa), d=(tam_a)) * (2 * np.pi)), (fftfreq(len(Xb), d=(tam_b)) * (2 * np.pi)), (fftfreq(len(Xc), d=(tam_c)) * (2 * np.pi))

#índices de frequência mudados de 0 a N-1 para -N/2 + 1 a N/2
#posicionando a frequência zero no meio do gráfico
wda, Xda = fftshift(wa), fftshift(Xa)
wdb, Xdb = fftshift(wb), fftshift(Xb)
wdc, Xdc = fftshift(wc), fftshift(Xc)

#calculando módulos e fases dos sinais
ModXa, phasXa = np.abs(Xda), np.angle(Xda)
ModXb, phasXb = np.abs(Xdb), np.angle(Xdb)
ModXc, phasXc = np.abs(Xdc), np.angle(Xdc)

#gráficos dos sinais no tempo
fig, ax = plt.subplots(1, 1)
ax.plot(ta, x1a, 'r-', linewidth=2, label='x1a(t_a)')
ax.plot(tb, x1b, 'g-', linewidth=2, label='x1b(t_b)')
ax.plot(tc, x1c, 'b-', linewidth=2, label='x1c(t_c)')
ax.set_xlim(-10, 10)
ax.set_title('x1(t)')
ax.set_ylabel("Amplitude")
ax.set_xlabel("t")
ax.legend()
ax.grid(True)

#gráficos do módulos dos sinais
fig1, ax1 = plt.subplots(1, 1)
ax1.plot(wda, ModXa, 'r-', linewidth=2, label='|Xa(e^jw)|')
ax1.plot(wdb, ModXb, 'g-', linewidth=2, label='|Xb(e^jw)|')
ax1.plot(wdc, ModXc, 'b-', linewidth=2, label='|Xc(e^jw)|')
ax1.set_title('Magnitude')
ax1.set_ylabel("Amplitude")
ax1.set_xlabel("rad/s")
ax1.set_xlim(-50, 50)
ax1.legend()
ax1.grid(True)

#gráficos das fases dos sinais
fig2, ax2 = plt.subplots(1, 1)
ax2.stem(wda, phasXa, 'r-', markerfmt='ro', label="angle(Xa(e^jw))", use_line_collection=True)
ax2.stem(wdb, phasXb, 'g-', markerfmt='go', label="angle(Xb(e^jw))", use_line_collection=True)
ax2.stem(wdc, phasXc, 'b-', markerfmt='bo', label="angle(Xc(e^jw))", use_line_collection=True)
ax2.set_title('Fase da FT')
ax2.set_ylabel("Amplitude")
ax2.set_xlabel("rad/s")
ax2.set_xlim(-5, 5)
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()