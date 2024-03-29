print("Escreva abaixo apenas valores em binário!")

# Comando responsável por guardar cada dígito do input em um Lista/vetor[i] e converter cada valor para inteiro
numeroBinario1 = list(map(int, input()))
numeroBinario2 = list(map(int, input()))

# Guarda o número de elementos presentes no vetor através da função len(vetor)
tamanhob1 = len(numeroBinario1)
tamanhob2 = len(numeroBinario2)

# Ler cada intem da lista por vez
for i in numeroBinario1:
    # Verifica se o item da vez é 0 ou 1   
    if i != 0 and i != 1:
        print("Dígito inválido:", i)
        quit()

# Ler cada intem da lista por vez
for i in numeroBinario2:
    # Verifica se o item da vez é 0 ou 1
    if i != 0 and i != 1:
        print("Dígito inválido:", i)
        quit()

# Verifica se o primeiro numero em binario tem - bits em relaçâo ao segundo
if (tamanhob1 < tamanhob2):
    #calcula quantos bits são necessário para ambos ficarem com a mesma quantidade
    diferenca = tamanhob2 - tamanhob1
    # Laço com a repetição igual a diferença de bits de um para o outro
    for tamanhob1 in range(diferenca):
        # Adiciona 0 a esquerda do item de referência da lista
        numeroBinario1.insert(0, 0)

# Verifica se o degundo numero em binario tem - bits em relaçâo ao primeiro
elif (tamanhob1 > tamanhob2):
    #calcula quantos bits são necessário para ambos ficarem com a mesma quantidade
    diferenca = tamanhob1 - tamanhob2
    # Laço com a repetição igual a diferença de bits de um para o outro
    for tamanhob2 in range(diferenca):
        # Adiciona 0 a esquerda do item de referência da lista
        numeroBinario2.insert(0, 0)

resultado = []
vaiUm = [0]

numeroBinario1.reverse()
numeroBinario2.reverse()

for n in numeroBinario1:
    if (numeroBinario1[n] == 1 and numeroBinario2[n] == 1):
        resultado.append(0)
        vaiUm.append(1)

    elif((numeroBinario1[n] == 0 and numeroBinario2[n] == 1) or (numeroBinario1[n] == 1 and numeroBinario2[n] == 0)):
        resultado.append(1)
        vaiUm.append(0)

    elif(numeroBinario1[n] == 0 and numeroBinario2[n] == 0):
        resultado.append(0)
        vaiUm.append(0)

vaiUm.reverse()
numeroBinario1.reverse()
numeroBinario2.reverse()
resultado.reverse()


print(vaiUm, '\n', numeroBinario1, '\n' ,numeroBinario2, '\n', resultado,  sep='')  