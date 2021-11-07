# While
nome = ''
while nome != 'exit':
    nome = input('Qual o seu nome: ')
    print(f' Olã {nome}')

p = 0
while p < 10:
    p = p + 1
    # print(f"{p}")
    pass

x = 0
while x < 2:
    y = 0
    while y < 2:
        g = 0
        while g < 2:
            print(f" {x}, {y}, {g}")
            g += 1
        y += 1
    x += 1

print()
print(f'\n Fim do Programa: {x}')
