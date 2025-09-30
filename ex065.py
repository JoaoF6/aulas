resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('Digitre um numero: '))
    soma += num
    quant += 1
    resp = str(input('Quer continuar? [S/N]').strip().upper()[0])
media = soma / quant
print(' A sua media foi: {}'.format(media))
print('FIM')