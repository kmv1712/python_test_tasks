list_input = []
w_h = input().split(' ')
w, h = int(w_h[0]), int(w_h[1])
matrix = [list(input()) for item in range(0, w)]
matrix_out = [[0 for x in range(h)] for y in range(w)]
for i in range(0, w):
    for j in range(0, h):
        if matrix[i][j] == '*':
            matrix_out[i][j] = '*'

            if matrix_out[i][j-1] != '*' and j-1 >= 0:
                matrix_out[i][j-1] = matrix_out[i][j-1] + 1

            if j+1 < h and matrix_out[i][j+1] != '*':
                matrix_out[i][j+1] = matrix_out[i][j+1] + 1

            if matrix_out[i-1][j] != '*' and i-1 >= 0:
                matrix_out[i-1][j] = matrix_out[i-1][j] + 1

            if i+1 < w and matrix_out[i+1][j] != '*':
                matrix_out[i+1][j] = matrix_out[i+1][j] + 1

            if i+1 < w and j+1 < h and matrix_out[i+1][j+1] != '*':
                matrix_out[i+1][j+1] = matrix_out[i+1][j+1] + 1

            if matrix_out[i-1][j-1] != '*' and j-1 >= 0 and i-1 >= 0:
                matrix_out[i-1][j-1] = matrix_out[i-1][j-1] + 1

            if i+1 < w and matrix_out[i+1][j-1] != '*' and j-1 >= 0:
                matrix_out[i+1][j-1] = matrix_out[i+1][j-1] + 1

            if j+1 < h and matrix_out[i-1][j+1] != '*' and i-1 >= 0:
                matrix_out[i-1][j+1] = matrix_out[i-1][j+1] + 1

for item in matrix_out:
    print(''.join([str(char) for char in item]))
