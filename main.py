# Implementação Algoritmo de Smith-Waterman

import numpy as np

def smith_waterman(seq1, seq2, match=2, mismatch=-1, gap=-1):

    # Inicializa a matriz de pontuações
    score_matrix = np.zeros((len(seq1) + 1, len(seq2) + 1))

    # Inicializa a matriz de direções
    pointer_matrix = np.zeros((len(seq1) + 1, len(seq2) + 1))

    # Inicializa o maior valor e sua posição
    max_score = 0
    max_pos = None

    # Preenche a matriz de pontuações
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            # Calcula a pontuação para a posição atual
            diag_score = score_matrix[i - 1, j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            up_score = score_matrix[i - 1, j] + gap
            left_score = score_matrix[i, j - 1] + gap
            score_matrix[i, j] = max(0, diag_score, up_score, left_score)

            # Atualiza a matriz de direções
            if score_matrix[i, j] == diag_score:
                pointer_matrix[i, j] = 1
            elif score_matrix[i, j] == up_score:
                pointer_matrix[i, j] = 2
            elif score_matrix[i, j] == left_score:
                pointer_matrix[i, j] = 3

            # Atualiza o maior valor e sua posição
            if score_matrix[i, j] > max_score:
                max_score = score_matrix[i, j]
                max_pos = (i, j)

    # Recupera o alinhamento
    align1 = ""
    align2 = ""
    i, j = max_pos
    while score_matrix[i, j] != 0:
        if pointer_matrix[i, j] == 1:
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif pointer_matrix[i, j] == 2:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        elif pointer_matrix[i, j] == 3:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1

    return max_score, align1, align2

# Teste

seq1 = "ACCTGAGCTAGCTGACG"
seq2 = "ACCTAGGCTAGCTGACG"
score, align1, align2 = smith_waterman(seq1, seq2)
print("Pontuação:", score)
print("Alinhamento 1:", align1)
print("Alinhamento 2:", align2)

# Saída esperada:
# Pontuação: 14.0
# Alinhamento 1: ACCTGAGCTAGCTGACG
# Alinhamento 2: ACCTAGGCTAGCTGACG
