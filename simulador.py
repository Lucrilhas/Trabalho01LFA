from automato import Automato

# Classe simulador que ira verifica quais palavras funcionam em um automato
class Simulador:
    def __init__(self, aut: Automato):
        self.aut = aut  # Recebe o automato

    def inicia(self):   # Incia o procedimento
        # Verifica cada palavra e salva a resposta em resultados do automato
        for palavra in self.aut.palavras:
            self.aut.resultados.append(self.resolve_palavra(palavra))

    # Verificador se a palavra funciona no automato
    def resolve_palavra(self, palavra):
        # Primeiro verifica se a palavra tem transições fora do alfabeto
        for p in palavra:
            if p not in self.aut.vals:
                return "Essa palavra contém valores fora do alfabeto do automato"

        # Inicia uma fila de operações
        fila = [(self.aut.e_inicial[0], palavra)]  # (estado atual, palavra restante)

        # print(fila)

        # Enquanto a fila não estiver vazia
        while fila:

            # Caso a primeira operação da fila ainda tenha letras na palavra para analisar
            if fila[0][1]:
                for transicao in self.aut.r_transicao[fila[0][0]][fila[0][1][0]]:   # Verifica cada transição da primeira operação da fila
                    # Cria uma nova operação com o proximo estado e com a palavra sem a letra que fez chegar aqui
                    # Coloca essa nova operação na fila
                    fila.append((transicao, fila[0][1][1:]))

            # Caso o Automato seja um E-NFA percorre todos os epsilons sem custar nenhuma letra
            if self.aut.tipo == 'e-nfa':
                # Faz basicamente a mesma coisa que acima
                for transicao in self.aut.r_transicao[fila[0][0]]['E']:
                    fila.append((transicao, fila[0][1][:]))

            # print(fila)

            # Se a operação atual é de um estado final
            # E se não tem mais palavra pra percorrer
            # Então a palavra terminou em um estado final, logo é aceita
            if fila[0][0] in self.aut.e_final and not fila[0][1]:
                return "O automato consegue ler essa palavra"

            # Remove a operação atual da fila
            fila.pop(0)
            # print(fila)
            # print()

        # Quando a fila fica vazia vem pra cá e a palavra não é suficiente
        return "O automato NÃO consegue ler essa palavra"
