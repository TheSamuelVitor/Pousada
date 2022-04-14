import os
from time import sleep
from datetime import datetime, date

#cores \033[31m TEXTO \033[m
# 30 - branco
# 31 - vermelho
# 32 - verde
# 33 - amarelo
# 34 - azul
# 35 - roxo
# 36 - azul claro
# 37 - cinza

def limpar():
    os.system('clear')

acompanhante = []
acom_nome = []
acom_cpf = []
piso1 = 10
piso2 = 10

def valida_int() :
    sap = 1

clientes = []
cliente_nome = []
cliente_cpf = []
cliente_tele = []
cliente_estado = []
cliente_cidade = []
cliente_plano = []
tam = len(cliente_nome)

qtd_clientes = 0
gastos = 0
ganhos = 0
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

fornecedores_nome_dono = []
fornecedores_nome_em = []
fornecedores_produto = []
fornecedores_pro_qtd = []
fornecedores_pro_va = []
fornecedores_cnpj = []
fornecedores_estado = []
fornecedores_cidade = []
fornecedores_rua = []
fornecedores_num = []

opcao = 1
opcao_cliente = 1
opcao_fornecedor = 1
nova_op = 0

estadia_dia = 200
num_sema1 = 5
num_bisema1 = 6
num_men1 = 8
prc_sema_1 =  num_sema1/100
prc_bisema1 = num_bisema1/100
prc_men1 = num_men1/100
estadia_sema = (estadia_dia * 7) - ((estadia_dia * 7)*prc_sema_1)
estadia_bisema = (estadia_dia * 14) - ((estadia_dia * 14)*prc_bisema1)
estadia_men = (estadia_dia * 30) - ((estadia_dia * 30)*prc_men1)


estadia_dia2 = 350
num_sema2 = 10
num_bisema2 = 15
num_men2 = 20
prc_sema_2 =  num_sema2/100
prc_bisema2 = num_bisema2/100
prc_men2 = num_men2/100
estadia_sema2 = (estadia_dia2 * 7) - ((estadia_dia2 * 7)*prc_sema_2)
estadia_bisema2 = (estadia_dia2 * 14) - ((estadia_dia2 * 14)*prc_bisema2)
estadia_men2 = (estadia_dia2 * 30) - ((estadia_dia2 * 30)*prc_men2)

