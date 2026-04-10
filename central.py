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
        with open(arq, 'at') as arquivo:
            arquivo.write(f'{self.nome_conta}:{self.senha_conta}\n')
            print(f'Novo registro de cliente criado: [red]{self.nome_conta}[/]')

class Login():
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
    
    def verificacao_conta(self, arq):
        with open(arq, 'r') as arquivo:
        
            for linha in arquivo:
                if self.nome in linha and self.senha in linha:
                    print(f'[green]{self.nome} logado com sucesso!![/]')
                    return
            
            print(f'[red]Usuario:{self.nome.upper()}\nSenha:{self.senha.upper()} não cadastrado![/]')
            
class Conta:
    def __init__(self):
        pass # tratar sobre saldo e coisas afins, apos entrar no login do sistema

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
    
    elif res == 2:
        usuario = input('Digite seu nome: ')
        senha_usuario = input('Digite sua senha: ')
        conta = Login(usuario, senha_usuario)
        conta.verificacao_conta(arq)
