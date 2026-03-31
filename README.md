# projetokbank
projeto de treino 

# Projeto KBank

Sistema bancário simples em Python

## Funcionalidades
- Depósito
- Saque
- Consulta de saldo


-----------------------------------------------------------------------------------------------------
Para vizualização
def leiaInt(numero):
    while True:
        try:
            n = int(input(numero))
        except(ValueError, TypeError):
            print('\033[31mERRO!Digite um numero valido.\033[m')
            continue
        else:
            return n


def linha(lin=40):
    return '-' * lin

def cabecalho(texto):
    print(linha())
    print(f'\033[034m{texto.center(40)}\033[m')
    print(linha())
    
def menu(lista):
    c = 1
    for v in lista:
        print(f'\033[034m{c} - {v}\033[m')
        c+=1
    print(linha())
    opc = leiaInt('\033[032mSua opção: \033[m')
    return opc

def criarArquivo(nome):
    a = open(nome, 'wt+')
    a.close()

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except (FileNotFoundError):
        return False
    else:
        return True

def lerArquivo(nome):
    a = open(nome, 'rt')
    cabecalho('PESSOAS CADASTRADAS')
    print(f'{"\033[33mNOME":<36}IDADE\033[m')
    for linhatxt in a:
        print(f'{linhatxt.strip()} anos')
    print(linha())
    a.close()    


def cadastrarPessoa(arq, nome='desconhecido', idade=0):
    a = open(arq, 'at')
    a.write(f'{nome:<30}{idade}\n')
    a.close()
     

arq = 'kauanArqui.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

cabecalho('MENU PRINCIPAL')
while True:
    time.sleep(0.9)
    res =  menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if res == 1:
        time.sleep(0.6)
        lerArquivo(arq)
    elif res == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrarPessoa(arq, nome, idade)
        print(f'Novo registro de {nome} adicionado.')
        print(linha())
    elif res == 3:
        cabecalho('Saindo do sistema...')
        time.sleep(0.6)
        break




# class contaBancaria:
    
#     def __init__(self, id, nome, saldo = 0):
#         self.id = id
#         self.titular = nome
#         self.saldo = saldo
#         print(f'Conta {self.id} criada com sucesso. Saldo atual da conta de R${self.saldo:,.2f}')
    
#     def __str__(self):
#         return f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo"
    
#     def depositar(self, valor):
#         self.saldo += valor
#         print(f'Deposito de R${valor:.2f} efetuado com sucesso. Saldo total atual R${self.saldo:,.2f}')
        
#     def sacar(self, saque):
#         if saque > self.saldo:
#             print(f'\033[31mSaque de R${saque:,.2f} na conta {self.id} NEGADO. Saldo insuficiente!\033[m')
#         else:
#             self.saldo -= saque
#             return f"Voce sacou R${saque:,.2f}. Total da conta = R${self.saldo:.2f}"
    
# c1 = contaBancaria(112, "Kauan", 3000)
# c1.depositar(500)
# print(c1)
# print(c1.sacar(10000))

from rich import print
from rich.panel import Panel #Nesse caso Panel seria uma classe que faz esse painel.. e nesse exercicio eu usei msg como objeto para mostrar o que a Classe faz... nas importações, o import que vier com letra maiuscula exemplo esse Panel.. siginifica que é uma classe!
from rich.table import Table #classe de criar tabelas
from rich import inspect #para ler manual de comandos para estuda-los

# #PAINEL
# print("[bold red]Funcionando![/] :earth_americas: :grinning_face_with_sweat:") 
# msg = Panel("[blue] PAINEL DE EXEMPLO[/]", title='Mensagem', style='red', width=40)
# print(msg)
# print(Panel.__doc__)

# #TABELA
# tabela = Table(title='Teste', style='green')
# tabela.add_column('Preco')
# tabela.add_column('Nome')
# tabela.add_row('[red]1,40[/]', '[red]lapis[/]')
# print(tabela)

# #INSPECT
# inspect(int)

https://github.com/kauansantts/projetokbank.git
-----------------------------------------------------------------------------------------------------
