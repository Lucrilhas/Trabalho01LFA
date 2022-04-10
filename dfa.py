from automato import Automato

class DFA:
    def __init__(self, aut: Automato):
        self.aut = automato

        for p in aut.palavras:
            self.aut.resultados.append(self.le_palavra(p))

    def le_palavra(self, palavra):
        for p in palavra:
            if p not in self.aut.vals:
                return 'Essa palavra contém valores fora do alfabeto do automato'

        e_atual = self.aut.e_inicial
        for letra in palavra:
            if len(self.aut.r_transicao[e_atual[0]][letra]) == 0:
                return 'O automato NÃO consegue ler essa palavra'
            e_atual = self.aut.r_transicao[e_atual[0]][letra]

        if e_atual[0] in self.aut.e_final:
            return 'O automato consegue ler essa palavra'
        else:
            return 'A palavra não termina em um estado final, logo não é aceitavel'

