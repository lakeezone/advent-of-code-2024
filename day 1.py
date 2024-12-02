esquerda = []
direita = []

with open("c:/projetos/py/advente-of-code-2024/data.txt") as arquivo:
    linhas = arquivo.readlines()

    total = 0

    for line in linhas:
        line = line.strip().split()  
        esquerda.append(int(line[0]))
        direita.append(int(line[1]))

esquerda = sorted(esquerda)
direita = sorted(direita)

for i in range(len(esquerda)):
    total += abs(esquerda[i] - direita[i])

    print("AOC DAY 1 - PART 1 - " + str(total))

    total = 0

for i in range(len(esquerda)):
    k = int(esquerda[i])
    total += (k * direita.count(k))

    print("AOC DAY 1 - PART 2 - " + str(total))
