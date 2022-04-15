from automato import Automato
from copy import deepcopy


class Simulador:
    def __init__(self, aut: Automato):
        self.aut = aut

    def inicia(self):
        # Verifica cada palavra
        for palavra in self.aut.palavras:
            self.aut.resultados.append(self.resolve_palavra(palavra))

    def resolve_palavra(self, palavra):
        # Caso a palavra tenha transições fora do alfabeto
        for p in palavra:
            if p not in self.aut.vals:
                return "Essa palavra contém valores fora do alfabeto do automato"

        fila = [(self.aut.e_inicial[0], palavra)]  # (estado atual, palavra restante)
        #print(self.aut.r_transicao)
        # print(fila)
        while fila:
            if fila[0][1]:
                for transicao in self.aut.r_transicao[fila[0][0]][fila[0][1][0]]:
                    fila.append((transicao, fila[0][1][1:]))

            if self.aut.tipo == 'e-nfa':
                for transicao in self.aut.r_transicao[fila[0][0]]['E']:
                    fila.append((transicao, fila[0][1][:]))

            # print(fila)


            if fila[0][0] in self.aut.e_final and not fila[0][1]:
                return "O automato consegue ler essa palavra"


            fila.pop(0)
            # print(fila)
            # print()
        return "O automato NÃO consegue ler essa palavra"
