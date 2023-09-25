vitorias_inter = 0
vitorias_gremio = 0
empates = 0

inter, gremio = input().split()
inter, gremio = int(inter), int(gremio)
if (inter > gremio):
    vitorias_inter = vitorias_inter + 1
elif (inter < gremio):
    vitorias_gremio = vitorias_gremio + 1
else:
    empates = empates + 1

print('Novo grenal (1-sim 2-nao)')
resposta = int(input())

while (resposta == 1):
    inter, gremio = input().split()
    inter, gremio = int(inter), int(gremio)
    if (inter > gremio):
        vitorias_inter = vitorias_inter + 1
    elif (inter < gremio):
        vitorias_gremio = vitorias_gremio + 1
    else:
        empates = empates + 1

    print('Novo grenal (1-sim 2-nao)')
    resposta = int(input())

print(vitorias_inter + vitorias_gremio + empates,'grenais')
print('Inter:{}'.format(vitorias_inter))
print('Gremio:{}'.format(vitorias_gremio))
print('Empates:{}'.format(empates))
if (vitorias_inter > vitorias_gremio):
    print('Inter venceu mais')
elif (vitorias_gremio > vitorias_inter):
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
