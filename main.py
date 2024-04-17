#Implementação Smith-Waterman

seq1 = "ACGTT"
seq2 = "ACCTT"

match = 1
mismatch = -1
gap_penalty = -2

rows = len(seq1) + 1
cols = len(seq2) + 1

j = 0
i = 0

score_matrix = [[0 for j in range(cols)] for i in range(rows)]

for j in range(1, cols):
    score_matrix[0][j] = gap_penalty * j

for i in range(1, rows):
    score_matrix[i][0] = gap_penalty * i

for row in score_matrix:
    print(row)

