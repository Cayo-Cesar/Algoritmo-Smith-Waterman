seq1 = "AGTACCA" # Vertical
seq2 = "CATTCC"  # Horizontal

match = 1
mismatch = -1
gap_penalty = -2

rows = len(seq1) + 2
cols = len(seq2) + 2

score_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(2, rows):
    score_matrix[i][0] = gap_penalty * (i - 1)

for j in range(2, cols):
    score_matrix[0][j] = gap_penalty * (j - 1)

for i in range(1, rows):
    for j in range(1, cols):
        if seq1[i - 2] == seq2[j - 2]:  
            score = match
        else:
            score = mismatch

        right = score_matrix[i][j - 1] + gap_penalty
        down = score_matrix[i - 1][j] + gap_penalty
        diag = score_matrix[i - 1][j - 1] + score

        score_matrix[i][j] = max(right, down, diag)

for row in score_matrix:
    print(row)
