inter = gremio = empate = 0

while (True):
    gols_inter, gols_gremio = input().split()
    gols_inter, gols_gremio = int(gols_inter), int(gols_gremio)

    if (gols_inter > gols_gremio):
        inter = inter + 1
    elif (gols_gremio > gols_inter):
        gremio = gremio + 1
    else:
        empate = empate + 1

    print('Novo grenal (1-sim 2-nao)')
    resposta = int(input())
    if (resposta == 2):
        break

total = inter + gremio + empate

print(total, 'grenais')
print('Inter:',inter, sep='')
print('Gremio:{}'.format(gremio))
print('Empates:',empate, sep='')

if (inter > gremio):
    print('Inter venceu mais')
elif (gremio > inter):
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
