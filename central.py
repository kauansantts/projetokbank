from rich import print
from rich.panel import Panel
from random import randint
from time import sleep

arq = 'dados.txt'


class Cliente:
    def __init__(self, nome, senha):
        self.nome_conta = nome
        self.senha_conta:float = senha

    def cadastrar_cliente(self, arq, saldo):
        self.saldo_conta = saldo
        with open(arq, 'at') as arquivo:
            arquivo.write(f'{self.nome_conta}:{self.senha_conta}:{self.saldo_conta}\n')
            print(f'Novo registro de cliente criado: [red]{self.nome_conta}[/]')
    
    def login(self,nome, senha, arq):
        self.nome = nome
        self.senha = senha
        with open(arq, 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(':')

                if self.nome == dados[0] and self.senha == dados[1]:
                    self.saldo_conta = float(dados[2])
                    return True
            print(f'[red]Usuario:{self.nome.upper()}\nSenha:{self.senha.upper()} não cadastrado![/]')
            return False
  


class Conta:
    def __init__(self, cliente):
        self.cliente_logado = cliente
        self.saldo_atual = self.cliente_logado.saldo_conta
        res = ''
    
    def analise_saldo(self, arq):
        print(f'[green]SALDO[/]: R${self.cliente_logado.saldo_conta}')
        res = ''
        while res in 'Ss':
            res = input('Deseja modificar seu saldo[S/N]: ')
            while res.upper() not in 'SN':
                res = input('Deseja modificar seu saldo[S/N]: ')
            if res in 'Nn':
                sleep(0.5)
                print(f'[green]SALDO[/]: R${self.cliente_logado.saldo_conta}')
                print('[green]Modifique quando quiser![/]')

                break
            else:
                self.cliente_logado.saldo_conta = float(input('R$ '))
                linhas = []

                with open(arq, 'r') as arquivo:
                    for linha in arquivo:
                        dados = linha.strip().split(':')

                        if dados[0] == self.cliente_logado.nome_conta and dados[1] == self.cliente_logado.senha_conta:
                            linhas.append(f'{dados[0]}:{dados[1]}:{self.cliente_logado.saldo_conta}\n')
                        else:
                            linhas.append(linha)

                with open(arq, 'w') as arquivo:
                    arquivo.writelines(linhas)
                sleep(0.4)
                print(f'[green]NOVO SALDO:[/] R${self.cliente_logado.saldo_conta}')
                
    
    def menu_logado(self, opc):
        match opc:
            case 1:
                valor = leiaFloat('Qual valor para o planejamento:R$ ')
                print(f'Com 6 meses investindo {valor:.2f} seu saldo chega a R${self.cliente_logado.saldo_conta + (valor * 6):.2f}')
            case 2:
                valor = leiaFloat('Qual valor para o planejamento:R$ ')
                print(f'Com 12 meses investindo {valor:.2f} seu saldo chega a R${self.cliente_logado.saldo_conta + (valor * 12):.2f}')


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
        
def leiaFloat(numero):
    while True:
        try:
            n = float(input(numero))
        except(ValueError, TypeError):
            print('[red]ERRO!Digite um numero valido.[/]')
            continue
        else:
            return n

def menu(opcoes):
    c = 1
    for v in opcoes:
        print(f'{c} - {v}')
        c+=1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc

   
while True:
    cabecalho('MENU PRINCIPAL')
    res = menu(['Cadastrar conta', 'Entrar', 'SAIR'])
    if res == 3:
        print(f'[green]{"K-BANK AGRADECE":^40}[/]')
        sleep(0.6)
        break
    
    elif res == 1:
        nome = input('Digite seu nome: ')
        senha = input('Digite sua senha: ')
        saldo = leiaFloat('Digite seu saldo:R$')
        cliente = Cliente(nome, senha)
        cliente.cadastrar_cliente(arq, saldo)
    
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
                cliente_logado.analise_saldo(arq)
                res = ''
                while True:
                    res = input('Quer fazer um planejamento[S/N]: ')
                    while res.upper() not in 'SN':
                        res = input('Quer fazer um planejamento[S/N]: ')
                    if res in 'Ss':
                        painel = Panel('[blue]1[/] - 6 Meses\n[blue]2[/] - 12 Meses', title='[green]PLANEJAMENTO[/]', width=40)
                        print(painel)
                        opc = leiaInt('Sua opção: ')
                        while opc not in {1, 2}:
                            opc = leiaInt('Sua opção: ')
                        cliente_logado.menu_logado(opc)
                        respo = input('Quer continuar[S/N]: ')
                        while respo.upper() not in 'SN':
                            respo = input('Quer continuar[S/N]: ')
                        if respo in 'Nn':
                            break 
                    elif res in 'Nn':
                        break
                resp = input(f'Deseja manipular algo mais em sua conta {cliente_logado_nome}?[S/N] ')
                while resp.upper() not in 'SN':
                    resp = input('[S/N]: ')
                if resp in 'Nn':
                    break 