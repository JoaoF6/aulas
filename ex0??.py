print('Sequencia de fibonacci')
n = int(input('Quantos numeros da sequencia vc quer ver? '))
p = 0
a = 1
for c in range(n):
    soma = a + p
    a = p
    p = soma
    print(a, ' ', end = '')
    print('->' if c < n - 1 else 'fim', end='')