# Código que mostra o loop funcionando em cada iteração
INDICE = 13
SOMA = 0
K = 0

# Loop para calcular a SOMA conforme o valor de K, exibindo o progresso
while K < INDICE:
    K += 1
    SOMA += K
    print(f"Iteração {K}: SOMA = {SOMA}")

# Exibe o valor final de SOMA
print(f"Valor final de SOMA: {SOMA}")
