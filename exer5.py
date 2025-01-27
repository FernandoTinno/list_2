'''
Elevar números ao quadrado e ordenar (com map e sorted)
Crie uma função que eleve ao quadrado todos os números de uma lista, utilizando
map, e depois retorne a lista ordenada.
Exemplo de entrada: [3, 1, 4, 2]
Exemplo de saída: [1, 4, 9, 16]
'''

def ordened_list(list):
    square_list = [] 
    ordened = sorted(list)
    for num in ordened:
        square_list.append(num**2)
    return square_list

num_list = [2,1,5,3,6]
resultado = ordened_list(num_list)
print(resultado) 


#eu fiz com lambda primeiro, depois li de novo o enunciado e não constava o uso do lambda, então fiz outro mas deixei comentado o com lambda

#num_list = [2,1,5,3,6]

#new_list = list(map(lambda x: x **2,sorted(num_list)))

#print(new_list)

    
    