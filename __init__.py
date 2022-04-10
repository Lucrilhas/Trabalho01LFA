from textos import *
from dfa import DFA
from nfa import *

if __name__ == '__main__':
    automatos = le_arq_entrada()

    for automato in automatos:
        # automato.printa_automato()
        if automato.tipo == 'dfa':
            DFA(automato)
        elif automato.tipo == 'nfa':
            nfa_to_dfa(automato)

    #automatos_to_text(automatos)
