from textos import *
from simulador import Simulador

if __name__ == '__main__':
    automatos = le_arq_entrada()

    for n, automato in enumerate(automatos):
        Simulador(automato).inicia()


        # for p, r in zip(automato.palavras, automato.resultados):
        #     print(p, r)
    # print('Imprimindo resultados em saida.txt')
    automatos_to_text(automatos)
