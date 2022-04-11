class Automato:
    def __init__(self):
        self.estados = []
        self.r_transicao = []
        self.e_inicial = []
        self.e_final = []
        self.vals = []
        self.tipo = 'dfa'
        self.palavras = []
        self.resultados = []

    # Imprime os valores do automato
    def printa_automato(self):
        print(f"Estados: {sorted(self.estados)}\n"
              f"Regras de Transição: {self.r_transicao}\n"
              f"Estado inicial: {self.e_inicial}\n"
              f"Estado final: {self.e_final}\n"
              f"Alfabeto: {self.vals}\n"
              f"Palavras: {self.palavras}\n"
              f"Tipo: {self.tipo}\n"
              f"Resultados: {self.resultados}")

    # Organiza
    def organiza(self):
        self.estados = sorted(self.estados)
        self.e_final = sorted(self.e_final)
        self.palavras = sorted(self.palavras)
        self.vals = sorted(self.vals)
        for e in self.estados:
            for v in self.vals:
                self.r_transicao[e][v] = sorted(self.r_transicao[e][v])


class DFA:
    def __init__(self, aut: Automato):
        self.aut = aut

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


def nfa_to_dfa(aut: Automato):
    # Cria novos estados a partir de entrada com mais de uma resposta
    for e in aut.estados[:]:
        for v in aut.vals:
            if len(aut.r_transicao[e][v]) > 1:
                aut.r_transicao[e][v] = [''.join(elem for elem in aut.r_transicao[e][v])]
                if (novo_estado := aut.r_transicao[e][v][0]) not in aut.estados:
                    aut.estados.append(novo_estado)

                    # Verifica se esse novo estado é final
                    for f in aut.e_final:
                        if f in novo_estado:
                            aut.e_final.append(novo_estado)
                            break

                    # Cria novas regras de transição para esse estado - Por enquanto vazias
                    aut.r_transicao[novo_estado] = {v: [] for v in aut.vals}


    # Preenche as regras de transições vazias
    for v in aut.vals:
        num_estados = len(aut.estados)
        for i in range(0, num_estados):
            for j in range(i + 1, num_estados):
                if aut.estados[i] in aut.estados[j]:
                    aut.r_transicao[aut.estados[j]][v] = uniao(aut.r_transicao[aut.estados[j]][v],
                                                               aut.r_transicao[aut.estados[i]][v])


def uniao(x: list, y: list):
    if len(x) == 0:
        return y
    if len(y) == 0:
        return x
    if x[0] in y[0]:
        return y
    if y[0] in x[0]:
        return x
    return [x[0] + y[0]]