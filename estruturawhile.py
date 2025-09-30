''' 
estrutura de repeticao com teste logico = while
while not apple: (enquanto a condicao for verdadeira, o laco se repetira)
    apple
pega
usar while quando nao souber o limite


'''
r = 'p'
while r == 'p':
    r = str(input('qual o seu sexo? \nM - Masculino \nF - Feminino? ')).strip().upper()
    if r != 'M' or r != 'F':
        r = str(input('erro!! qual o seu sexo? \nM - Masculino \nF - Feminino? ')).strip().upper()
        if r == 'M':
            print('Voce e homem!')
        elif r == 'F':
            print('voce e mulher!')
    else:
        print('erro, digite novamente')
