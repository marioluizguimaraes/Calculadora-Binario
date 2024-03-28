print("Escreva abaixo apenas valores em binário!")

# Comando responsável por guardar cada dígito do input em um Lista/vetor[i] e converter cada valor para inteiro
numeroBinario1 = list(map(int, input()))
numeroBinario2 = list(map(int, input()))

# Guarda o número de elementos presentes no vetor através da função len(vetor)
tamanhob1 = len(numeroBinario1)
tamanhob2 = len(numeroBinario2)

# Verifica se os dígitos correspondem a 0 ou 1
for i in numeroBinario1:
    if i != 0 and i != 1:
        print("Dígito inválido:", i)
        quit()

for i in numeroBinario2:
    if i != 0 and i != 1:
        print("Dígito inválido:", i)
        quit()





valores = []



    