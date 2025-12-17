from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])
    
    # Step 1: Check if first row or first column has any zero
    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_zero = any(matrix[i][0] == 0 for i in range(rows))
    
    # Step 2: Use first row and first column as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Step 3: Update the rest of the matrix using markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Step 4: Update first row if needed
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    
    # Step 5: Update first column if needed
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0

# Example usage:
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

setZeroes(matrix)  # modify matrix in-place
print(matrix)       # print the modified matrix
