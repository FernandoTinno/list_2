'''
Filtrar tuplas com média maior que 5
Escreva uma função que receba uma lista de tuplas, onde cada tupla contém
números inteiros. Utilize map e filter para filtrar as tuplas cuja média dos valores
seja maior que 5.
Exemplo de entrada: [(2, 8), (4, 5, 6), (1, 2)]
Exemplo de saída: [(2, 8), (4, 5, 6)]
'''

def media_filter(tupla_list):
   
      
    filter_list = list(filter(lambda x:sum(x)/len(x) >=5,tupla_list ))
        
    return filter_list
    

tupla_list = [(2,8),(4,5,6),(1,2)]

print(media_filter(tupla_list))