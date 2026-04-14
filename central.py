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
        res = ''
        while res in 'Ss':
            res = input('Deseja modificar seu saldo[S/N]: ')

            if res in 'Nn':
                sleep(0.5)
                print(f'[green]SALDO[/]: R${self.saldo_atual}')
                print('[green]Modifique quando quiser![/]')
                print(linha())
                break
            else:
                self.saldo_atual = float(input('R$ '))
                sleep(0.4)
                print(f'[green]NOVO SALDO:[/] R${self.saldo_atual}')
    
    def menu_logado(self, opc):
        match opc:
            case 1:
                valor = float(input('Qual valor para o planejamento:R$ '))
                print(f'Com 6 meses investindo {valor:.2f} seu saldo chega a R${self.saldo_atual + (valor * 6)}')
            case 2:
                valor = float(input('Qual valor para o planejamento:R$ '))
                print(f'Com 12 meses investindo {valor:.2f} seu saldo chega a R${self.saldo_atual + (valor * 12)}')


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
            resp = ''
            while True:
                cliente_logado_nome = cliente.nome
                sleep(0.5)
                cabecalho(f'[green]         BEM VINDO {cliente_logado_nome}[/]')
                cliente_logado = Conta(cliente)
                cliente_logado.analise_saldo()
                res = ''
                while True:
                    res = input('Quer fazer um planejamento[S/N]: ')
                    if res in 'Ss':
                        painel = Panel('[blue]1[/] - 6 Meses\n[blue]2[/] - 12 Meses', title='[green]PLANEJAMENTO[/]')
                        print(painel)
                        opc = int(input('Sua opção: '))
                        cliente_logado.menu_logado(opc)
                        respo = input('Quer continuar[S/N]: ')
                        if respo in 'Nn':
                            break 
                    elif res in 'Nn':
                        break
                resp = input(f'Deseja manipular algo mais em sua conta [green]{cliente_logado_nome}[/]?[SAIR]: ')
                if resp == 'SAIR':
                    retorno = False
                    break 