while opcao != 0:
    limpar()
    print('\033[31m--------------------------------------\033[m')
    print('| BEM VINDO A POUSADA NOVO HORIZONTE |')
    print('\033[34m--------------------------------------\033[m')
    print('\n---------------- MENU ----------------')
    print('\n1. CLIENTES')
    print('2. FORNECEDORES')
    print('3. RELATÓRIO')
    print('4. CONFIG')
    print('0. SAIR')
    opcao = int(input('\nDigite uma opção: '))
    limpar()
    
    if opcao == 1:

        while opcao_cliente != 0:
            
            limpar()
            print('\033[36m------------------------\033[m')
            print('\033[36m|\033[m     AREA - CLIENTE   \033[36m|\033[m')
            print('\033[36m------------------------\033[m')
            print('\n--------- MENU ---------')
            print('\n1. CADASTRO')
            print('2. LISTAR')
            print('3. CHECKOUT')
            print('4. LIMPAR')
            print('0. SAIR')
            opcao_cliente = int(input('\nDigite uma opção: '))
            limpar()

            if opcao_cliente == 1:
                
                while True:
                                
                                print('\n\033[36m-----------------------------------------------------------\033[m')
                                print('\033[36m|\033[m                         ESTADIAS                        \033[36m|\033[m')
                                print('\033[36m-----------------------------------------------------------\033[m')
                                print('\n')
                                print(f'       PISO 1                          PISO 2 ')
                                print(f'-  DISPONIVEIS [{piso1}]             -  DISPONIVEIS [{piso2}]')
                                print(f'-  DIÁRIA = R$ {estadia_dia}              -  DIÁRIA = R$ {estadia_dia2}')
                                print('\n                         PLANOS:                          ')
                                print(f'\n1. DIAS                         1. DIAS ')
                                print(f'2. SEMANAL = R$ {estadia_sema}          2. SEMANAL = R$ {estadia_sema2}')
                                print(f'3. BI-SEMANAL = R$ {estadia_bisema}       3. BI-SEMANAL = R$ {estadia_bisema2}')
                                print(f'4. MENSAL = R$ {estadia_men}           4. MENSAL = R$ {estadia_men2}')
                                piso = int(input('\nESCOLHA O PISO E O PLANO -\nPiso: '))
                                estadia = int(input('Plano: '))

                                limpar()
                                #piso 1
                                if(piso == 1) : 
                                    
                                    if estadia == 1 and piso == 1:
                                        
                                        qtd_dia = int(input('Quantidade de dias: '))
                                        
                                        if(qtd_dia>=7 and qtd_dia<14):
                                            
                                            if(qtd_dia == 7) :
                                                print('RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO SEMANAL!\nPLANO COM ATÉ 10% DEDESCONTO')
                                                decisao = input('Deseja trocar seu plano? S/N: ')
                                                decisao = decisao.upper()
                                                if decisao == "S":
                                                    estadia = 2
                                                else:
                                                    print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                                    ganhos += qtd_dia * estadia_dia
                                            
                                            else:
                                                
                                                print(f'RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO SEMANAL + {qtd_dia-7}  diarias!\nPLANOCOM ATÉ 10% DE DESCONTO')
                                                decisao = input('Deseja trocar seu plano? S/N: ')
                                                decisao = decisao.upper()
                                                if decisao == "S":
                                                    plano = estadia_dia + ((qtd_dia-7)*estadia_dia) 
                                                    ganhos += estadia_dia + ((qtd_dia-7)*estadia_dia)
                                                else:
                                                    print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                                    ganhos += qtd_dia * estadia_dia
                                        
                                        elif(qtd_dia>=14 and qtd_dia<30):
                                            
                                            if(qtd_dia == 14) :
                                                print('RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO BI-SEMANAL!\nPLANO COM ATÉ 15% DEDESCONTO')
                                                decisao = input('Deseja trocar seu plano? S/N: ')
                                                decisao = decisao.upper()
                                                if decisao == "S":
                                                    estadia = 3
                                                else:
                                                    print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                                    ganhos += qtd_dia * estadia_dia
                                            
                                            else :
                                                print(f'RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO BI-SEMANAL + {qtd_dia-14} diarias!\nPLANO COM ATÉ 15% DE DESCONTO')
                                                decisao = input('Deseja trocar seu plano? S/N: ')
                                                decisao = decisao.upper()
                                                if decisao == "S":
                                                    plano = 2.118,20 + ((qtd_dia-14)*estadia_dia)
                                                    ganhos += 2.118,20 + ((qtd_dia-14)*estadia_dia)
                                                else:
                                                    print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                                    ganhos += qtd_dia * estadia_dia
                                        
                                        elif(qtd_dia>=30):
                                            
                                            if(qtd_dia == 30):
                                                print('RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO MENSAL!\nPLANO COM ATÉ 25% DE DESCONTO')
                                                decisao = input('Deseja trocar seu plano? S/N: ')
                                                decisao = decisao.upper()
                                                if decisao == "S":
                                                    estadia = 4
                                                else:
                                                    print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                                    ganhos += qtd_dia * estadia_dia
                                            
                                            else :
                                                print(f'RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO MENSAL + {qtd_dia - 30} diarias\nPLANOCOM ATÉ 25% DE DESCONTO')
                                                decisao = input('Deseja trocar seu plano? S/N: ')
                                                decisao = decisao.upper()
                                                if decisao == "S":
                                                    plano = 4.005,00 + ((qtd_dia - 30)*estadia_dia)
                                                    ganhos += 4.005,00 + ((qtd_dia - 30)*estadia_dia)
                                                else:
                                                    print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                                    ganhos += qtd_dia * estadia_dia
                                        
                                        else:
                                            print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                            ganhos += qtd_dia * estadia_dia
                                        
                                        plano = f'DIARIA - {qtd_dia} dia(s)\nValor = R$ {qtd_dia*estadia_dia:.2f}'
                                        qtd_clientes+=1

                                    elif estadia == 2 and piso == 1:
                                        plano = f'SEMANAL\nValor = R$ {estadia_dia}'
                                        ganhos += estadia_dia
                                        qtd_clientes+=1

                                    elif estadia == 3 and piso == 1:
                                        plano = f'BI - SEMANAL\nValor = R$ {estadia_sema}'
                                        ganhos += estadia_sema
                                        qtd_clientes+=1

                                    elif estadia == 4 and piso == 1:
                                        plano = f'MENSAL\nValor = R$ {estadia_men}'
                                        ganhos += estadia_men
                                        qtd_clientes+=1
                                    sleep(2)
                                    break

                                #piso 2
                                elif(piso == 2) :
                                    dwad = 1
                                    if estadia == 1 and piso == 2:
                                        qtd_dia = int(input('Quantidade de dias: '))

                                        if(qtd_dia>=7 and qtd_dia<14):

                                            if(qtd_dia == 7) :
                                                print('RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO SEMANAL!\nPLANO COM ATÉ 10% DEDESCONTO')
                                                decisao = input('Deseja trocar seu plano? S/N: ')
                                                decisao = decisao.upper()
                                                if decisao == "S":
                                                    estadia = 2
                                                else:
                                                    print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                                    ganhos += qtd_dia * estadia_dia2

                                            else:
                                                print(f'RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO SEMANAL + {qtd_dia-7}  diarias!\nPLANOCOM ATÉ 10% DE DESCONTO')
                                                decisao = input('Deseja trocar seu plano? S/N: ')
                                                decisao = decisao.upper()
                                                if decisao == "S":
                                                    plano = estadia_sema2 + ((qtd_dia-7)*estadia_dia2)
                                                    ganhos+= estadia_sema2 + ((qtd_dia-7)*estadia_dia2)
                                                else:
                                                    print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                                    ganhos += qtd_dia * estadia_dia2

                                        elif(qtd_dia>=14 and qtd_dia<30):

                                            if(qtd_dia == 14) :
                                                print('RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO BI-SEMANAL!\nPLANO COM ATÉ 15% DEDESCONTO')
                                                decisao = input('Deseja trocar seu plano? S/N: ')
                                                decisao = decisao.upper()
                                                if decisao == "S":
                                                    estadia = 3
                                                else:
                                                    print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                                    ganhos += qtd_dia * estadia_dia2

                                            else :
                                                print(f'RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO BI-SEMANAL + {qtd_dia-14} diarias!\nPLANO COM ATÉ 15% DE DESCONTO')
                                                decisao = input('Deseja trocar seu plano? S/N: ')
                                                decisao = decisao.upper()
                                                if decisao == "S":
                                                    plano = estadia_bisema2 + ((qtd_dia-14)*estadia_dia2)
                                                    ganhos += estadia_bisema2 + ((qtd_dia-14)*estadia_dia2)
                                                else:
                                                    print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                                    ganhos += qtd_dia * estadia_dia2
                                        elif(qtd_dia>=30):

                                            if(qtd_dia == 30):
                                                print('RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO MENSAL!\nPLANO COM ATÉ 25% DE DESCONTO')
                                                decisao = input('Deseja trocar seu plano? S/N: ')
                                                decisao = decisao.upper()
                                                if decisao == "S":
                                                    estadia = 4
                                                else:
                                                    print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                                    ganhos += qtd_dia * estadia_dia2

                                            else :
                                                print(f'RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO MENSAL + {qtd_dia - 30} diarias\nPLANOCOM ATÉ 25% DE DESCONTO')
                                                decisao = input('Deseja trocar seu plano? S/N: ')
                                                decisao = decisao.upper()
                                                if decisao == "S":
                                                    plano = estadia_men2 + ((qtd_dia - 30)*estadia_dia2)
                                                    ganhos +=  estadia_men2 + ((qtd_dia - 30)*estadia_dia2)
                                                else:
                                                    print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                                    ganhos += qtd_dia * estadia_dia2

                                        else:
                                                print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                                ganhos += qtd_dia * estadia_dia2

                                        plano = f'DIARIA - {qtd_dia} dia(s)\nValor = R$ {qtd_dia*estadia_dia2:.2f}'
                                        qtd_clientes += 1

                                    elif estadia == 2 and piso == 2:
                                        plano = f'SEMANAL\nValor = {estadia_sema2:.2f}'
                                        ganhos += estadia_sema2
                                        qtd_clientes+=1

                                    elif estadia == 3 and piso == 2:
                                        plano = f'BI - SEMANAL\nValor = {estadia_bisema2:.2f}'
                                        ganhos += estadia_bisema2
                                        qtd_clientes+=1

                                    elif estadia == 4 and piso == 2:
                                        plano = f'MENSAL\nValor = {estadia_men2:.2f}'
                                        ganhos += estadia_men2
                                        qtd_clientes+=1

                                    print('\n DESEJA CADASTRAR ACOMPANHANTE?')
                                    while(1):
                                        ac = int(input('1 - Sim\n2 - Não\nopção : '))
                                        if(ac == 1):
                                            print('----------------------------')
                                            print('  CADASTRO DO ACOMPANHANTE  ')
                                            nome_acom = input('NOME: ')
                                            while True:
                                                cpf_acom = input('CPF: ')
                                                if len(cpf_acom) == 11 and cpf_acom.isdigit() == True:
                                                    print('----------------------')
                                                    print('CADASTRO REALIZADO')
                                                    qtd_clientes += 1
                                                    break
                                                else :
                                                    print('CPF INVÁLIDO')
                                        elif(ac == 2):
                                            print('\n----------------------')
                                            print('  CADASTRO REALIZADO  ')
                                            break
                                        else :
                                            print('Opção inválida!\n')
                                    sleep(2)
                                    break

                # OPÇÃO DOS CLIENTES
                if tam < 30:
                    print('----------------------')
                    print(' CADASTRO DE CLIENTES ')
                    print('----------------------')
                    nome_cli = input('Nome: ')
                    
                    while True:
                        cpf_cli = input('CPF: ')
                        if len(cpf_cli) == 11 and cpf_cli.isdigit() == True:
                            fone_cli = int(input('Telefone: '))
                            print('ENDEREÇO')
                            estado_cli = input('Estado: ')
                            cidade_cli = input('Cidade: ')

                            cliente_nome.append(nome_cli)
                            cliente_cpf.append(cpf_cli)
                            cliente_tele.append(fone_cli)
                            cliente_estado.append(estado_cli)
                            cliente_cidade.append(cidade_cli)
                            cliente_plano.append(plano)
                            break

                        else:
                            print('CPF INVÁLIDO!')

                else:
                    print('------------------------------------------------')
                    print('           AGRACEMOS PELA PREFERÊNCIA           ')
                    print('  INFELIZMENTE ESTAMOS SEM QUARTOS DISPONÍVEIS  ')
                    print('------------------------------------------------')
            
            elif opcao_cliente == 2:
                tam = len(cliente_nome)
                for e in range(tam):
                    print('---------------------')
                    print('  LISTA DE CLIENTES  ')
                    print('---------------------')
                    print(f'NOME = {cliente_nome[e]}')
                    print(f'CPF = {cliente_cpf[e]}')
                    print(f'TELEFONE = {cliente_tele[e]}')
                    print(f'ESTADO = {cliente_estado[e]}')
                    print(f'CIDADE = {cliente_cidade[e]}')
                    print(f'PLANO = {cliente_plano[e]}')            
                    print('----------------------')
                    sleep(5)
                    limpar()

            elif opcao_cliente == 4:
                print('----------------------------')
                print('  LISTA DE CLIENTES LIMPAR  ')
                print('----------------------------')
                cliente_nome.clear()
                cliente_cpf.clear()
                cliente_tele.clear()
                cliente_estado.clear()
                cliente_cidade.clear()
                cliente_plano.clear()
                sleep(5)

            elif opcao_cliente == 0:
                print('----------------------------')
                print('   SAIR LISTA DE CLIENTES   ')
                print('----------------------------')
                sleep(5)

            else :
                print('------------------')
                print('  OPÇÃO INVÁLIDA  ')
                print('------------------')
                sleep(1)

        opcao_cliente = 1
        
    elif opcao == 2:
        
        while opcao_fornecedor != 0:
            
            limpar()
            print('------------------------')
            print('   AREA - FORNECEDORES  ')
            print('------------------------')
            print('--------- MENU ---------')
            print('\n1. CADASTRO')
            print('2. LISTAR')
            print('3. LIMPAR')
            print('0. SAIR')
            fornecedor = int(input('Digite uma opção:'))
            limpar()

            if opcao_fornecedor == 1:
                
                print('---------------------------')
                print(' CADASTRO DE FORNECEDORES  ')
                print('---------------------------')
                nome_dono_for = input('Nome do dono: ')
                nome_em_for = input('Nome da empresa: ')
                
                while True:
                    
                    cnpj = int(input('CNPJ: '))
                    if len(cnpj) == 14 and cnpj.isdigit() == True:
                        print('\nENDEREÇO')
                        estado_for = input('Estado: ')
                        cidade_for = input('Cidade: ')
                        rua_for = input('Rua: ')
                        num_for = input('Número: ')
                        cep_for = input('CEP = ')
                        print('INFORMAÇÕES SOBRE O PRODUTO')
                        produto = input('Nome = ')
                        produto_qtd = int(input('Quantidade = '))
                        produto_val = float(input('Valor = '))
                    else:
                            print('CPF INVÁLIDO!')
                    
                    fornecedores_produto.append(produto)
                    fornecedores_pro_qtd.append(produto_qtd)
                    fornecedores_pro_va.append(produto_val)
                    fornecedores_nome_dono.append(nome_dono_for)
                    fornecedores_nome_em.append(nome_em_for)
                    fornecedores_cnpj.append(cnpj)
                    fornecedores_estado.append(estado_for)
                    fornecedores_cidade.append(cidade_for)
                    fornecedores_rua.append(rua_for)
                    fornecedores_num.append(num_for)
                    print('----------------------')
                    print('CADASTRO REALIZADO')

            elif opcao_fornecedor == 2:
                
                print('-----------------------')
                print(' LISTA DE FORNECEDORES ')
                print('-----------------------')
                tam = len(fornecedores_nome_dono)
                
                for i in range(tam):
                    print(f'NOME DO DONO = {fornecedores_nome_dono[i]}')
                    print(f'NOME DA EMPRESA = {fornecedores_nome_em[i]}')
                    print(f'CNPJ = {fornecedores_cnpj[i]}')
                    print('ENDEREÇO')
                    print(f'ESTADO = {fornecedores_estado[i]}')
                    print(f'CIDADE {fornecedores_cidade[i]}')
                    print(f'RUA = {fornecedores_rua[i]}')
                    print(f'NUMERO = {fornecedores_num[i]}')
                    print('INFORMAÇÕES DO PRODUTO')
                    print(f'NOME DO PRODUTO = {fornecedores_produto[i]}')
                    print(f'QUANTIDADE = {fornecedores_pro_qtd[i]}')
                    print(f'VALOR = {fornecedores_pro_va[i]}')
                    sleep(5)

            elif opcao_fornecedor == 3:
               
                print('-----------------------------')
                print(' LISTA DE FORNECEDORES LIMPA ')
                print('-----------------------------')
                fornecedores_nome_dono.clear()
                fornecedores_nome_em.clear()
                fornecedores_produto.clear()
                fornecedores_pro_qtd.clear()
                fornecedores_pro_va.clear()
                fornecedores_cnpj.clear()
                fornecedores_estado.clear()
                fornecedores_cidade.clear()
                fornecedores_rua.clear()
                fornecedores_num.clear()
                sleep(5)
        
    elif opcao == 3:
    
        print('--------------------')
        print('  RELATÓRIO MENSAL  ')
        print('--------------------')
        print(f'Mês : {meses[3]}')
        print(f'Quantidade de hóspedes atualmente: {qtd_clientes}')
        print(f'Gastos: {gastos}')
        print(f'Ganho bruto: {ganhos}')
        print(f'Lucro liquido: {ganhos - gastos}\n')
        sleep(5)

    elif opcao == 4:
        print('\033[35m-------------------------\033[m')
        print('\033[35m|\033[m    AREA DE ALTERAÇÃO  \033[35m|\033[m')
        print('\033[35m-------------------------\033[m')
        print('  -_- MODIFICAR VALOR-_-')
        print('\n1 - DIÁRIA NO PISO 01.')
        print('2 - DIÁRIA NO PISO 02.')
        
        while(2) :
            
            mod = int(input('\nSUA ESCOLHA: '))
            
            if (mod == 1) :
                antigo_dia1 = estadia_dia
                modificar = int(input('\nQUAL O NOVO VALOR? '))
                estadia_dia = modificar
                print(f'\nVALOR DA DIÁRIA ALTERADO DE: {antigo_dia1} PARA: {modificar}')
                sleep(2)
                break
            
            elif (mod == 2) :
                antigo_dia2 = estadia_dia2
                modificar2 = int(input('\nQUAL O NOVO VALOR? '))
                estadia_dia2 = modificar2
                print(f'\nVALOR DA DIÁRIA ALTERADO DE: {antigo_dia2} PARA: {modificar}')
                sleep(2)
                break
            
            else :
                print('\nValor inválido')

    elif opcao == 0:
        print('-----------------------------')
        print('  AGRADECEMOS A PREFERÊNCIA  ')
        print('-----------------------------')
        sleep(5)
        limpar()
        
    else:
        print('------------------')
        print('  OPÇÃO INVÁLIDA  ')
        print('------------------')
        sleep(1)
        
