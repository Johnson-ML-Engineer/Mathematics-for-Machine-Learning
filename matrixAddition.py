row=int(input("Enter the no of rows in matrix :"))
column=int(input("Enter the no of columns in matrix :"))
print(f"Enter {row*column} elements for matrix1:\n")
matrix1=[[int(input()) for i in range(column)] for j in range(row)]
print(f"Enter {row*column} elements for matrix2:\n")
matrix2=[[int(input()) for i in range(column)] for j in range(row)]
matrix_addition = [[matrix1[i][j] + matrix2[i][j] for j in range(column)] for i in range(row)]
print(f"addition of {matrix1} and {matrix2} is \n\n",matrix_addition)

