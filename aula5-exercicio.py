''' 
- Faça um programa que leia a quantidade de pessoas que serao
convidadas para uma festa.
- Após isso o programa irá perguntar o nome de todas as pessoas e colocar
em uma lista de convidados
- Após irá imprimir todos os nomes da lista.
'''


numero_convidados = input('Qual a quantidade de convidados você deseja? ')
lista_convidados = []

i = 1
while i <= int(numero_convidados):
    nome_do_convidado = input('Coloque o nome do convidado #'+ str(i) +': ')
    lista_convidados.append(nome_do_convidado)
    i += 1

print('Serão', numero_convidados, 'convidados')
print('\nLISTA DE CONVIDADOS')

for convidado in lista_convidados:
    print(convidado)