salario_bruto = float(input('Salário Bruto: R$'))

if salario_bruto <= 1045.00:
  INSS = salario_bruto * 0.075
elif salario_bruto <= 2089.60:
  INSS = salario_bruto * 0.09
elif salario_bruto <= 3134.40:
  INSS = salario_bruto * 0.12
else:
  INSS = salario_bruto * 0.14

salario_liquido = salario_bruto - INSS

if salario_liquido <= 1903.98:
  IR = 0
elif salario_liquido <= 2826.65:
  IR = salario_liquido * 0.075 - 142.8
elif salario_liquido <= 3751.05:
  IR = salario_liquido * 0.15 - 354.8
elif salario_liquido <= 4664.68:
  IR = salario_liquido * 0.225 - 869.36

salario_liquido -= IR
print('%.2f' % INSS)
print('%.2f' % IR)
print('%.2f' % salario_liquido)