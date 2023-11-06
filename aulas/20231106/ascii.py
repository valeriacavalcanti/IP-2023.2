# tabela ascii


print("{:8} {:3} {:3} {:3} {:3}".format('BIN','OCT', 'HEX', 'DEC', 'SÍMBOLO'))
for i in range(32, 128):
    decimal = i
    binario = bin(i)[2:]
    octal = oct(i)[2:]
    hexa = hex(i)[2:]
    simbolo = chr(i)
    
    print("{:>08} {:>03} {:>03} {:>03} {}".format(binario, octal, hexa, decimal, simbolo))
