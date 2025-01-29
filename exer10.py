'''
. Média ponderada com dicionário e reduce
Crie uma função que receba um dicionário onde as chaves são nomes de alunos e
os valores são listas de notas (com pesos na última posição). A função deve calcular
a média ponderada de cada aluno usando reduce e retornar um novo dicionário
com os resultados.
Exemplo de entrada:
{
 "João": [8, 7, 9, 2], # (notas: 8, 7, 9; peso: 2)
 "Ana": [5, 6, 7, 3] # (notas: 5, 6, 7; peso: 3)
}
Exemplo de saída:
{
 "João": 8.0,
 "Ana": 6.0
}
'''
from functools import reduce


def ponder():
    dictionary = {'fernando': [7,8,9,2],'larissa':[5,6,7,3]}
    
    note_f = dictionary['fernando'][:-1]#definir que o ultimo numero será o peso, logo o restante será a nota do aluno(a)
    note_l = dictionary['larissa'][:-1]
    
    weight_f = dictionary['fernando'][-1] #define o peso das notas, que seria o ultimo valor da lista
    weight_l = dictionary['larissa'][-1]
    
    total_note_f = reduce(lambda x, y: x + y * weight_f, note_f, 0)#multiplica as notas por 2 e somam, gerando a nota final do aluno exp 2+3+4 -> 4+6+8 = 18, defini y como 0 pois precisava de 2 argumentos e se caso eu definise um valor para y a conta ficaria incoreta
    total_note_l = reduce(lambda x, y: x + y * weight_l, note_l, 0)
    
    total_weight_f = dictionary['fernando'][-1] * len(dictionary['fernando'][:-1])# serve para gerar o valor que ira dividir a nota final. que posteriormente ira gerar a media, já que media ponderada seria o valor de cada nota do aluno sobre o peso e após isso, dividir pela quantidade de notas vezes o peso.
    total_weight_l = dictionary['larissa'][-1] * len(dictionary['larissa'][:-1])
    
    new_dictionary = {'fernando': total_note_f / total_weight_f, 'larissa': total_note_l / total_weight_l}#realiza a divisão da nota final e do peso final para assim gerar a media do aluno(a)
    
    
    
    return new_dictionary
    #print(media_f)
    
    

print(ponder())
    