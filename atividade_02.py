"""
ATIVIDADE 02 - FTC
Melhorar o código incluindo: mostrar raiz, folhas, vértices com letras e nível da árvore.

MARLON DA SILVA ROGÉRIO

#include <stdio.h>
#include <math.h>
int main() {
   // 0 - nao se liga e 1 se liga
   int matriz[11][11] = {{0,1,1,0,0,0,0,0,0,0,0},  // vertice a
                         {1,0,0,1,1,1,0,0,0,0,0},  // vertice b
                         {1,0,0,0,0,0,1,1,0,0,0},  // vertice c
                         {0,1,0,0,0,0,0,0,0,0,0},  // vertice d
                         {0,1,0,0,0,0,0,0,1,1,0},  // vertice e
                         {0,1,0,0,0,0,0,0,0,0,0},  // vertice f
                         {0,0,1,0,0,0,0,0,0,0,1},  // vertice g
                         {0,0,1,0,0,0,0,0,0,0,0},  // vertice h
                         {0,0,0,0,1,0,0,0,0,0,0},  // vertice i
                         {0,0,0,0,1,0,0,0,0,0,0},  // vertice j
                         {0,0,0,0,0,0,1,0,0,0,0}}; // vertice k
   int i, j;
   for (i=0;i<11;i++) {
      for (j=0;j<11;j++) {
         if ( matriz[i][j] == 1 ) {
            printf("%d se liga com %d\n", i, j);
         }
      }
   }
}

"""
from abc import ABC


vertices = { 0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K' }
ligacoes = {    
                'A': [0,1,1,0,0,0,0,0,0,0,0],
                'B': [1,0,0,1,1,1,0,0,0,0,0],
                'C': [1,0,0,0,0,0,1,1,0,0,0],
                'D': [0,1,0,0,0,0,0,0,0,0,0],
                'E': [0,1,0,0,0,0,0,0,1,1,0],
                'F': [0,1,0,0,0,0,0,0,0,0,0],
                'G': [0,0,1,0,0,0,0,0,0,0,1],
                'H': [0,0,1,0,0,0,0,0,0,0,0],
                'I': [0,0,0,0,1,0,0,0,0,0,0],
                'J': [0,0,0,0,1,0,0,0,0,0,0],
                'K': [0,0,0,0,0,0,1,0,0,0,0]    
            }   

ligacoes_registradas = []
ligacoes_de_interesse = []

for a in ligacoes:
    for b in ligacoes[a]:
        if b == 1:
            temp = '%s%s'%(a, vertices[ligacoes[a].index(b)])
            temp2 = '%s%s'%(vertices[ligacoes[a].index(b)], a)
            if not temp in ligacoes_registradas and not temp2 in ligacoes_registradas:
                print('%s se liga com %s ' % (a, vertices[ligacoes[a].index(b)]))
                ligacoes_de_interesse.append('%s%s'%(a, vertices[ligacoes[a].index(b)]))
                ligacoes_registradas.append('%s'%(temp))
                ligacoes_registradas.append('%s'%(temp2))

print(ligacoes_de_interesse)

raiz = input('Informe a raiz do grafo: ')
incidencia_elementos = { 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K' :0 }

for a in ligacoes_de_interesse:
    for b in incidencia_elementos:
        if b in a:
            incidencia_elementos[b] += 1

maior_valor = 0
for a in incidencia_elementos:
    if incidencia_elementos[a] == 1 and a != raiz:
        print('%s é FOLHA' % a)
    if incidencia_elementos[a] > maior_valor:
        maior_valor = incidencia_elementos[a]

print('\nO Gráfo tem %d níveis' % maior_valor)    
