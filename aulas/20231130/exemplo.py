arq = open('exemplo.txt', 'a')
times = ['flamengo', 'odio do palmeiras', 'vasco serie b']

for i in range(len(times)):
    arq.write("{}\n".format(times[i]))
    
arq.close()