'''
# Em qua., 13 de abr. de 2022 às 15:53, Pedro Miguel Martins Galdino <pedro.mm.galdino@aluno.senai.br> escreveu:
import os
from time import sleep
from datetime import datetime, date

def limpar():
    os.system('cls')

acompanhante = []
acom_nome = []
acom_cpf = []
acc = 0
clientes = []
cliente_nome = []
cliente_cpf = []
cliente_tele = []
cliente_estado = []
cliente_cidade = []
cliente_plano = []
tam = len(cliente_nome)

qtd_clientes = 0
gastos = 0
ganhos = 0

fornecedores_nome_dono = []
fornecedores_nome_em = []
fornecedores_produto = []
fornecedores_pro_qtd = []
fornecedores_pro_va = []
fornecedores_cnpj = []
fornecedores_estado = []
fornecedores_cidade = []
fornecedores_rua = []
fornecedores_num = []

opcao = 1
opcao_cliente = 1
opcao_fornecedor = 1
nova_op = 0

estadia_dia = 200
estadia_sema = (estadia_dia * 7) - ((estadia_dia * 7)*0.05)
estadia_bisema = (estadia_dia * 14) - ((estadia_dia * 14)*0.06)
estadia_men = (estadia_dia * 30) - ((estadia_dia * 30)*0.08)

estadia_dia2 = 350
estadia_sema2 = (estadia_dia2 * 7) - ((estadia_dia2 * 7)*0.10)
estadia_bisema2 = (estadia_dia2 * 14) - ((estadia_dia2 * 14)*0.15)
estadia_men2 = (estadia_dia2 * 30) - ((estadia_dia2 * 30)*0.20)

while opcao != 0:
    limpar()
    print('----------------------')
    print(' BEM VINDO A POUSADIA ')
    print('----------------------')
    print('--- MENU ---')
    print('1. CLIENTES')
    print('2. FORNECEDORES')
    print('3. RELATÓRIO')
    print('4. CONFIG')
    print('0. SAIR')
    opcao = int(input('Digite uma opção: '))
    limpar()
    
    if opcao == 1:

        while opcao_cliente != 0:
            limpar()
            print('----------------------')
            print(' BEM VINDO A POUSADIA ')
            print('----------------------')
            print('--- MENU ---')
            print('1. CADASTRO')
            print('2. LISTAR')
            print('3. CHECKOUT')
            print('4. LIMPAR')
            print('0. SAIR')
            opcao_cliente = int(input('Digite uma opção:'))
            limpar()

            if opcao_cliente == 1:

                # OPÇÃO DOS CLIENTES
                if tam < 30:
                    print('----------------------')
                    print(' CADASTRO DE CLIENTES ')
                    print('----------------------')
                    nome_cli = input('Nome: ')
                    
                    while True:
                        cpf_cli = input('CPF: ')
                        if len(cpf_cli) == 11 and cpf_cli.isdigit() == True:
                            fone_cli = int(input('Telefone: '))
                            print('ENDEREÇO')
                            estado_cli = input('Estado: ')
                            cidade_cli = input('Cidade: ')
                            while True:    
                                print('----------------------')
                                print('   ESTADIAS   ')
                                print('----------------------')
                                print(f'-  DIÁRIA(piso 1) = R$ {estadia_dia}     - DIÁRIA(piso 2) = R${estadia_dia2}')
                                print(f'1. DIAS                        1. DIAS ')
                                print(f'2. SEMANAL = R$ {estadia_sema}         2. SEMANAL = R$ {estadia_sema2}')
                                print(f'3. BI-SEMANAL = R$ {estadia_bisema}      3. BI-SEMANAL = R$ {estadia_bisema2}')
                                print(f'4. MENSAL = R$ {estadia_men}          4. MENSAL = R$ {estadia_men2}')
                                piso = int(input('\nOpçao -\nPiso: '))
                                estadia = int(input('Plano: '))

                                #piso 1
                                if estadia == 1 and piso == 1:
                                    qtd_dia = int(input('Quantidade de dias: '))
                                    if(qtd_dia>=7 and qtd_dia<14):
                                        if(qtd_dia == 7) :
                                            print('RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO SEMANAL!\nPLANO COM ATÉ 10% DEDESCONTO')
                                            decisao = input('Deseja trocar seu plano? S/N: ')
                                            decisao = decisao.upper()
                                            if decisao == "S":
                                                estadia = 2
                                            else:
                                                print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                                ganhos += qtd_dia * estadia_dia
                                        else:
                                            print(f'RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO SEMANAL + {qtd_dia-7}  diarias!\nPLANOCOM ATÉ 10% DE DESCONTO')
                                            decisao = input('Deseja trocar seu plano? S/N: ')
                                            decisao = decisao.upper()
                                            if decisao == "S":
                                                plano = estadia_dia + ((qtd_dia-7)*estadia_dia) 
                                                ganhos += estadia_dia + ((qtd_dia-7)*estadia_dia)
                                            else:
                                                print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                                ganhos += qtd_dia * estadia_dia
                                    elif(qtd_dia>=14 and qtd_dia<30):
                                        if(qtd_dia == 14) :
                                            print('RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO BI-SEMANAL!\nPLANO COM ATÉ 15% DEDESCONTO')
                                            decisao = input('Deseja trocar seu plano? S/N: ')
                                            decisao = decisao.upper()
                                            if decisao == "S":
                                                estadia = 3
                                            else:
                                                print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                                ganhos += qtd_dia * estadia_dia
                                        else :
                                            print(f'RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO BI-SEMANAL + {qtd_dia-14} diarias!\nPLANO COM ATÉ 15% DE DESCONTO')
                                            decisao = input('Deseja trocar seu plano? S/N: ')
                                            decisao = decisao.upper()
                                            if decisao == "S":
                                                plano = 2.118,20 + ((qtd_dia-14)*estadia_dia)
                                                ganhos += 2.118,20 + ((qtd_dia-14)*estadia_dia)
                                            else:
                                                print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                                ganhos += qtd_dia * estadia_dia
                                    elif(qtd_dia>=30):
                                        if(qtd_dia == 30):
                                            print('RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO MENSAL!\nPLANO COM ATÉ 25% DE DESCONTO')
                                            decisao = input('Deseja trocar seu plano? S/N: ')
                                            decisao = decisao.upper()
                                            if decisao == "S":
                                                estadia = 4
                                            else:
                                                print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                                ganhos += qtd_dia * estadia_dia
                                        else :
                                            print(f'RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO MENSAL + {qtd_dia - 30} diarias\nPLANOCOM ATÉ 25% DE DESCONTO')
                                            decisao = input('Deseja trocar seu plano? S/N: ')
                                            decisao = decisao.upper()
                                            if decisao == "S":
                                                plano = 4.005,00 + ((qtd_dia - 30)*estadia_dia)
                                                ganhos += 4.005,00 + ((qtd_dia - 30)*estadia_dia)
                                            else:
                                                print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                                ganhos += qtd_dia * estadia_dia
                                    else:
                                        print(f'Sua estadia será R$ {qtd_dia * estadia_dia:.2f}')
                                        ganhos += qtd_dia * estadia_dia
                                    plano = f'DIARIA - {qtd_dia} dia(s)\nValor = R$ {qtd_dia*estadia_dia:.2f}'
                                    qtd_clientes+=1
                                elif estadia == 2 and piso == 1:
                                    plano = 'SEMANAL\nValor = R$ estadia_dia'
                                    ganhos += estadia_dia
                                    qtd_clientes+=1
                               
                                elif estadia == 3 and piso == 1:
                                    plano = 'BI - SEMANAL\nValor = R$ 2.118,20'
                                    ganhos += 2.118,20
                                    qtd_clientes+=1
                                
                                elif estadia == 4 and piso == 1:
                                    plano = 'MENSAL\nValor = R$ 4.005,00'
                                    ganhos += 4.005,00
                                    qtd_clientes+=1
                    
                                #piso 2
                                
                                elif estadia == 1 and piso == 2:
                                    qtd_dia = int(input('Quantidade de dias: '))
                                    
                                    if(qtd_dia>=7 and qtd_dia<14):
                                        
                                        if(qtd_dia == 7) :
                                            print('RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO SEMANAL!\nPLANO COM ATÉ 10% DEDESCONTO')
                                            decisao = input('Deseja trocar seu plano? S/N: ')
                                            decisao = decisao.upper()
                                            if decisao == "S":
                                                estadia = 2
                                            else:
                                                print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                                ganhos += qtd_dia * estadia_dia2
                                        
                                        else:
                                            print(f'RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO SEMANAL + {qtd_dia-7}  diarias!\nPLANOCOM ATÉ 10% DE DESCONTO')
                                            decisao = input('Deseja trocar seu plano? S/N: ')
                                            decisao = decisao.upper()
                                            if decisao == "S":
                                                plano = estadia_sema2 + ((qtd_dia-7)*estadia_dia2)
                                                ganhos+= estadia_sema2 + ((qtd_dia-7)*estadia_dia2)
                                            else:
                                                print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                                ganhos += qtd_dia * estadia_dia2
                                    
                                    elif(qtd_dia>=14 and qtd_dia<30):
                                        
                                        if(qtd_dia == 14) :
                                            print('RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO BI-SEMANAL!\nPLANO COM ATÉ 15% DEDESCONTO')
                                            decisao = input('Deseja trocar seu plano? S/N: ')
                                            decisao = decisao.upper()
                                            if decisao == "S":
                                                estadia = 3
                                            else:
                                                print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                                ganhos += qtd_dia * estadia_dia2
                                            
                                        else :
                                            print(f'RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO BI-SEMANAL + {qtd_dia-14} diarias!\nPLANO COM ATÉ 15% DE DESCONTO')
                                            decisao = input('Deseja trocar seu plano? S/N: ')
                                            decisao = decisao.upper()
                                            if decisao == "S":
                                                plano = estadia_bisema2 + ((qtd_dia-14)*estadia_dia2)
                                                ganhos += estadia_bisema2 + ((qtd_dia-14)*estadia_dia2)
                                            else:
                                                print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                                ganhos += qtd_dia * estadia_dia2
                                    elif(qtd_dia>=30):
                                        
                                        if(qtd_dia == 30):
                                            print('RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO MENSAL!\nPLANO COM ATÉ 25% DE DESCONTO')
                                            decisao = input('Deseja trocar seu plano? S/N: ')
                                            decisao = decisao.upper()
                                            if decisao == "S":
                                                estadia = 4
                                            else:
                                                print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                                ganhos += qtd_dia * estadia_dia2
                                        
                                        else :
                                            print(f'RECOMENDAMOS TROCAR SUA ESTADIA PARA NOSSO PLANO MENSAL + {qtd_dia - 30} diarias\nPLANOCOM ATÉ 25% DE DESCONTO')
                                            decisao = input('Deseja trocar seu plano? S/N: ')
                                            decisao = decisao.upper()
                                            if decisao == "S":
                                                plano = estadia_men2 + ((qtd_dia - 30)*estadia_dia2)
                                                ganhos +=  estadia_men2 + ((qtd_dia - 30)*estadia_dia2)
                                            else:
                                                print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                                ganhos += qtd_dia * estadia_dia2
                                    
                                    else:
                                            print(f'Sua estadia será R$ {qtd_dia * estadia_dia2:.2f}')
                                            ganhos += qtd_dia * estadia_dia2
                                    
                                    plano = f'DIARIA - {qtd_dia} dia(s)\nValor = R$ {qtd_dia*estadia_dia2:.2f}'
                                    qtd_clientes += 1
                                
                                elif estadia == 2 and piso == 2:
                                    plano = f'SEMANAL\nValor = {estadia_sema2:.2f}'
                                    ganhos += estadia_sema2
                                    qtd_clientes+=1
                                
                                elif estadia == 3 and piso == 2:
                                    plano = f'BI - SEMANAL\nValor = {estadia_bisema2:.2f}'
                                    ganhos += estadia_bisema2
                                    qtd_clientes+=1
                                
                                elif estadia == 4 and piso == 2:
                                    plano = f'MENSAL\nValor = {estadia_men2:.2f}'
                                    ganhos += estadia_men2
                                    qtd_clientes+=1
                                print('\n DESEJA CADASTRAR ACOMPANHANTE?')
                                while(acc != 1):
                                    ac = input('1 - Sim\n2 - Não\nopção : ')
                                    if(ac == 1):
                                        print('----------------------\nCADASTRAR ACOMPANHANTE')
                                        nome_acom = input('NOME: ')
                                        while True:
                                            cpf_acom = input('CPF: ')
                                            if len(cpf_acom) == 11 and cpf_acom.isdigit() == True:
                                                print('----------------------')
                                                print('CADASTRO REALIZADO')
                                                acc = 1
                                                qtd_clientes += 1
                                                break
                                            else :
                                                print('CPF INVÁLIDO')
                                    elif(ac == 2):
                                        print('----------------------')
                                        print('CADASTRO REALIZADO')
                                        acc = 1
                                    else :
                                        print('Opção inválida!')
                                acc = 0
                                sleep(2)
                                break
                            
                            cliente_nome.append(nome_cli)
                            cliente_cpf.append(cpf_cli)
                            cliente_tele.append(fone_cli)
                            cliente_estado.append(estado_cli)
                            cliente_cidade.append(cidade_cli)
                            cliente_plano.append(plano)
                            break
                        
                        else:
                            print('CPF INVÁLIDO!')

                else:
                    print('-----------------------\nAGRACEMOS PELA PREFERÊNCIA\nINFELIZMENTE ESTAMOS SEM QUARTOS DISPONÍVEIS\n-----------------------')
            
            elif opcao_cliente == 2:
                tam = len(cliente_nome)
                for e in range(tam):
                    print('----------------------')
                    print('  LISTA DE CLIENTES  ')
                    print('----------------------')
                    print(f'NOME = {cliente_nome[e]}')
                    print(f'CPF = {cliente_cpf[e]}')
                    print(f'TELEFONE = {cliente_tele[e]}')
                    print(f'ESTADO = {cliente_estado[e]}')
                    print(f'CIDADE = {cliente_cidade[e]}')
                    print(f'PLANO = {cliente_plano[e]}')            
                    print('----------------------')
                    sleep(5)
                    limpar()

            elif opcao_cliente == 4:
                print('----------------------')
                print('LISTA DE CLIENTES LIMPAR ')
                print('----------------------')
                cliente_nome.clear()
                cliente_cpf.clear()
                cliente_tele.clear()
                cliente_estado.clear()
                cliente_cidade.clear()
                cliente_plano.clear()
                sleep(5)
        
    elif opcao == 2:
        while opcao_fornecedor != 0:
            limpar()
            print('----------------------')
            print(' BEM VINDO A POUSADIA ')
            print('----------------------')
            print('--- MENU ---')
            print('1. CADASTRO')
            print('2. LISTAR')
            print('3. CHECKOUT')
            print('4. LIMPAR')
            print('0. SAIR')
            fornecedor = int(input('Digite uma opção:'))
            limpar()

            if opcao_fornecedor == 1:
                print('----------------------')
                print(' CADASTRO DE FORNECEDORES ')
                print('----------------------')
                nome_dono_for = input('Nome do dono: ')
                nome_em_for = input('Nome da empresa: ')
                while True:
                    cnpj = int(input('CNPJ: '))
                    if len(cnpj) == 14 and cnpj.isdigit() == True:
                        print('\nENDEREÇO')
                        estado_for = input('Estado: ')
                        cidade_for = input('Cidade: ')
                        rua_for = input('Rua: ')
                        num_for = input('Número: ')
                        cep_for = input('CEP = ')
                        print('INFORMAÇÕES SOBRE O PRODUTO')
                        produto = input('Nome = ')
                        produto_qtd = int(input('Quantidade = '))
                        produto_val = float(input('Valor = '))
                fornecedores_produto.append(produto)
                fornecedores_pro_qtd.append(produto_qtd)
                fornecedores_pro_va.append(produto_val)
                fornecedores_nome_dono.append(nome_dono_for)
                fornecedores_nome_em.append(nome_em_for)
                fornecedores_cnpj.append(cnpj)
                fornecedores_estado.append(estado_for)
                fornecedores_cidade.append(cidade_for)
                fornecedores_rua.append(rua_for)
                fornecedores_num.append(num_for)
                print('----------------------')
                print('CADASTRO REALIZADO')

            elif opcao_fornecedor == 2:
                print('----------------------')
                print(' LISTA DE FORNECEDORES ')
                print('----------------------')
                tam = len(fornecedores_nome_dono)
                for i in range(tam):
                    print(f'NOME DO DONO = {fornecedores_nome_dono[i]}')
                    print(f'NOME DA EMPRESA = {fornecedores_nome_em[i]}')
                    print(f'CNPJ = {fornecedores_cnpj[i]}')
                    print('ENDEREÇO')
                    print(f'ESTADO = {fornecedores_estado[i]}')
                    print(f'CIDADE {fornecedores_cidade[i]}')
                    print(f'RUA = {fornecedores_rua[i]}')
                    print(f'NUMERO = {fornecedores_num[i]}')
                    print('INFORMAÇÕES DO PRODUTO')
                    print(f'NOME DO PRODUTO = {fornecedores_produto[i]}')
                    print(f'QUANTIDADE = {fornecedores_pro_qtd[i]}')
                    print(f'VALOR = {fornecedores_pro_va[i]}')
                    sleep(5)

            elif opcao_fornecedor == 4:
                print(' ----------------------')
                print('LISTA DE FORNECEDORES LIMPA ')
                print(' ----------------------')
                fornecedores_nome_dono.clear()
                fornecedores_nome_em.clear()
                fornecedores_produto.clear()
                fornecedores_pro_qtd.clear()
                fornecedores_pro_va.clear()
                fornecedores_cnpj.clear()
                fornecedores_estado.clear()
                fornecedores_cidade.clear()
                fornecedores_rua.clear()
                fornecedores_num.clear()
                sleep(5)
        
    elif opcao == 3:
        print('----------------------\nRELATÓRIO MENSAL\n----------------------')
        print(f'Mês : ')
        print(f'Quantidade de hóspedes atualmente: {qtd_clientes}')
        print(f'Gastos: {gastos}')
        print(f'Lucro bruto: {ganhos}')
        print(f'Lucro liquido: {ganhos - gastos}\n')
        sleep(5)

        
    elif opcao == 0:
        print('----------------------')
        print('AGRADECEMOS A PREFERÊNCIA')
        print('----------------------')

    else:
        print('----------------------')
        print('  OPÇÃO INVÁLIDA  ')
        print('----------------------')
'''