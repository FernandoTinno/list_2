'''
Contar letras em uma lista de palavras (com map e reduce)
Crie uma função que receba uma lista de palavras e retorne a soma total de letras
em todas as palavras, utilizando map para contar as letras e reduce para somar.
Exemplo de entrada: ["casa", "python", "lambda"]
Exemplo de saída: 16
'''
from functools import reduce


def plus_words(name_list):
    name_list_number = list(map(len,name_list))#a variavel map serve para realizar alguma alteração nos itens de uma variavel, por isso que deve se colocar a ação que deseja como o len e depois colocar a variavel que deseja alterar
    
    final_name_list = reduce(lambda x,y: x+y,name_list_number)
    return final_name_list

name_list = ['map','python','lambda','filter','reduce']

print(plus_words(name_list))