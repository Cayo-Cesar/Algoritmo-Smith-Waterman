#Implementação do algoritmo de Smith-Waterman para alinhamento local de sequências de DNA
#Autor: Cayo Cesar
#Data: 17/04/2024

# Função para imprimir a matriz de score e salvar em um txt
def print_matrix(matrix):
    with open('score_matrix.txt', 'w') as file:
        for row in matrix:
            for value in row:
                print(value, end='\t')
                file.write(str(value) + '\t')
            print()
            file.write('\n')l

#Sequencias de DNA
seq1 = "ATCG" # Vertical
seq2 = "TCG"  # Horizontal

#Scores
match = 1
mismatch = -1
gap_penalty = -2

# Inicialização das linhas e colunas da matriz de score
rows = len(seq1) + 1 
cols = len(seq2) + 1  

# Inicialização do valor das variaveis de direção
right = 0
down = 0
diag = 0

# Inicialização da matriz de score
score_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# Inicialização dos valores de penalidade de gap para as linhas e colunas iniciais
for i in range(1, rows):
    score_matrix[i][0] = gap_penalty * i

for j in range(1, cols):
    score_matrix[0][j] = gap_penalty * j

# Preenchimento da matriz de score
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

# Impressão da matriz de score
print_matrix(score_matrix)
