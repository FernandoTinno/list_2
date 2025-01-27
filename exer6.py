'''
Dicionário de números pares e ímpares
Escreva uma função que receba uma lista de números inteiros e utilize lambda e
filter para dividir a lista em números pares e ímpares. Retorne um dicionário com
duas chaves: "pares" e "ímpares".
Exemplo de entrada: [1, 2, 3, 4, 5, 6]
Exemplo de saída: {"pares": [2, 4, 6], "ímpares": [1, 3, 5]}
'''

def odd_even(num_list):

    odd = list(filter(lambda x: x %2 == 1,num_list))#filtrando somente os numeros que o resto da divisão será 1,logo numeros ímpares
    even = list(filter(lambda x: x %2 == 0,num_list))#mesma função mas para filtrar agora os numeros pares
    
    separed_dictionary = {'ímpares': odd,'pares': even}
    return separed_dictionary


num_list =[1,2,3,4,5,6]

print(odd_even(num_list))
     
     
        

        
