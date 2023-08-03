row=int(input("Enter the number of rows in matrix: "))
column=int(input("Enter the number of columns in matrix: "))
print(f"Enter {row*column} elements for the matrix: ")
matrix=[[int(input()) for j in range(column)] for i in range(row)]

print("Matrix before Transpose ",matrix)
transpose = [[matrix[i][j] for i in range(2)] for j in range(3)]
print("Matrix after Transpose ",transpose)