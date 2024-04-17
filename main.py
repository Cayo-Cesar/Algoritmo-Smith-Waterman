#Implementação Smith-Waterman

seq1 = "AGTACCA" #Vertical
seq2 = "CATTCC" #Horizontal

match = 1
mismatch = -1
gap_penalty = -2

rows = len(seq1) + 1
cols = len(seq2) + 1

j = 0
i = 0

right = None
down = None
diag = None

score_matrix = [[0 for j in range(cols)] for i in range(rows)]

for j in range(1, cols):
    score_matrix[0][j] = gap_penalty * j

for i in range(1, rows):
    score_matrix[i][0] = gap_penalty * i

TODO: Corrigir a implementação da matriz, pois o al
for i in range(1, rows):
    for j in range(1, cols):
        if seq1[i - 1] == seq2[j - 1]:
            score = match
        else:
            score = mismatch

        right = score_matrix[i][j - 1] + gap_penalty
        down = score_matrix[i - 1][j] + gap_penalty
        diag = score_matrix[i - 1][j - 1] + score

        score_matrix[i][j] = max(right, down, diag, 0)

for row in score_matrix:
    print(row)

