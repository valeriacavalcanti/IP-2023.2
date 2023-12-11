import funcoes

arq_brasileirao = open('brasileirao.csv', 'r')
arq_extrato = open('extrato_brasileirao.txt', 'w')

registros = arq_brasileirao.read().splitlines()


arq_extrato.write('LIBERTADORES\n')
times = funcoes.libertadores(registros[1:])
for i in range(len(times)):
    arq_extrato.write('- {}\n'.format(times[i]))


arq_extrato.write('\n')

arq_extrato.write('REBAIXADOS\n')
times = funcoes.rebaixados(registros[1:])
for i in range(len(times)):
    arq_extrato.write('- {}\n'.format(times[i]))

arq_extrato.write('\n')

qtd_gols = funcoes.total_gols(registros[1:])
arq_extrato.write('Total de gols: {}\n'.format(qtd_gols))

arq_brasileirao.close()
arq_extrato.close()
