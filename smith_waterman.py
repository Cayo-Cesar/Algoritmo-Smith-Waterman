#Implementação do algoritmo de Smith-Waterman para alinhamento global de sequências de DNA
#Autor: Cayo Cesar
#Data: 17/04/2024

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

    # pilha_movimentos = []
    rows = len(seq1) + 1
    cols = len(seq2) + 1

    #Direção de Movimentos
    right = 0
    down = 0
    diag = 0

    #Inicializa a Matriz com 0 em todas as posições
    score_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    #Incrementa a primeira linha e coluna com os valores de gap_penalty * i
    for i in range(1, rows):
        score_matrix[i][0] = gap_penalty * i

    for j in range(1, cols):
        score_matrix[0][j] = gap_penalty * j

    #Preenche a matriz de score verificando se os elementos são iguais ou diferentes( match ou mismatch) e atribuindo o valor correto de acordo com a situação 
    for i in range(1, rows):
        for j in range(1, cols):
            if seq1[i - 1] == seq2[j - 1]:
                score = match
            else:
                score = mismatch

    #Calcula os valores de right, down e diag e atribui o maior valor a posição atual da matriz
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

    #Atribui o maior valor a posição atual da matriz
            score_matrix[i][j] = max(right, down, diag)
    return score_matrix

# Função para inverter a matriz de score
def invert_matrix(matrix):
    inverted_matrix = [list(row) for row in reversed(matrix)]
    return inverted_matrix

# Função para imprimir a matriz de score e salvar em um txt
def print_matrix(matrix, seq1, seq2):
    # Inverte a sequência 1 para imprimir corretamente
    rows = len(matrix)
    cols = len(matrix[0])

    # Salva a matriz em um arquivo txt
    with open('matrix.txt', 'w') as f:
        # Imprime a sequência 2
        seq1_reversed = list(reversed(seq1))
        # Imprime a matriz de score e a sequência 1 ja invertida e é feita a adição do valor U na primeira posição da matriz
        for i in range(rows):
            if i < rows - 1:
                f.write(seq1_reversed[i] + "\t")
            else:
                f.write("U" + "\t")
            for j in range(cols):
                f.write(str(matrix[i][j]) + "\t")
            f.write("\n")
        # Imprime a sequência 2
        f.write("\tU")
        for base in reversed(seq2):
            f.write("\t" + base)
        f.write("\n")

# Leitura das configurações do arquivo
with open('input.txt', 'r') as file:
    seq1 = file.readline().strip()
    seq2 = file.readline().strip()
    gap_penalty = int(file.readline().strip())
    mismatch = int(file.readline().strip())
    match = int(file.readline().strip())
    
# Chamada da função score_matrix
score_matrix = score_matrix(seq1, seq2, match, mismatch, gap_penalty)

# Função para inverter a matriz de score
inverted_matrix = invert_matrix(score_matrix)

# Impressão da matriz de score
print_matrix(inverted_matrix, seq1, seq2)
