cupom_correto = '1234' # Código do cupom de desconto válido
print('Processo de cadastro:')
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if (idade < 18):    #Restrições para menores de 18 anos, não podendo escolher o plano Premium.
    plano = int(input('Escolha seu plano: \n1 - Básico \n2 - Padrão \nDigite o número do plano: '))
else:
    plano = int(input('Escolha seu plano: \n1 - Básico \n2 - Padrão \n3 - Premium \nDigite o número do plano: '))

telas = int(input('Digite o número de telas simultâneas (1-4): '))
offline = bool(int(input('Pacote de download offline (0 para não, 1 para sim): ')))
cupom = bool(int(input('Possui cupom de desconto? (0 para não, 1 para sim): ')))
match plano:                 #Valores dos planos.
    case 1:
        plano = 19.90
        plano_vlr = 19.90
        plano_inf = 'Básico'
    case 2:
        plano = 34.90
        plano_vlr = 34.90
        plano_inf = 'Padrão'
    case 3:
        plano = 49.90
        plano_vlr = 49.90
        plano_inf = 'Premium'

if (telas == 4):            #valores adicionais por telas simultâneas.
    telas_inf = 24
    plano += telas_inf
elif (telas == 3):
    telas_inf = 18
    plano += telas_inf
elif (telas == 2):
    telas_inf = 10
    plano += telas_inf
else:
    plano += 0

if (offline == True):      #Valor adicional para download offline.
    offline_vlr = 12
    plano += offline_vlr
    offline_inf = 'Sim'
else:    
    offline_vlr = 0
    plano += offline_vlr
    offline_inf = 'Não'

while True and (cupom == True):      #Validação do cupom de desconto.
    cupom_usuario = str(input('Digite o código do cupom: '))
    if (cupom_usuario == cupom_correto):
        desconto = plano * 0.15
        plano -= desconto
        plano_vlr -= desconto
        print('Cupom aplicado com sucesso! Você recebeu 15% de desconto.')
        break
    else:
        print('Cupom inválido. Digite novamente.')

match idade:      #Classificação por faixa etária e restrição para o plano Premium.
    case idade if idade < 18:
        idade_inf = 'Jovem'
        plano_blq = 'O plano Premium não está disponível para menores de 18 anos.'
        senior_dsct = 0
    case idade if 18 <= idade < 60:
        idade_inf = 'Adulto'
        senior_dsct = 0
    case idade if idade >= 60:
        idade_inf = 'Sênior'
        senior_dsct = 5
        plano -= senior_dsct

from datetime import datetime   #Horario de cadastro. !!!EM TEMPO REAL!!!
data_atual = datetime.now()
agora = data_atual.strftime('%H:%M')

match agora:  #Classificação de turnos
    case agora if '06:00' <= agora < '11:59':
        agora_trn = 'Manhã'
    case agora if '12:00' <= agora < '17:59':
        agora_trn = 'Tarde'
    case agora if '18:00' <= agora < '23:00':
        agora_trn = 'Noite'
    case _:
        agora_trn = 'Madrugada'
        agora_inf = 'Cadastro realizado fora do horário de atendimento. Suporte disponível a partir das 6h.'

# V Resultados V

print('============================================= \n        BEM-VINDO À VDKSTREAM! \n=============================================')
print('Cliente: ', nome, '|', idade_inf)
print('Plano:', plano_inf)
print('Telas: ', telas)
print('Download: ', offline_inf)
print('Turno: ', agora, '|', agora_trn)
print('==============================================')
print('Valor base: R$ {:.2f}'.format(plano_vlr))
if (cupom == True):
    print('Desconto: R$ {:.2f}'.format(desconto))
else:
    print('Desconto: R$ 0.00')
if (telas == 1):
    print('Acrésc. telas: R$ 0.00')
else:
    print('Acrésc. telas: R$ {:.2f}'.format(telas_inf))
print('Downloads: R$ {:.2f}'.format(offline_vlr))
print('Desconto sênior: R$ {:.2f}'.format(senior_dsct))
print('===============================================')
print('Total Mensal: R$ {:.2f}'.format(plano))
print('===============================================')
if idade < 18:
    print(plano_blq)
if agora < '06:00' or agora >= '23:00':
    print(agora_inf)