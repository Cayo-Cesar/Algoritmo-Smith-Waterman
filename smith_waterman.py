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

    pilha_movimentos = []
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
            
            score_matrix[i][j] = max(right, down, diag)

    return score_matrix

def backtrack(score_matrix, seq1, seq2, match, mismatch, gap_penalty):
    rows = len(seq1) + 1
    cols = len(seq2) + 1

    i = rows - 1
    j = cols - 1

    align1 = ''
    align2 = ''

    while i > 0 and j > 0:
        score = score_matrix[i][j]
        score_diag = score_matrix[i - 1][j - 1]
        score_up = score_matrix[i][j - 1]
        score_left = score_matrix[i - 1][j]

        if score == score_diag + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            align1 += seq1[i - 1]
            align2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif score == score_left + gap_penalty:
            align1 += seq1[i - 1]
            align2 += '-'
            i -= 1
        elif score == score_up + gap_penalty:
            align1 += '-'
            align2 += seq2[j - 1]
            j -= 1

    while i > 0:
        align1 += seq1[i - 1]
        align2 += '-'
        i -= 1

    while j > 0:
        align1 += '-'
        align2 += seq2[j - 1]
        j -= 1

    align1 = align1[::-1]
    align2 = align2[::-1]

    print(align1)
    print(align2)

    return align1, align2

# Função para imprimir a matriz de score e salvar em um txt
def print_matrix(matrix):
    with open('score_matrix.txt', 'w') as file:
        for row in matrix:
            for value in row:
                print(value, end='\t')
                file.write(str(value) + '\t')
            print()
            file.write('\n')

# Leitura das configurações do arquivo
with open('config.txt', 'r') as file:
    seq1 = file.readline().strip()
    seq2 = file.readline().strip()
    match = int(file.readline().strip())
    mismatch = int(file.readline().strip())
    gap_penalty = int(file.readline().strip())

# Chamada da função score_matrix
score_matrix = score_matrix(seq1, seq2, match, mismatch, gap_penalty)

# Impressão da matriz de score
print_matrix(score_matrix)

# Chamada da função backtrack
align1, align2 = backtrack(score_matrix, seq1, seq2, match, mismatch, gap_penalty)
