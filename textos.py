
def le_arq_entrada():
    # Lê o arquivo de entrada:
    with open('entrada.txt') as f:
        conteudo = f.read()

    # Separa as instancias de entrada:
    entradas = []
    aux = ''
    for char in conteudo:
        if char == '{':
            aux = ''
        elif char == '}':
            entradas.append(aux)
        else:
            aux += char


    return [Automato(entrada) for entrada in entradas]

class Automato:
    def __init__(self, txt_entrada):
        self.estados = []
        self.r_transicao = []
        self.e_inicial = []
        self.e_final = []
        self.vals = []
        self.tipo = 'dfa'
        self.palavras = []
        self.resultados = []

        self.interpreta_entrada(txt_entrada)

    def interpreta_entrada(self, txt_entrada):
        # Interpreta os dados para as variaveis
        get_rt = False
        get_ef = False
        get_pl = False

        for lin in txt_entrada.split('\n'):
            if get_rt:
                if ']' in lin:
                    get_rt = False
                else:
                    self.r_transicao.append(remove_special_chars(lin).split(','))
            elif r'"regras_de_transicao":' in lin:
                get_rt = True

            elif r'"estado_inicial":' in (rms:=remove_special_chars(lin)):
                self.e_inicial = [rms.replace(r'"estado_inicial":', '')]

            elif get_ef:
                if ']' in lin:
                    get_ef = False
                else:
                    self.e_final.append(remove_special_chars(lin))
            elif r'"estado_final":' in lin:
                get_ef = True

            elif get_pl:
                if ']' in lin:
                    get_pl = False
                else:
                    self.palavras.append(remove_special_chars(lin).split(','))
            elif r'"palavras":' in lin:
                get_pl = True

        # Pega os estados a partir das regras de transição
        for e1, e2, v in self.r_transicao:
            if e1 not in self.estados:
                self.estados.append(e1)
            if e2 not in self.estados:
                self.estados.append(e2)
            if v not in self.vals:
                self.vals.append(v)

        # Transforma regra de transição em dicionario
        dicionario = {}
        for e in self.estados:
            dicionario[e] = {}
            for v in self.vals:
                dicionario[e][v] = []

        for e1, e2, v in self.r_transicao:
            dicionario[e1][v].append(e2)

        for k in dicionario:
            for s0 in dicionario[k]:
                if len(dicionario[k][s0]) > 1:
                    self.tipo = 'nfa'

        self.r_transicao = dicionario



    # Imprime os valores do automato
    def printa_automato(self):
        print(f"Estados: {self.estados}\n"
              f"Regras de Transição: {self.r_transicao}\n"
              f"Estado inicial: {self.e_inicial}\n"
              f"Estado final: {self.e_final}\n"
              f"Alfabeto: {self.vals}\n"
              f"Palavras: {self.palavras}\n"
              f"Tipo: {self.tipo}\n"
              f"Resultados: {self.resultados}")



def remove_special_chars(txt):
    return txt.replace(' ', '').replace('\n', '').replace('\t', '')

def automatos_to_text(automatos):
    text = ''

    for aut in automatos:
        text += '{\n'
        text += f'\tEstados: {aut.estados}\n'
        text += f'\tEstado inicial: {aut.e_inicial}\n'
        text += f'\tEstado final: {aut.e_final}\n'
        text += f'\tAlfabeto: {aut.vals}\n'


        text += '\tRegras de transição:[\n\t\t\t\t'
        for a in aut.vals:
            text += f'{a}\t\t\t\t\t'
        text += '\n'

        for e in aut.estados:
            text += f'\t\t{e}\t\t'
            for v in aut.vals:
                text += f'{aut.r_transicao[e][v]}\t\t\t\t'
            text += '\n'
        text += '\t]\n'



        text += '\tPalavras:[\n'
        for p, r in zip(aut.palavras, aut.resultados):
            text += f'\t\t{p}\t->\t{r}\n'
        text += '\t]\n'
        text += f'\tTipo: {aut.tipo}\n'
        text += '}\n\n'

    with open('saida.txt', 'w') as f:
        f.write(text)