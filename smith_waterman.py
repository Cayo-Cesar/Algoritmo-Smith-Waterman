#Implementação do algoritmo de Smith-Waterman para alinhamento global de sequências de DNA
#Autor: Cayo Cesar
#Data: 17/04/2024

'''
A entrada de dados se da por um arquivo config.txt no formato abaixo:

seq1    # Vertical
seq2    # Horizontal
match
mismatch
gap_penalty

'''

# Função para criar a matriz de score
def score_matrix(seq1, seq2, match, mismatch, gap_penalty):

    # pilha_movimentos = []
    rows = len(seq1) + 1
    cols = len(seq2) + 1

    right = 0
    down = 0
    diag = 0

    score_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        score_matrix[i][0] = gap_penalty * i

    for j in range(1, cols):
        score_matrix[0][j] = gap_penalty * j

    for i in range(1, rows):
        for j in range(1, cols):
            if seq1[i - 1] == seq2[j - 1]:
                score = match
            else:
                score = mismatch

            right = score_matrix[i][j - 1] + gap_penalty
            down = score_matrix[i - 1][j] + gap_penalty
            diag = score_matrix[i - 1][j - 1] + score

            # # Append na pilha de movimentos para a realização do backtracing posteriormente
            # if max(right, down, diag) == diag:
            #     pilha_movimentos.append('D')

            # elif max(right, down, diag) == down:
            #     pilha_movimentos.append('U')

            # elif max(right, down, diag) == right:
            #     pilha_movimentos.append('L')

            score_matrix[i][j] = max(right, down, diag)

    return score_matrix

# Função para imprimir a matriz de score e salvar em um txt
def print_matrix(matrix):
    with open('score_matrix.txt', 'w') as file:
        for row in matrix:
            for value in row:
                print(value, end='\t')
                file.write(str(value) + '\t')
            print()
            file.write('\n')

def invert_matrix(matrix):
    inverted_matrix = [list(row) for row in reversed(matrix)]
    return inverted_matrix

# Leitura das configurações do arquivo
with open('config.txt', 'r') as file:
    seq1 = file.readline().strip()
    seq2 = file.readline().strip()
    match = int(file.readline().strip())
    mismatch = int(file.readline().strip())
    gap_penalty = int(file.readline().strip())

# Chamada da função score_matrix
score_matrix = score_matrix(seq1, seq2, match, mismatch, gap_penalty)

# Função para inverter a matriz de score
inverted_matrix = invert_matrix(score_matrix)

# Impressão da matriz de score
print_matrix(inverted_matrix)
