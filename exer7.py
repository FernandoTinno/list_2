'''
Agrupar números em categorias (com dicionários e lambdas)
Escreva uma função que receba uma lista de números inteiros e utilize map e filter
para criar um dicionário que agrupe os números em três categorias:
o "positivos" (números maiores que 0)
o "negativos" (números menores que 0)
o "zeros" (números iguais a 0).
o Exemplo de entrada: [1, -2, 0, 3, -5, 0]
o Exemplo de saída: {"positivos": [1, 3], "negativos": [-2, -5], "zeros": [0, 0]}
'''

def dictionary_categories(num_list):
    
    separed_dictionary = {'positos':list(filter(lambda x: x > 0,num_list)),'negativos':list(filter(lambda x: x < 0,num_list)),'zeros':list(filter(lambda x: x == 0,num_list))}
    return separed_dictionary

num_list =[1, -2, 0, 3, -5, 0]

print(dictionary_categories(num_list))

#não consegui pensar em alguma maneira de incrementar o map, até perguntei por curiosidade para o chat e ele me retornou informando que não havia nescessidade de ultilizar