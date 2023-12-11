import funcoes

arq = open('brasileirao.csv', 'r')

registros = arq.read().splitlines()
#registros = arq.readlines()

#nomes_times = funcoes.times(registros[1:])
#for i in range(len(nomes_times)):
#    print(nomes_times[i])
    
#print(funcoes.total_gols(registros[1:]))
#print(funcoes.media_gols_rodadas(registros[1:]))
#print(funcoes.media_gols_jogos(registros[1:]))

#print(funcoes.rebaixados(registros[1:]))

# print(funcoes.libertadores(registros[1:]))

arq.close()
