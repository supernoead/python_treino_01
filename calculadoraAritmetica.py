from os import system, name
#CALCULADORA ARITMÉTICA SIMPLES
#Matheus Phelipe, 2020

#------------VARIÁVEIS GLOBAIS
isAtiva = True #variável define que nossa aplicação está sendo executada
historico = [] #lista que contém o histórico dos cálculos

#------------FUNÇÕES BÁSICAS

def somar(a,b):
    return a + b

def subtrair(a, b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a, b):
    try:
        return a/b
    except :
        return "Impossível efetuar divisão. Valor indeterminado para divisão por 0 (zero)."

def verHistorico():
    resultado = ">>>Histórico de operações\n"
    for x in historico:
        resultado += x +"\n"
    return resultado

def obterValores():
    value1 = float(input("Valor 1: "))
    value2 = float(input("Valor 2: "))
    return (value1, value2)

def selecionarFuncao(funcao):
    # 0 > usuário deseja sair
    # -1 > usuário informou opção inválida

    if(funcao>=1 and funcao<=4): #valor informado é um novo cálculo!
        valor1, valor2 = obterValores() #neste método, obteremos os valores para serem computados
        if(funcao==1):
            resultado = f'Somar: {valor1} + {valor2} = {somar(valor1, valor2)}'
        elif(funcao==2):
            resultado = f'Subtrair: {valor1} - {valor2} = {subtrair(valor1, valor2)}'
        elif(funcao==3):
            resultado = f'Multiplicar: {valor1} * {valor2} = {multiplicar(valor1, valor2)}'
        elif(funcao==4):
            resultado = f'Dividir: {valor1} / {valor2} = {dividir(valor1, valor2)}'
        
        #como foi feita uma nova operação, salvamos na lista
        historico.append(resultado)   
        return historico[-1] #e retornamos a última opção feita pelo usuário
    elif(funcao==5): #usuário deseja apenas ver o histórico
        return verHistorico()
    else: #caso contrário, devemos informar ao usuário que ele deve tentar novamente
        return "Comando Inválido. Tente novamente!"


def menu():
    texto = '''>>>>>>CALCULADORA ARITMÉTICA SIMPLES<<<<<<\n=========================================\nSelecione uma opção abaixo para continuar\n=========================================\n
        (1) - Somar
        (2) - Subtrair
        (3) - Multiplicar
        (4) - Dividir
        (5) - Ver histórico
        (6) - Sair\n'''
    print(texto)
    return int(input("Digite sua opção: "))


def limparTela():
    # para ambientes Windows
    if name == 'nt': #para 
        system('cls') 
    # para ambientes Mac ou Linux
    else: 
        system('clear') 

#------------LOOP PRINCIPAL


while(isAtiva):
    opcao = menu()
    if(opcao==6):
        isAtiva = False
        print("Encerrando aplicação...\nAté a próxima! :)")
    else:
        limparTela()
        print(selecionarFuncao(opcao))
        



