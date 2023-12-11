import funcoes

arq = open('municipios.csv', 'r', encoding='utf-8')

registros = arq.read().splitlines()

print('Quantidade de cidades: ', len(registros))

print('Cidades da PB:', funcoes.quantidade_cidades_por_codigo_UF(registros, 25))
print('Cidades da PB:', funcoes.quantidade_cidades_por_sigla_UF(registros, "PB"))

print('Cidade:', funcoes.nome_cidade(registros, 2507507))
print('Cidade:', funcoes.nome_cidade(registros, 2504850))

print('Mesorregiões da PB:', funcoes.mesorregioes(registros, "PB"))
print('Mesorregiões de SC:', funcoes.mesorregioes(registros, "SC"))

print('População da PB:', funcoes.populacao(registros, 25))
print('População da PB:', funcoes.populacao(registros, 26))

print('Latitude de João Pessoa:', funcoes.latitude(registros, 2504850))
print('Longitude de João Pessoa:', funcoes.longitude(registros, 2504850))
print(funcoes.latitude(registros, 2504850), funcoes.longitude(registros, 2504850))

arq.close()
