from textos import *
from dfa import *

if __name__ == '__main__':
    automatos = le_arq_entrada()

    for automato in automatos:
        if automato.tipo == 'dfa':
            DFA(automato)
            # automato.printa_automato()

    automatos_to_text(automatos)
