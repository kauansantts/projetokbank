from rich import print
from rich.panel import Panel
from random import randint
from time import sleep
import func
import classes

if __name__ == "__main__":

    arq = 'dados.txt'


    
    while True:
        func.cabecalho('MENU PRINCIPAL')
        res = func.menu(['Cadastrar conta', 'Entrar', 'SAIR'])
        if res == 3:
            print(f'[green]{"K-BANK AGRADECE":^40}[/]')
            sleep(0.6)
            break
        
        elif res == 1:
            nome = input('Digite seu nome: ')
            senha = input('Digite sua senha: ')
            saldo = func.leiaFloat('Digite seu saldo:R$')
            cliente = classes.Cliente(nome, senha)
            cliente.cadastrar_cliente(arq, saldo)
        
        elif res == 2:
            usuario = input('Digite seu nome: ')
            senha_usuario = input('Digite sua senha: ')
            cliente = classes.Cliente(usuario, senha_usuario)
            retorno = cliente.login(usuario, senha_usuario, arq)
            if retorno == True:
                resp = ''
                while True:
                    cliente_logado_nome = cliente.nome
                    sleep(0.5)
                    func.cabecalho(f'[green]         BEM VINDO {cliente_logado_nome}[/]')
                    cliente_logado = classes.Conta(cliente)
                    cliente_logado.analise_saldo(arq)
                    res = ''
                    while True:
                        res = input('Quer fazer um planejamento[S/N]: ')
                        while res.upper() not in 'SN':
                            res = input('Quer fazer um planejamento[S/N]: ')
                        if res in 'Ss':
                            painel = Panel('[blue]1[/] - 6 Meses\n[blue]2[/] - 12 Meses', title='[green]PLANEJAMENTO[/]', width=40)
                            print(painel)
                            opc = func.leiaInt('Sua opção: ')
                            while opc not in {1, 2}:
                                opc = func.leiaInt('Sua opção: ')
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
                