# Exercício - 31/03/21

ne = int(input('Digite o número de eleitores: '))
tentativa = 0
quantidade_votos = 0
João = 0
Maria = 0
Voto_branco = 0
Voto_nulo = 0
senha = 0
while ne >= quantidade_votos:
    print('\n\t***Próximo eleitor***\n')
    print('\tCÓDIGO | CANDIDATO')
    print('\t11     | João')
    print('\t45     | Maria')
    print('\t0      | Voto em Branco')
    seu_voto = int(input('Digite seu voto: '))
    quantidade_votos = quantidade_votos + 1
    if seu_voto == 11:
        João = João + 1
    if seu_voto == 45:
        Maria = Maria + 1
    if seu_voto == 0:
        Voto_branco = Voto_branco + 1
    if seu_voto !=11 and 45 and 0:
        Voto_nulo = Voto_nulo + 1
    if seu_voto == 1234:
        while tentativa >= 0 and senha != 2003:
            senha = int(input('Digite a senha para encerrar a eleição: '))
        break
    if quantidade_votos == ne:
        break
        print('VOTAÇÃO ENCERRADA!')
        print('*'*33)


        print(f'Quantidades de votos esperados: {ne}')
        print(f'Total de votos: {quantidade_votos}')
        print('*'*33)


        print('RESULTADO DA ELEIÇÃO:')
        print(f'Quantidade dos votos para Maria: {Maria}')
        print(f'Quantidade dos votos para João: {João}')
        print(f'Quantidade dos votos em branco: {Voto_branco}')
        print(f'Quantidade de votos nulos: {Voto_nulo}')

print('VOTAÇÃO ENCERRADA PELO PRESIDENTE!')
print('*'*33)

print(f'Quantidades de votos esperados: {ne}')
print(f'Total de votos: {quantidade_votos}')
print('*'*33)


print('RESULTADO DA ELEIÇÃO:')
print(f'Quantidade dos votos para Maria: {Maria}')
print(f'Quantidade dos votos para João: {João}')
print(f'Quantidade dos votos em branco: {Voto_branco}')
print(f'Quantidade de votos nulos: {Voto_nulo}')
