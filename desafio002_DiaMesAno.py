dia = input('Por favor informe o dia do seu nascimento: ')
mes = input('Por favor informe o mes do seu nascimento: ')
ano = input('Por favor informe o ano do seu nascimento: ')

if mes == "Jan" or mes == "jan" or mes == "1" or mes == '01':
    mes = 'Janeiro'

elif mes == "Fev" or mes == "fev" or mes == "2" or mes == '02':
    mes = 'Fevereiro'

elif mes == "Mar" or mes == "mar" or mes == "3" or mes == '03':
    mes = 'Março'

elif mes == "Abr" or mes == "mar" or mes == "4" or mes == '04':
    mes = 'Março'

elif mes == "Mai" or mes == "mar" or mes == "5" or mes == '05':
    mes = 'Março'

elif mes == "Jun" or mes == "mar" or mes == "6" or mes == '06':
    mes = 'Março'

elif mes == "Jul" or mes == "mar" or mes == "7" or mes == '07':
    mes = 'Março'

elif mes == "Ago" or mes == "mar" or mes == "8" or mes == '08':
    mes = 'Março'

elif mes == "set" or mes == "mar" or mes == "9" or mes == '09':
    mes = 'Março'

elif mes == "Out" or mes == "mar" or mes == "10" or mes == '10':
    mes = 'Março'

elif mes == "Nov" or mes == "mar" or mes == "11" or mes == '11':
    mes = 'Março'

elif mes == "Dez" or mes == "mar" or mes == "12" or mes == '12':
    mes = 'Março'


print ('Vôce nasceu no dia',dia,'de',mes,'de',ano) 

a = input ('. Correto? - ::')

if(a == "s"):
    print('Okay, muito obrigado...')
else:
    print('Ouve alguns problemas internos !!')
    print('Me desculpe pelo incomodo...')
