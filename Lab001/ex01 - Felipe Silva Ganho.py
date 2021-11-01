#Felipe Silva Ganho

def separaParImpar(s, n):
    sinalPar = []
    sinalImpar = []

    for i in range(len(s)):
        sinalPar.append(1 / 2 * (s[i] + s[len(s) - i - 1]))
        sinalImpar.append(1 / 2 * (s[i] - s[len(s) - i - 1]))

    return "Par: " + str(sinalPar), "Ímpar: " + str(sinalImpar)

#Teste da Função\n"
print("Alguns testes nos sinais:")
print("s1 = [ 2, 1, 0, 1, 2], n = [-2, -1, 0, 1, 2] =", separaParImpar([ 2, 1, 0, 1, 2], [-2, -1, 0, 1, 2]))
print("s2 = [-2,-1, 0, 1, 2], n = [-2, -1, 0, 1, 2] =", separaParImpar([-2,-1, 0, 1, 2], [-2, -1, 0, 1, 2]))
print("s3 = [ 0, 0 ,0 , 2, 4], n = [-2, -1, 0, 1, 2] =", separaParImpar([ 0, 0 ,0 , 2, 4], [-2, -1, 0, 1, 2]))
print("s4 = [ 0 , -1 , -1, 3 , 2], n = [-2, -1, 0, 1, 2] =", separaParImpar([ 0 , -1 , -1, 3 , 2], [-2, -1, 0, 1, 2]))
print("s5 = [ 0, 0 ,0 , 2, 4], n = [ 0, 1, 2, 3, 4] =", separaParImpar([ 0, 0 ,0 , 2, 4], [ 0, 1, 2, 3, 4]))