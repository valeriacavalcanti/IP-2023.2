import funcoes

arq = open('municipios.txt', 'r', encoding='utf-8')

# gravando na memória principal
# gera uma lista contendo as linhas do arquivo
# TODOS OS MUNICIPIOS - 5560
registros = arq.read().splitlines()

arq.close()

#for i in range(5):
#    print(registros[i])


codigo = int(input("Digite o código do estado: "))
print(funcoes.quantidade_cidade_codigo_UF(registros, codigo)) #PB
print(funcoes.quantidade_cidade_sigla_UF(registros, 'PB')) #PB
print(funcoes.cidade(registros, 2507507)) # João Pessoa
print(funcoes.cidade(registros, 2504850)) # Coxixola
print(funcoes.cidade(registros, 0000000)) # Erro
