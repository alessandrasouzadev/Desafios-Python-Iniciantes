filme1 = {'título': 'Star Wars',
            'ano': 1977,
            'diretor': 'George Lucas'}
filme2 = {'título': 'Avengers',
          'ano': 2012,
          'diretor': 'Joss Whedon'
          }
filme3 = {'título': 'Matrix',
       'ano': 1999,
       'diretor': 'Wachowski'
}#COMO CRIAR UM DICIONARIO
dados = dict()
dados = {'nome': 'Pedro', 'idade': 22}
print(dados['nome'])
print(dados['idade'])

#COMO ADICIONAR ELEMENTO(KEYS) AO DICIONARIO 
dados['sexo'] = 'M'

#COMO REMOVER ELEMENTOS
del dados ['idade']

#COMO RETORNAR TODOS OS VALORES(CONTEÚDOS)
print(dados.values())

#COMO RETORNAR TODOS OS TITULOS (CHAVES)
print(dados.keys())

#COMO RETORNAR TODOS OS VALORES+CHAVES
print(dados.items())

#COMO UTILIZAR DENTRO DO 'FOR'
for k, v in dados.items():
    print(f'O{k} é {v}')

#EXISTE A POSSIBILIDADE DE JUNÇÃO COM LISTA+DICIONÁRIOS+TUPLAS

locadora = dict()
locadora = {'título', 'ano', 'diretor' }
locadora ['título'] = 'Star Wars', 'Avengers', 'Matrix'
locadora ['ano'] = 1977, 2012, 1999
locadora ['diretor'] = 'George Lucas', 'Joss Whedon', 'Wachowski'
print(locadora)
#não funciona pratica, se sobresceve

#EXEMPLO DE DICIONÁRIO DENTRO DE LISTA


locadora = []
filme1 = {'título': 'Star Wars',
            'ano': 1977,
            'diretor': 'George Lucas'}
filme2 = {'título': 'Avengers',
          'ano': 2012,
          'diretor': 'Joss Whedon'
          }
filme3 = {'título': 'Matrix',
       'ano': 1999,
       'diretor': 'Wachowski'
}

locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)

for i in range(0,len(locadora)):
    print(f'O filme é: {locadora[i]}')

#BUSCA DE LISTA(X) NA POSIÇÃO DE DICIONÁRIO 

print(locadora[0]['título'])

#NESSE EXEMPLO OS DADOS ESTÃO SENDO SOBRESCRITOS E NÃO ADICIONADOS
filmes = dict()
filmes = {'título': 'Star Wars',
            'ano': 1977,
            'diretor': 'George Lucas'}
filmes = {'título': 'Avengers',
          'ano': 2012,
          'diretor': 'Joss Whedon'
          }
filmes = {'título': 'Matrix',
          'ano': 1999,
          'diretor' :'Wachowski'}
print(filmes)

#PARA REFERENCIAR A CHAVE É NECESSÁRIO UTILIZAR ASPAS DUPLAS
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

#OBSERVAÇÃO (items = enumerate)

#CUIDADO: PARA NÃO SOBRESCREVER DADOS, PARA QUE ISSO NÃO ACONTEÇA SERIA NECESSÁRIO REALIZAR UM FATIAMENTO MAS ISSO NÃO É ACEITÁVEL NOS DICIONÁRIOS, ENTÃO TERÁ QUE USAR UM METÓDO PRÓPRIO PARA OS DICIONÁRIOS 'copy()'
estado = dict()
brasil = list()
for c in range(0,2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

#ORDENANDO DICIONÁRIOS PELOS VALORES
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(0,6),
        'Jogador2': randint(0,6),
        'Jogador3': randint(0,6),
        'Jogador4': randint(0,6),
        }
ranking = dict()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)