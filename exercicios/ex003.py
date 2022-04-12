n1 = int(input('Forneça o primeiro Numero: '))
n2 = int(input('Forneça o segundo Numero:  '))
res = n1 + n2

print('A soma de {} e {} numero é igual a: {}'.format(n1, n2, res))

resp = input('Correto?: ')

if resp == "s" or resp == "sim":
    print('Obrgiado')

else:
    print('Me descupe pelo erro')
