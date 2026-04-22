from rich import print
from rich.panel import Panel
from random import randint
from time import sleep
from classes import *
from central import *



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