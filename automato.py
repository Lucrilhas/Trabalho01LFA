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
