"""
Programa: soma003
Descrição: Este programa le dois números digitados no teclado e imprime na tela a sua soma. Esta versão introduz o uso de f-strings
Autor: Filipe
Data: 02/06/2023
Versão: 0.0.3
"""

#Atribuição de variáveis


#Entrada de dados
numero_1 = float(input("Digite a primeira parcela: "))
numero_2 = float(input("Digite a segunda parcela: "))

#Processamento de dados
soma = (numero_1 + numero_2)

#Saida de dados
print(f"O resultado da soma do número {numero_1} com o número {numero_2} é igual a {soma}")