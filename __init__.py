from textos import *
from automato import DFA, nfa_to_dfa

if __name__ == '__main__':
    automatos = le_arq_entrada()

    for n, automato in enumerate(automatos):
        print(f'Iniciando automato {n}')
        # automato.printa_automato()
        if automato.tipo == 'dfa':
            print('Automato é do tipo DFA')
            DFA(automato)
        elif automato.tipo == 'nfa':
            print('Automato é do tipo NFA')
            nfa_to_dfa(automato)
            DFA(automato)
        print(f'Finalizado automato {n}\n')

    print('Imprimindo resultados em saida.txt')
    automatos_to_text(automatos)
