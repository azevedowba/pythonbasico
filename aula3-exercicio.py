'''EXERCICIO
PARA ENTRAR NO EXERCITO É PRECISO TER:
    - MAIS DE 18 ANOS
    - PESAR MAIS OU IGUAL DE 60kg
    - MEDIR  MAIS OU IGUAL 1.70 METROS

Faça um programa que pergunte a idade o peso e a altura de uma pessoa
e decide se ela está apta a ser do exército.
'''

nome = input('Qual seu nome? ')
print('Olá! ',nome)

idade = int(input('Qual sua idade? ')) # converte a idade em um NUMERO inteiro
peso = float(input('Qual seu peso? ')) # converte o peso em um NUMERO "quebrado" / float
altura = float(input('Qual sua altura? ')) # converte a altura em um NUMERO "quebrado" / float

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('VOCÊ ESTÁ __ APTO __ PARA ENTRAR NO EXÉRCITO!!')
else:
    print('VOCÊ FOI -- REPROVADO -- PARA O EXÉRCITO!!')