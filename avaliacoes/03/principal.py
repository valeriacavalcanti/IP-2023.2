import funcoes

arq = open('cstrc.csv', 'r')
registros = arq.read().splitlines()

periodos = funcoes.periodos(registros)
print('Quantidade de períodos:', periodos)

for i in range(periodos):
    print('Período {}: {}h'.format(i + 1, funcoes.total(registros, i + 1)))

print('Maior CH:', funcoes.maior(registros))

print("Disciplinas com Carga horária 83h")
for disciplina in funcoes.disciplinas(registros, 83):
    print('-',disciplina)

arq.close()
