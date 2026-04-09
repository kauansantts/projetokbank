from rich import print
from rich.panel import Panel
from rich.table import Table
from random import randint
from time import sleep

arq = 'dados.txt'


class Cliente:
    def __init__(self, nome, senha):
        self.nome_conta = nome
        self.senha_conta = senha
        self.clientes = []

    def cadastrar_cliente(self, arq):
        a = open(arq, 'at')
        a.write(f'Nome:{self.nome_conta} [{self.senha_conta}]\n')
        a.close()
        print(f'Novo registro de cliente criado: [red]{self.nome_conta}[/]')

class Conta:
    def __init__(self):
        pass         #usar como funcao de entrar no sistema --- 2 - Entrar



def linha(l=40):
    return '-'* l

def cabecalho(msg):
    print(linha())
    print(f'[green]{msg.center(40)}[/]')
    print(linha())

def leiaInt(numero):
    while True:
        try:
            n = int(input(numero))
        except(ValueError, TypeError):
            print('[red]ERRO!Digite um numero valido.[/]')
            continue
        else:
            return n

def menu(opcoes):
    cabecalho('OPÇÕES')
    c = 1
    for v in opcoes:
        print(f'{c} - {v}')
        c+=1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc


   
cabecalho('MENU PRINCIPAL')
while True:
    res = menu(['Cadastrar conta', 'Entrar', 'SAIR'])
    if res == 3:
        print(f'[green]{"K-BANK AGRADECE":^40}[/]')
        sleep(0.6)
        break
    
    elif res == 1:
        nome = input('Digite seu nome: ')
        senha = input('Digite sua senha: ')
        cliente = Cliente(nome, senha)
        cliente.cadastrar_cliente(arq)
