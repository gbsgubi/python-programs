HPken = int(input('Digite o valor do HP do Ken: '))
HPryu = int(input('Digite o valor do HP do Ryu: '))

ATKryu = 0
ATKken = 0

while HPken > 0 and HPryu > 0:
  ATK = int(input('Valor do golpe (Positivo: KEN) (Negativo: RYU): '))
  if ATK<0:
    HPken = HPken + ATK
    ATKryu +=1
    print(f'Ryu aplicou um golpe: {ATK}')
    print(f'HP Ken: {HPken}')
    print(f'HP Ryu: {HPryu}')
  else:
    HPryu = HPryu - ATK
    ATKken +=1
    print(f'Ken aplicou um golpe: {ATK}')
    print(f'HP Ryu: {HPryu}')
    print(f'HP Ken: {HPken}')

if HPken:
  print('Lutador Ken venceu!')
  print(f'Total de golpes realizados por Ken: {ATKken}')
  print(f'Total de golpes realizados por Ryu: {ATKryu}')
else:
  print('Lutador Ryu venceu!')
  print(f'Total de golpes realizados por Ryu: {ATKryu}')
  print(f'Total de golpes realizados por Ken: {ATKken}')