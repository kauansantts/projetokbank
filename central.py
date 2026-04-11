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
    
    def login(self,nome, senha, arq):
        self.nome = nome
        self.senha = senha
        with open(arq, 'r') as arquivo:
            for linha in arquivo:
                if self.nome in linha and self.senha in linha:
                    return True
                else:
                    sleep(0.5)
                    print(f'[red]Usuario:{self.nome.upper()}\nSenha:{self.senha.upper()} não cadastrado![/]')
                    return False
  


class Conta:
    
    saldo_atual = 0
    
    def __init__(self, cliente):
        self.cliente_logado = cliente
        res = ''
    
    def analise_saldo(self):
        print(f'[green]SALDO[/]: R${self.saldo_atual}')
        res = input('Deseja modificar seu saldo[S/N]: ')
        if res in 'Ss':
            self.saldo_atual = float(input('R$ '))  
            print(f'[green]SALDO:[/] R${self.saldo_atual}')
        elif res in 'Nn':
            print('[green]Modifique quando quiser![/]')


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
        cliente = Cliente(usuario, senha_usuario)
        retorno = cliente.login(usuario, senha_usuario, arq)
        if retorno == True:
            res = ''
            while res.upper() in 'SAIR':
                cliente_logado_nome = cliente.nome
                cliente_logado = cliente
                sleep(0.5)
                cliente_logado = Conta(cliente_logado)
                painel = Panel(f'', title=f'[green]Bem vindo, {cliente_logado_nome}![/]') #CONTINUAR ESSE RACIOCIONIO DE MOSTRAR TUDO EM UM PAINEL
                print(painel)
                res = input('Quer continuar[S/N]: ')
                if res in 'Nn':
                    break