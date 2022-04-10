from automato import Automato


class NFA:
    def __init__(self, aut: Automato):
        print(aut.r_transicao)
        self.new_aut = Automato()
        self.old_aut = aut


def nfa_to_dfa(aut: Automato):
    # Cria novos estados a partir de entrada com mais de uma resposta
    for e in aut.estados[:]:
        for v in aut.vals:
            if len(aut.r_transicao[e][v]) > 1:
                # old_estados = aut.r_transicao[e][v]
                aut.r_transicao[e][v] = [''.join(elem for elem in aut.r_transicao[e][v])]
                if (novo_estado := aut.r_transicao[e][v][0]) not in aut.estados:
                    aut.estados.append(novo_estado)

                    # Verifica se esse novo estado é final
                    for f in aut.e_final:
                        if f in novo_estado:
                            aut.e_final.append(novo_estado)
                            break

                    # Cria novas regras de transição para esse estado - Por enquanto vazias
                    aut.r_transicao[novo_estado] = {v:[] for v in aut.vals}

    # Preenche as regras de transições vazias
    for v in aut.vals:
        for os in old_estados:
            print(v, os)
            print(set(aut.r_transicao[novo_estado][v]))
            print(aut.r_transicao[os][v][0])
            aut.r_transicao[novo_estado][v] = set(aut.r_transicao[novo_estado][v]).union([aut.r_transicao[os][v][0]])
            print(aut.r_transicao[novo_estado][v])
            print()




    # print(aut.r_transicao)
    # print(aut.estados)
    # print(aut.e_final)
