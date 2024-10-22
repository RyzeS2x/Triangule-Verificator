ret1 = int(input('Digite o comprimento da primeira reta: '))
ret2 = int(input('Digite o comprimento da segunda reta: '))
ret3 = int(input('Digite o comprimento da terceira reta: '))

if ret1 + ret2 > ret3 and ret3 + ret2 > ret1 and ret1 + ret3 > ret2:
    
    print('Da pra formar um triangulo')

else:

    print('Não pode formar um triangulo')
