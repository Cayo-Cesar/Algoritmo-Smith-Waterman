seq1 = "ATCG" # Vertical
seq2 = "TCG"  # Horizontal

match = 1
mismatch = -1
gap_penalty = -2

rows = len(seq1) + 1  # Removido o adicional +2
cols = len(seq2) + 1  # Removido o adicional +2

right = 0
down = 0
diag = 0

score_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# Inicialização dos valores de penalidade de gap para as linhas e colunas iniciais
for i in range(1, rows):
    score_matrix[i][0] = gap_penalty * i

for j in range(1, cols):
    score_matrix[0][j] = gap_penalty * j

for i in range(1, rows):
    for j in range(1, cols):
        if seq1[i - 1] == seq2[j - 1]:  # Corrigido o acesso aos índices das sequências
            score = match
        else:
            score = mismatch

        right = score_matrix[i][j - 1] + gap_penalty
        down = score_matrix[i - 1][j] + gap_penalty
        diag = score_matrix[i - 1][j - 1] + score

        score_matrix[i][j] = max(right, down, diag)

for row in score_matrix:
    print(row)
