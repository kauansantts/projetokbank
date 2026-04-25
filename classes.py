from rich import print
from rich.panel import Panel
from random import randint
from time import sleep
import func
from central import *

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
                
    
    def menu_logado(self, res):
        match res:
            case 1:
                valor = func.leiaFloat('Qual valor para o planejamento:R$ ')
                print(f'Com 6 meses investindo {valor:.2f} seu saldo chega a R${self.cliente_logado.saldo_conta + (valor * 6):.2f}')
            case 2:
                valor = func.leiaFloat('Qual valor para o planejamento:R$ ')
                print(f'Com 12 meses investindo {valor:.2f} seu saldo chega a R${self.cliente_logado.saldo_conta + (valor * 12):.2f}')
                
    def alterar_dados(self, arq):
        print(f'[green]CONTA[/]: {self.cliente_logado.nome_conta}\n[green]SENHA[/]: {self.cliente_logado.senha_conta}')
        res = ''
        while res in 'Ss':
            res = input('Deseja modificar algo na sua conta[S/N]: ')
            while res.upper() not in 'SN':
                res = input('[S/N]: ')
            if res in 'Nn':
                sleep(0.5)
                print('[green]Modifique quando quiser![/]')
                break
            else:
                nome_atual = input('Nome: ')
                senha_atual = input('Senha: ')
                linhas = []
                with open(arq, 'r') as arquivo:
                    for linha in arquivo:
                        dados = linha.strip().split(':')
        
                        if dados[0] == self.cliente_logado.nome_conta and dados[1] == self.cliente_logado.senha_conta:
                            linhas.append(f'{nome_atual}:{senha_atual}:{dados[2]}\n')
                        else:
                            linhas.append(linha)
                            
                with open(arq, 'w') as arquivo:
                    arquivo.writelines(linhas)
                sleep(0.4)
                print(f'[green]NOVOS DADOS:[/] Nome:{nome_atual}\nSenha: {senha_atual}')            

                