#Implementação do algoritmo de Smith-Waterman para alinhamento global de sequências de DNA

'''
A entrada de dados se da por um arquivo input.txt no formato abaixo:

seq1    # Vertical
seq2    # Horizontal
match
mismatch
gap_penalty

'''

# Função para criar a matriz de score
def score_matrix(seq1, seq2, match, mismatch, gap_penalty):

    rows = len(seq1) + 1
    cols = len(seq2) + 1

    score_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        score_matrix[i][0] = gap_penalty * i

    for j in range(1, cols):
        score_matrix[0][j] = gap_penalty * j

    for i in range(1, rows):
        for j in range(1, cols):
            score = match if seq1[i - 1] == seq2[j - 1] else mismatch

            # Determina a lista de direções, podendo ir pra direita, baixo ou diagonal
            directions = [(i, j - 1), (i - 1, j), (i - 1, j - 1)]
            # Map aplica a score_matrix a soma de score se for diagonal ou de gap se for direita ou baixo
            right, down, diag = map(lambda x: score_matrix[x[0]][x[1]] + (score if x == (i - 1, j - 1) else gap_penalty), directions)
            # Adiciona o maior dos 3 na matriz
            score_matrix[i][j] = max(right, down, diag)

    return score_matrix


def backtracing(score_matrix, seq1, seq2, match, mismatch, gap_penalty):

    rows = len(seq1) + 1
    cols = len(seq2) + 1

    i = rows - 1
    j = cols - 1

    # Inicialização da pilha para armazenar os movimentos
    stack = []

    # Percorrer a matriz de scores
    while i > 0 and j > 0:
        score = score_matrix[i][j]
        score_diag = score_matrix[i - 1][j - 1]
        score_up = score_matrix[i][j - 1]
        score_left = score_matrix[i - 1][j]

        # Determina o movimento atual e adiciona à pilha
        if score == score_diag + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            stack.append('D')  # Diagonal
            i -= 1
            j -= 1
        elif score == score_left + gap_penalty:
            stack.append('U')  # Up
            i -= 1
        elif score == score_up + gap_penalty:
            stack.append('L')  # Left
            j -= 1

    # Completa a pilha 
    while i > 0:
        stack.append('U')
        i -= 1
    while j > 0:
        stack.append('L')
        j -= 1

    stack.reverse()

    # Reconstrução dos alinhamentos
    align1 = ''
    align2 = ''
    i = 0
    j = 0
    for move in stack:
        if move == 'D':
            align1 += seq1[i]
            align2 += seq2[j]
            i += 1
            j += 1
        elif move == 'U':
            align1 += seq1[i]
            align2 += '-'
            i += 1
        elif move == 'L':
            align1 += '-'
            align2 += seq2[j]
            j += 1

    # Impressão dos alinhamentos
    with open('output.txt', 'a') as f:
        f.write("\n\nAlinhamento:\n\n")
        f.write(align1 + "\n")
        f.write(align2 + "\n")

    # print(align1)
    # print("\n")
    # print(align2)
    
    return align1, align2

def invert_matrix(matrix):
    inverted_matrix = [list(row) for row in reversed(matrix)]
    return inverted_matrix

def print_matrix(matrix, seq1, seq2, match, mismatch, gap_penalty):
    rows = len(matrix)
    cols = len(matrix[0])

    # Último número da matriz (canto superior direito)
    last_score = matrix[0][-1]

    with open('output.txt', 'w') as f:
        # Imprime a sequência 2
        seq1_reversed = list(reversed(seq1))
        # Imprime a matriz de score e a sequência 1 já invertida e é feita a adição do valor U na primeira posição da matriz
        for i in range(rows):
            if i < rows - 1:
                f.write(seq1_reversed[i].center(3) + "\t")
            else:
                f.write("U".center(3) + "\t")
            for j in range(cols):
                f.write(str(matrix[i][j]).center(3) + "\t")
            f.write("\n")
        f.write("\t U  ")
        for base in seq2:
            f.write("\t" + base.center(3))
        # Imprime os valores de match, mismatch, gap_penalty e o score
        f.write("\n\n========== SCORE: " + str(last_score) + " | Match: " + str(match) + " | Mismatch: " + str(mismatch) + " | Gap Penalty: " + str(gap_penalty) + " ==========")
        f.write("\n\nMEU NUMERO DA CHAMADA EH 7")
        
with open('input.txt', 'r') as file:
    seq1 = file.readline().strip()
    seq2 = file.readline().strip()
    gap_penalty = int(file.readline().strip())
    mismatch = int(file.readline().strip())
    match = int(file.readline().strip())
    
score_matrix = score_matrix(seq1, seq2, match, mismatch, gap_penalty)

inverted_matrix = invert_matrix(score_matrix)

print_matrix(inverted_matrix, seq1, seq2, match, mismatch, gap_penalty)

align1, align2 = backtracing(score_matrix, seq1, seq2, match, mismatch, gap_penalty)

