'''
Nomes com mais de 5 letras (com filter)
Escreva uma função que receba uma lista de nomes e, utilizando filter, retorne
apenas os nomes com mais de 5 letras.
Exemplo de entrada: ["Ana", "Lucas", "Fernanda", "João"]
Exemplo de saída: ["Lucas", "Fernanda"]
'''
lista_nomes = ['Fernando','ana','larissa','joia']
def veri_name(list_name):
    if len(list_name) >= 5:
        return True
    else:
        return False


list_name = list(filter(veri_name,lista_nomes))

print(list_name)