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
                while True:
                    cliente_logado_nome = cliente.nome
                    sleep(0.5)
                    func.cabecalho(f'[green]         BEM VINDO {cliente_logado_nome}[/]')
                    cliente_logado = classes.Conta(cliente)
                    painel = Panel('[blue]1[/] - Modificar/ver saldo\n[blue]2[/] - Fazer planejamento\n[blue]3[/] - Alterar conta\n[blue]4[/] - Apagar conta\n[blue]5[/] - Sair', title='[green]MENU LOGADO[/]', width=40)
                    print(painel)
                    opc = func.leiaInt('Sua opção: ')
                    while opc not in {1, 2, 3, 4, 5}:
                            opc = func.leiaInt('Sua opção: ')
                    match opc:
                        case 1:
                            cliente_logado.analise_saldo(arq)
                        case 2:
                            painel2 = Panel('[blue]1[/] - 6 Meses\n[blue]2[/] - 12 Meses', title='[green]PLANEJAMENTO[/]', width=40)
                            print(painel2)
                            res = func.leiaInt('Sua opção: ')
                            while res not in {1, 2}:
                                 res = func.leiaInt('Sua opção: ')   
                            cliente_logado.menu_logado(res)
                        case 3:
                            cliente_logado.alterar_dados(arq)
                        case 4:
                            cliente_logado.excluirConta(arq)
                            break
                            
                        case 5:
                            print(f'[green]SAINDO DA CONTA {cliente_logado_nome}[/]')
                            print('LOADING....')
                            sleep(0.7)
                            break
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
