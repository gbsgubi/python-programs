#Exércicio - 17/03/21

A1 = float(input('Digite sua primeira nota: '))
A2 = float(input('Digite sua segunda nota: '))
A3 = float(input('Se você realizou uma terceira prova, digite sua nota, caso contrário, digite 0: '))
MP = float(input('Digite sua média prática: '))
MT1 = 0.4*A1 + 0.6*A2
MT2 = 0.4*A1 + 0.6*A3
MT3 = 0.4*A3 + 0.6*A2

if MT1>MT2 and MT1>MT3:
    MT=MT1
else:
    if MT2>MT1 and MT2>MT1:
          MT=MT2
    else:
          MT=MT3
if MT and MP:
    MF = 0.5*MT + 0.5*MP
else:
    MF = min(MT,MP)
print('\nUtilizar a média com o valor: %.2f'%MT)
if MF>=5:
    print(f'\nAprovado com %.2f'%MF)
else:
    print(f'\nReprovado com %.2f'%MF)