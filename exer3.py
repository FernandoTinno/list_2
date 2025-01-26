from functools import reduce

'''
3. Somar os números de uma lista (com reduce)
Crie uma função que, utilizando reduce e uma função lambda, receba uma lista de
números inteiros e retorne a soma total dos números.
Exemplo de entrada: [1, 2, 3, 4]
Exemplo de saída: 10

'''

num_list = [1,2,3,4,5]
teste = [2,5,7,9]
new_list = reduce(lambda x,y: x+y,num_list)

print(new_list)