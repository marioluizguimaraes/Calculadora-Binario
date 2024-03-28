print("Escreva abaixo um valor em binário!")

# Comando responsável por guardar cada dígito do input em um Lista/vetor[i] e converter cada valor para inteiro

numeroBinario = list(map(int, input()))

# Guarda o número de elementos presentes no vetor através da função len(vetor)
tamanho = len(numeroBinario)

valores = []

# Verifica se os dígitos correspondem a 0 ou 1
for i in numeroBinario:
    if i != 0 and i != 1:
        print("Dígito inválido:", i)
        quit()

casadavez = 0
# Calcula os valores relacionados ao número binário em cada casa
for n in numeroBinario:
    casadavez += 1
    valor = n * (2 ** (tamanho - casadavez))
    valores.append(valor)

resultado = sum(valores)

print("O valor em binário tem", tamanho, "Bits.")
print("Resultado em decimal:", resultado)

# Fontes:
# https://www.ime.usp.br/~leo/mac2166/2017-1/introducao_vetores_python.html#:~:text=O%20truque%20b%C3%A1sico%20%C3%A9%20ler,Tab.
# https://www.alura.com.br/artigos/listas-no-python?utm_term=&utm_campaign=%5BSearch%5D+%5BPerformance%5D+-+Dynamic+Search+Ads+-+Artigos+e+Conte%C3%BAdos&utm_source=adwords&utm_medium=ppc&hsa_acc=7964138385&hsa_cam=11384329873&hsa_grp=111087461203&hsa_ad=687448474447&hsa_src=g&hsa_tgt=dsa-2276348409543&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=CjwKCAjw5ImwBhBtEiwAFHDZx9875l6OTGadwWNuhFXP3XKKgTBxbpDxhdyJRjSk_U-geBmqEWOYoBoCEMgQAvD_BwE